# exportTensorFlowLog
Export TensorFlow logs to common easy to read formats (csv-files, png-images, ...)
<table>
<tr>
<th>Summary</th>
<th>Format</th>
</tr>
<tr>
<td>Scalars</td>
<td>1 csv-file. One column per scalar summary tag.</td>
</tr>
<tr>
<td>Images</td>
<td>Multiple PNG-images structured in folderes depending on the name of the summary tags.</td>
</tr>
<tr>
<td>Audio</td>
<td>Not yet supported.</td>
</tr>
<tr>
<td>Histograms</td>
<td>Not yet supported.</td>
</tr>
<tr>
<td>Distributions</td>
<td>Not yet supported.</td>
</tr>
<tr>
<td>Tensors</td>
<td>Not yet supported.</td>
</tr>
</table>

Tested on TensorFlow version 0.12.0 and Python 2.7.

Newer versions may have event_accumulator located differently. Adjust import of it accordingly. See table below.

<table>
<tr>
<th>TF version</th>
<th>event_accumulator location</th>
<th>event_accumulator import</th>
</tr>
<tr>
<td>&lt;1.1</td>
<td><a href="https://github.com/tensorflow/tensorflow/tree/c62a66bcd4d6f009e0b416055e2ecb8ef50fd0aa/tensorflow/python/summary">from tensorflow.python.summary import event_accumulator</a></td>
<td>from tensorflow.python.summary import event_accumulator</td>
</tr>
<tr>
<td>1.1</td>
<td><a href="https://github.com/tensorflow/tensorflow/tree/1ec6ed51182adf8f1b03a3188c16cd8a45ca6c85/tensorflow/tensorboard/backend/event_processing">tensorflow/tensorflow/tensorboard/backend/event_processing</a></td>
<td>from tensorflow.tensorboard.backend.event_processing import event_accumulator</td>
</tr>
<tr>
<td>&gt;1.3?</td>
<td>Moved to TensorBoard<br>
<a href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/backend/event_processing">tensorboard/tensorboard/backend/event_processing/</a></td>
<td>from ??? import event_accumulator</td>
</tr>
</table>

## Usage

```
python readLogs.py <output-folder> <output-path-to-csv> <summaries>

Inputs:
   <input-path-to-logfile>  - Path to TensorFlow logfile.
   <output-folder>          - Path to output folder.
   <summaries>              - (Optional) Comma separated list of summaries to save in output-folder. Default: scalars, histograms, images, audio, compressedHistograms
```
