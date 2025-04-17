#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import argparse
import pyedflib
import datetime
os.chdir(r"/home/greydon/Documents/GitHub/edf-epoch")
from ext_lib.edflibpy import EDFreader as EDFLIBReader


debug=False
if debug:
	import glob
	class Namespace:
		def __init__(self, **kwargs):
			self.__dict__.update(kwargs)
	
	sub_num='sub-0'
	ses_num='ses-013'
	
	out_dir='/home/greydon/Downloads'
	bids_dir=r'/media/greydon/Snobeanery/data/ieeg_data/bids'
	
	#data_fname=glob.glob(f'{bids_dir}/{sub_num}/{ses_num}/ieeg/{sub_num}_{ses_num}_task-*_ieeg.edf')
	data_fname=f'/home/greydon/Downloads/Fetterly~ Jess_9a6db4dd-8503-49bc-8b42-3fd452dafc97_stim.EDF'
	out_fname = os.path.splitext(data_fname)[0]+'_epoch.edf'
	start_time = 0
	end_time= 920
	chans_keep=None
	args = Namespace(data_fname=data_fname, start_time=start_time, end_time=end_time,chans_keep=chans_keep,out_fname=out_fname)


def main(args):
	
	if args.out_fname is not None:
		out_fname = args.out_fname
	else:
		out_fname = os.path.splitext(args.data_fname)[0]+'_epoch.edf'
	
	
	data_fname=r"/media/greydon/lhsc_data/datasets/ieeg_stim/ccep_data/sub-P046/ses-001/ieeg/sub-P046_ses-001_task-stim_run-01_ieeg.edf"

	signals, signal_headers, header = pyedflib.highlevel.read_edf(data_fname,None,None,digital=False,verbose=True)
	all_labels=[signal_headers[x]['label'] for x in range(len(signal_headers))]
	
	
	
	hdl = EDFLIBReader(data_fname)
	events=hdl.annotationslist
	events=[list(x) for x in events]

	# determine the annoation data block index
	ch_indx = hdl.getNumSignals()

	for i in ch_indx:
		signal_headers[i]['physical_min']=int(header['SignalHeaders'][i]['physical_min'])
		signal_headers[i]['physical_max']=int(header['SignalHeaders'][i]['physical_max'])
		signal_headers[i]['sample_rate']=header['sampling_frequency']
		signal_headers[i]['sample_frequency']=header['sampling_frequency']

	signal_headers[-1]['physical_min']=42900000

	pyedflib.highlevel.write_edf(out_fname, signals, header['SignalHeaders'], header)
	

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


