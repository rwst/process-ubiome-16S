This takes raw data that you can get from ubiome.com and has scripts to

 1. merge paired reads into `merged.fa`

 2. classify using the RDP classifier

The code is provided as-is with no warranty whatsoever.

Prerequisites:
==============

You need to know how to install and use

 - Biopython on top of Python 3.6

 - Trimmomatic, see https://github.com/timflutre/trimmomatic

 - RDP, see https://sourceforge.net/projects/rdp-classifier

Usage:
======

Assuming you have:
```
ssr_123456__R1__L001.fastq
ssr_123456__R1__L002.fastq
ssr_123456__R1__L003.fastq
ssr_123456__R1__L004.fastq
ssr_123456__R2__L001.fastq
ssr_123456__R2__L002.fastq
ssr_123456__R2__L003.fastq
ssr_123456__R2__L004.fastq
```
The procedure would be:
```
python3 merge_ubiome.py ssr_123456
cat merged_full*.fa >merged_full.fa
sh RDP_classify.sh
```
These scripts HAVE to be tweaked to suit your needs, like paths etc.

You might want to retrain RDP with new data but that's for experts
at the moment. The output from RDP could be changed to the BIOM format
to be analyzed using the excellent R phyloseq module. It's up to you.

Ralf Stephan
