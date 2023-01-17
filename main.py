#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import argparse
import pyedflib
import datetime
import io

debug=False


if debug:
	class Namespace:
		def __init__(self, **kwargs):
			self.__dict__.update(kwargs)
	
	data_fname = '/media/greydon/Snobeanery/data/ieeg_data/bids/sub-101/ses-015/ieeg/sub-101_ses-015_task-stim_run-02_ieeg.edf'
	start_time = 162.566
	end_time= 426.657
	chans_keep=None
	args = Namespace(data_fname=data_fname, start_time=start_time, end_time=end_time,chans_keep=chans_keep)

def main(args):
	
	out_fname = os.path.splitext(args.data_fname)[0]+'_epoch.edf'
	
	#read in the file
	ef = pyedflib.EdfReader(args.data_fname)
	header = ef.getHeader()
	annotation_data=ef.readAnnotations()
	labels = ef.getSignalLabels()
	sf = int(ef.samples_in_datarecord(1) / ef.datarecord_duration)
	header['startdate'] =  (header['startdate'] + datetime.timedelta(seconds=args.start_time))
	
	if args.chans_keep is None:
		args.chans_keep=labels
	
	n_samps=[]
	signal_headers=[]
	for chn in range(len(labels)):
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
		n_samps.append(ef.samples_in_datarecord(chn))
	
	n_samps=np.array(n_samps)/ef.datarecord_duration
	blocksize = int(np.sum(n_samps) * 2)
	
	# determine the annoation data block index
	ch_indx = [i for i,x in enumerate(labels) if any(y==x for y in args.chans_keep)]
	
	# determine the size of the data block
	start_sample = int(args.start_time*sf)
	stop_sample = int(args.end_time*sf)
	
	sigbufs = [np.zeros(stop_sample-start_sample,np.int32,'C') for i in np.arange(len(ch_indx))]
	for i in ch_indx:
		sigbufs[i][:] = ef.readSignal(i, start_sample, stop_sample-start_sample)
		print(f"Done channel {i}")
	
	file_out = pyedflib.EdfWriter(out_fname, len(ch_indx), file_type=pyedflib.FILETYPE_EDFPLUS)
	file_out.setSamplefrequency=sf
	file_out.setSignalHeaders(signal_headers)
	file_out.setHeader(header)
	file_out.recording_start_time.replace(microsecond=header['startdate'].microsecond)
	file_out.writeSamples(sigbufs, digital=False)
	
	file_out.writeAnnotation((header['startdate'].microsecond/1000000), -1, "Starting")
	if isinstance(annotation_data,tuple):
		for row in zip(annotation_data[0],annotation_data[1],annotation_data[2]):
			if row[0]>= args.start_time and row[0] <= args.end_time:
				file_out.writeAnnotation(row[0], row[1], row[2])
	
	
	
	file_out.close()
	ef.close()
	
	from helpers import EDFReader
	file_in = EDFReader()
	header = file_in.open(out_fname)
	
	with open(out_fname, 'rb') as fid:
		fid.seek(184, io.SEEK_SET)
		data_offset=int(fid.read(8).decode())
		fid.read(44)
		fid.read(8).decode()
		dur_record=int(fid.read(8).decode())
		n_signals=int(fid.read(4).decode())
		
		
	with open(out_fname, 'rb') as fid:
		fid=open(out_fname, 'rb')
		pat = '([+-]\\d+\\.?\\d*)(\x15(\\d+\\.?\\d*))?(\x14.*?)\x14\x00'
		assert(fid.tell() == 0)
		fid.seek(np.int64(data_offset) + np.int64(0) * np.int64(blocksize))
		read_idx = 0
		for i in range(len(n_samps)):
			buf = fid.read(np.int64(n_samps[i])*2)
		buf = fid.read(np.int64(57)*2)
		raw = re.findall(pat, buf.decode('latin-1'))
		if raw:
			list(map(list, [x+(0,) for x in raw]))
		
		fid.close()

if __name__ == "__main__":

	# Input arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--data_fname', help='Path to original EDF file.', required=True)
	parser.add_argument('-s', '--start_time', type=float, help='Start time of epoch (seconds i.e. 1037.371).', required=True)
	parser.add_argument('-e', '--end_time', type=float, help='End time of epoch (seconds i.e. 1244.652).', required=True)
	parser.add_argument('-c', '--chans_keep', type=list, help='Comma seperated list of channel names to keep (i.e. "LAHC1","LAHC2","LAHC3").',default=None)
	args = parser.parse_args()

	main(args)