import csv


attr = (
	[snr, stat.extrema, stat.rms[0],stat.count, stat.median, stat.stddev, stat.var]
	)
for item in attr:
    worksheet.write_string  (row, col,     item              )

