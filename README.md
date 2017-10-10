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

Tested on TensorFlow version 0.11.0, 1.1.0 and 1.3.0 and Python 2.7 and 3.6.

## Usage

```
python readLogs.py <output-folder> <output-path-to-csv> <summaries>

Inputs:
   <input-path-to-logfile>  - Path to TensorFlow logfile.
   <output-folder>          - Path to output folder.
   <summaries>              - (Optional) Comma separated list of summaries to save in output-folder. Default: scalars, histograms, images, audio, compressedHistograms
```
