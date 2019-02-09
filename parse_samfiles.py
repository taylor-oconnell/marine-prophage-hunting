import glob
import argparse
import pysam
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_reads_mapped(bamfile):

	bamfile = pysam.AlignmentFile(bamfile, 'rb')
	ref_reads_mapped = {}
	#Get reads mapped to each reference
	for genome in bamfile.references:
		genome_id = genome.split("_")[-1]
		reads_mapped = sum(1 for read in bamfile.fetch(genome))
		ref_reads_mapped[genome_id] = reads_mapped
	
	return ref_reads_mapped


def plot_hits_heatmap(hits_by_sample_df):

	fig, ax = plt.subplots(1,1, figsize=(6,5))
	sns.heatmap(hits_by_sample_df, cmap='YlGnBu', robust=True, ax=ax)
	plt.tight_layout()
	fig.savefig('marref_prophages_tara_oceans_heatmap.pdf')
	


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Parse indexed bam files and generate heatmap of hits per sample to the reference sequences')
	parser.add_argument('bamfile_dir', help='Directory with the indexed bamfiles to parse')
	args = parser.parse_args()
	
	#Get hits to reference genomes for each sample
	hits_per_sample = {}
	for bamfile in glob.glob(args.bamfile_dir + "/*.bam"):
		sample = bamfile.split("/")[-1][:-4]
		hits = get_reads_mapped(bamfile)
		hits_per_sample[sample] = hits

	#Combine hits for each sample into a dataframe
	hits_per_sample_df = pd.DataFrame.from_dict(hits_per_sample)
	print(hits_per_sample_df.head())

	#Plot heatmap of hits to reference sequences for all samples
	plot_hits_heatmap(hits_per_sample_df)

