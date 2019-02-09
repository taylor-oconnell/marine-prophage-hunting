#!/usr/bin/env bash
#This script streams FASTQ data from the Sequence Read Archive for a user-specified SRA run ID
#and maps the reads against a user-specified database using bowtie2

SRA_ID=$1

fastq-dump --split-spot -Z --readids --skip-technical --read-filter pass --dumpbase --clip ${SRA_ID} | \
bowtie2 -x all_MarRef_prophages --interleaved - --xeq --no-unal -S ${SRA_ID}.sam
