from sys import *
from subprocess import run
from Bio import Seq, SeqRecord, SeqIO

TRIM1 = 'java -jar /home/ralf/Trimmomatic-0.38/trimmomatic-0.38.jar PE -phred33'
TRIM2 = 'output_forward_paired.fq output_forward_unpaired.fq output_reverse_paired.fq output_reverse_unpaired.fq ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'

arg = argv[1]
for lane in range(1,5):
    trim_file1 = '{}__R1__L00{}.fastq'.format(arg, lane)
    trim_file2 = '{}__R2__L00{}.fastq'.format(arg, lane)
    cmd = TRIM1.split() + [trim_file1, trim_file2] + TRIM2.split()
    run(cmd)
    print('Processing Lane {}'.format(lane))
    recs = SeqIO.parse('output_forward_paired.fq', 'fastq')
    rdict = SeqIO.to_dict(SeqIO.parse('output_reverse_paired.fq', 'fastq'))
    n = 0
    try:
        seqs_full = []
        for rec in recs:
            seq2 = rdict.get(rec.id)
            if not seq2:
                print('No pair: {}'.format(rec.id))
                continue
            s = (str(rec.seq)[11:].rstrip()
                    + str(seq2.seq.reverse_complement()).rstrip())
            assert '\n' not in s
            seq = SeqRecord.SeqRecord(Seq.Seq(s))
            seq.id = rec.id.rstrip()
            seq.description = ''
            seqs_full.append(seq)
            n = n + 1
        SeqIO.write(seqs_full, 'merged_full_L{}.fa'.format(lane), 'fasta')
        print('Merged paired sequences: {}'.format(n))

        seqs_half = []
        recs = list(SeqIO.parse('output_forward_unpaired.fq', 'fastq'))
        seqs_half = seqs_half + recs
        n = len(recs)
        recs = list(SeqIO.parse('output_reverse_unpaired.fq', 'fastq'))
        seqs_half = seqs_half + recs
        SeqIO.write(seqs_half, 'merged_half_L{}.fa'.format(lane), 'fasta')
        print('Added unpaired sequences: {}'.format(n+len(recs)))
        
    except RuntimeError:
        print('exception caught')
        pass

