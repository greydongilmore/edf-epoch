#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import argparse
import pyedflib
debug=False


if debug:
	import glob
	class Namespace:
		def __init__(self, **kwargs):
			self.__dict__.update(kwargs)
	
	sub_num='sub-055'
	ses_num='ses-013'
	
	out_dir='/home/greydon/Downloads'
	bids_dir=r'/media/greydon/Snobeanery/data/ieeg_data/bids'
	
	data_fname=glob.glob(f'{bids_dir}/{sub_num}/{ses_num}/ieeg/{sub_num}_{ses_num}_task-*_ieeg.edf')
	out_fname = os.path.join(out_dir,f'{sub_num}_ses-{ses_num}_desc-task_ieeg.edf')
	start_time = 3931.914
	end_time= 4269.992
	chans_keep=None
	args = Namespace(data_fname=data_fname, start_time=start_time, end_time=end_time,chans_keep=chans_keep,out_fname=out_fname)


def main(args):
	
	if args.out_fname is not None:
		out_fname = args.out_fname
	else:
		out_fname = os.path.splitext(args.data_fname)[0]+'_epoch.edf'
	
	ef = pyedflib.EdfReader(args.data_fname)
	header = ef.getHeader()
	nch  = ef.signals_in_file
	fs = int(ef.samples_in_datarecord(1) / ef.datarecord_duration)
	annotation_data=ef.readAnnotations()
	
	if args.chans_keep is None:
		args.chans_keep=[x for x in range(nch)]
	
	# determine the annoation data block index
	ch_indx = [i for i,x in enumerate(range(nch)) if any(y==x for y in args.chans_keep)]
	
	signal_headers=[]
	for chn in ch_indx:
		signal_headers.append({
			'label': ef.getLabel(chn),
			'dimension': ef.getPhysicalDimension(chn),
			'sample_rate': int(ef.samples_in_datarecord(chn) / ef.datarecord_duration),
			'sample_frequency': int(ef.samples_in_datarecord(chn) / ef.datarecord_duration),
			'physical_max':ef.getDigitalMaximum(chn),
			'physical_min':  ef.getDigitalMinimum(chn),
			'digital_max': ef.getDigitalMaximum(chn),
			'digital_min': ef.getDigitalMinimum(chn),
			'prefilter':ef.getPrefilter(chn),
			'transducer': ef.getTransducer(chn)
		})
	
	
	start_sample=int(args.start_time*fs)
	stop_sample=int(args.end_time*fs)
	sigbufs = [np.zeros(int(stop_sample-start_sample),np.int16,order='C') for x in range(len(ch_indx))]
	for i in ch_indx:
		sigbufs[i][:]=ef.readSignal(i,start_sample, int(stop_sample-start_sample),digital=False)
		print(f"Done channel {i}")
	
	
	file_out = pyedflib.EdfWriter(out_fname, len(ch_indx), file_type=pyedflib.FILETYPE_EDFPLUS)
	file_out.setSignalHeaders(signal_headers)
	file_out.setHeader(header)
	file_out.writeSamples(sigbufs, digital=False)
	
	for onset,duration,event in zip(annotation_data[0],annotation_data[1],annotation_data[2]):
		if onset > args.start_time and onset < args.end_time:
			print(onset-args.start_time, duration, event)
			file_out.writeAnnotation(onset-args.start_time, duration, event)
	
	file_out.close()
	ef.close()


if __name__ == "__main__":

	# Input arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--data_fname', help='Path to original EDF file.', required=True)
	parser.add_argument('-o', '--out_fname', help='Path to ouput EDF file.', required=False)
	parser.add_argument('-s', '--start_time', type=float, help='Start time of epoch (seconds i.e. 1037.371).', required=True)
	parser.add_argument('-e', '--end_time', type=float, help='End time of epoch (seconds i.e. 1244.652).', required=True)
	parser.add_argument('-c', '--chans_keep', type=list, help='Comma seperated list of channel names to keep (i.e. "LAHC1","LAHC2","LAHC3").',default=None)
	args = parser.parse_args()
	
	main(args)


