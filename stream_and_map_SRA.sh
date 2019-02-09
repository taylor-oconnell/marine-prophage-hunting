#!/usr/bin/env bash
SRA_ID=$1

fastq-dump --split-spot -Z --readids --skip-technical --read-filter pass --dumpbase --clip ${SRA_ID} | bowtie2 -x all_MarRef_prophages --interleaved - --xeq --no-unal -S ${SRA_ID}.sam
