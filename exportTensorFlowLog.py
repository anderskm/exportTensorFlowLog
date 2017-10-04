from tensorflow.python.summary import event_accumulator
import time
import csv
import sys
import os
import collections

# '/home/anmo/AU_O_drive/ST_SPGroup/Projekter/2017_Noisy_labels/logs/slic_varying_noise_0.5/vgg_noise_model_train_procedure3__max0__slic_size_10_noise_0.5_trace_1e-2_noise_kernel_size_3x3_lr_0.01_wd_0.0001_fc_32_layers_20.0_2017.05.07_06.42.46/events.out.tfevents.1494132171.lena'

summariesDefault = ['scalars','histograms','images','audio','compressedHistograms'];

class Timer(object):
	# Source: https://stackoverflow.com/a/5849861
	def __init__(self, name=None):
		self.name = name

	def __enter__(self):
		self.tstart = time.time()

	def __exit__(self, type, value, traceback):
		if self.name:
			print('[%s]' % self.name)
			print('Elapsed: %s' % (time.time() - self.tstart))

def exitWithUsage():
	print(' ');
	print('Usage:');
	print('   python readLogs.py <output-folder> <output-path-to-csv> <summaries>');
	print('Inputs:');
	print('   <input-path-to-logfile>  - Path to TensorFlow logfile.');
	print('   <output-folder>          - Path to output folder.');
	print('   <summaries>              - (Optional) Comma separated list of summaries to save in output-folder. Default: ' + ', '.join(summariesDefault));
	print(' ');
	sys.exit();

if (len(sys.argv) < 3):
	exitWithUsage();

inputLogFile = sys.argv[1];
outputFolder = sys.argv[2];

if (len(sys.argv) < 4):
	summaries = summariesDefault;
else:
	if (sys.argv[3] == 'all'):
		summaries = summariesDefault;
	else:
		summaries = sys.argv[3].split(',');

print(' ');
print('> Log file: ' + inputLogFile);
print('> Output folder: ' + outputFolder);
print('> Summaries: ' + ', '.join(summaries));

if any(x not in summariesDefault for x in summaries):
	print('Unknown summary! See usage for acceptable summaries.');
	exitWithUsage();


print(' ');
print('Setting up event accumulator...');
with Timer():
	ea = event_accumulator.EventAccumulator(inputLogFile,
  	size_guidance={
      	event_accumulator.COMPRESSED_HISTOGRAMS: 0, # 0 = grab all
      	event_accumulator.IMAGES: 0,
      	event_accumulator.AUDIO: 0,
      	event_accumulator.SCALARS: 0,
      	event_accumulator.HISTOGRAMS: 0,
	})

print(' ');
print('Loading events from file*...');
print('* This might take a while. Sit back, relax and enjoy a cup of coffee :-)');
with Timer():
	ea.Reload() # loads events from file

print(' ');
print('Log summary:');
tags = ea.Tags();
for t in tags:
	tagSum = []
	if (isinstance(tags[t],collections.Sequence)):
		tagSum = str(len(tags[t])) + ' summaries';
	else:
		tagSum = str(tags[t]);
	print('   ' + t + ': ' + tagSum);


if ('audio' in summaries):
	print(' ');
	print('Exporting audio...');
	with Timer():
		print('   Audio is not yet supported!');

if ('compressedHistograms' in summaries):
	print(' ');
	print('Exporting compressedHistograms...');
	with Timer():
		print('   Compressed histograms are not yet supported!');


if ('histograms' in summaries):
	print(' ');
	print('Exporting histograms...');
	with Timer():
		print('   Histograms are not yet supported!');

if ('images' in summaries):
	print(' ');
	print('Exporting images...');
	imageDir = outputFolder + 'images'
	print('Image dir: ' + imageDir);
	with Timer():
		imageTags = tags['images'];
		for imageTag in imageTags:
			images = ea.Images(imageTag);
			imageTagDir = imageDir + '/' + imageTag;
			if not os.path.isdir(imageTagDir):
				os.makedirs(imageTagDir);
			for image in images:
				imageFilename = imageTagDir + '/' + str(image.step) + '.png';
				with open(imageFilename,'w+') as f:
					f.write(image.encoded_image_string);

if ('scalars' in summaries):
	print(' ');
	csvFileName =  os.path.join(outputFolder,'scalars.csv');
	print('Exporting scalars to csv-file...');
	print('   CSV-path: ' + csvFileName);
	scalarTags = tags['scalars'];
	with Timer():
		with open(csvFileName,'wb') as csvfile:
			logWriter = csv.writer(csvfile, delimiter=',');

			# Write headers to columns
			headers = ['wall_time','step'];
			for s in scalarTags:
				headers.append(s);
			logWriter.writerow(headers);
	
			vals = ea.Scalars(scalarTags[0]);
			for i in range(len(vals)):
				v = vals[i];
				data = [v.wall_time, v.step];
				for s in scalarTags:
					scalarTag = ea.Scalars(s);
					S = scalarTag[i];
					data.append(S.value);
				logWriter.writerow(data);

print(' ');
print('Bye bye...');

