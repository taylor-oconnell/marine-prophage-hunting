# marine-prophage-hunting

In this study, we are examining the abundance and distribution patterns of prophages in marine bacteria. We're using MarRef (https://mmp.sfb.uit.no/databases/marref/) as a reference database of marine bacterial species and we're predicting prophages in those genomes using PhiSpy (https://github.com/linsalrob/PhiSpy). To verify the prophages predicted by PhiSpy, we search for evidence of them in marine viromes under the assumption that we should be able to observe the true prophages in viral metagenomic data. We mapped reads from 112 viromes from the Tara Oceans project against the predicted prophage sequences using bowtie2. 

Because most users don't want to sacrifice the kind of disk space needed to download 100+ metagenomes, we alleviate the need for downloading data to disk by using fastq-dump (https://ncbi.github.io/sra-tools/fastq-dump.html) from the SRA toolkit to stream fastq data from the SRA and pipe it directly into bowtie2. SAM files output by bowtie2 are then converted to BAM format, sorted, and indexed using samtools (http://samtools.sourceforge.net/). Finally, the abundance profiles of the prophages are visualized in a heatmap.

This is an ongoing project just in its infancy. Be sure to check back for more!
