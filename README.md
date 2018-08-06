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

You might want to retrain RDP with new data but that's for experts
at the moment. The output from RDP could be changed to the BIOM to
be analyzed using the excellent R phylogeny module. It's up to you.

Ralf Stephan
