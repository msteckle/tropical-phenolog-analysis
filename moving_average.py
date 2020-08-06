import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
import datetime as dt
import matplotlib

# Set backend
matplotlib.use("Agg")

# Open S2 csv
ndre = []
with open("/home/6ru/data/S2_10Random_Samples.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		ndre.append(row)

dates = []
with open("/home/6ru/python_scripts/all_dt.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		dates.append(row)	

# Adjust S2 list and covert to numpy
ndre = np.array(ndre)
ndre = np.where(ndre=='', np.nan, ndre) # Set nan
ndre = np.delete(ndre,0,0) # Delete first row
ndre = np.delete(ndre,0,1) # Delete first obj in each row
ndre = ndre.astype(float) # Convert strings to floats
ndre = ndre.flatten()
print(len(ndre))

# Create x-axis values and set as datetime
dt_range = np.array(dates)
dt_range = dt_range.flatten()
dt_range = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dt_range]

x = mdates.date2num(dt_range)

y = ndre
y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = np.array(y[0:100]), np.array(y[100:200]), np.array(y[200:300]), np.array(y[300:400]), np.array(y[400:500]), np.array(y[500:600]), np.array(y[600:700]), np.array(y[700:800]), np.array(y[800:900]), np.array(y[900:1000])
print(len(y1), len(y2), len(y3), len(y4), len(y5), len(y6), len(y7),len(y8), len(y9), len(y10))

pc = 10	
# Find outliers and set as np.nan
pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9, pl10 = np.nanpercentile(y1,pc), np.nanpercentile(y2,pc), np.nanpercentile(y3,pc), np.nanpercentile(y4,pc), np.nanpercentile(y5,pc), np.nanpercentile(y6,pc), np.nanpercentile(y7,pc), np.nanpercentile(y8,pc), np.nanpercentile(y9,pc), np.nanpercentile(y10,pc)

o1, o2, o3, o4, o5, o6, o7, o8, o9, o10 = (y1 < pl1),(y2 < pl2),(y3 < pl3),(y4 < pl4),(y5 < pl5),(y6 < pl6),(y7 < pl7),(y8 < pl8),(y9 < pl9),(y10 < pl10)

y1[o1], y2[o2], y3[o3], y4[o4], y5[o5], y6[o6], y7[o7], y8[o8], y9[o9], y10[o10] = np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan

idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9, idx10 = np.isfinite(x) & np.isfinite(y1), np.isfinite(x) & np.isfinite(y2), np.isfinite(x) & np.isfinite(y3), np.isfinite(x) & np.isfinite(y4), np.isfinite(x) & np.isfinite(y5), np.isfinite(x) & np.isfinite(y6), np.isfinite(x) & np.isfinite(y7), np.isfinite(x) & np.isfinite(y8), np.isfinite(x) & np.isfinite(y9), np.isfinite(x) & np.isfinite(y10)

w=11
p=3

# Sav-Gol moving window polynomial
yhat1, yhat2, yhat3, yhat4, yhat5, yhat6, yhat7, yhat8, yhat9, yhat10 = savgol_filter(y1[idx1], w, p), savgol_filter(y2[idx2], w, p), savgol_filter(y3[idx3], w, p), savgol_filter(y4[idx4], w, p), savgol_filter(y5[idx5], w, p), savgol_filter(y6[idx6], w, p), savgol_filter(y7[idx7], w, p), savgol_filter(y8[idx8], w, p), savgol_filter(y9[idx9], w, p), savgol_filter(y10[idx10], w, p)

# Plot original and new lines	
fig,a = plt.subplots(2,5,sharex=True, sharey=True)
a[0,0].plot(dt_range, y1, '--')
a[0,0].plot(x[idx1], yhat1, 'g-')

a[0,1].plot(dt_range, y2, '--')
a[0,1].plot(x[idx2], yhat2, 'g-')

a[0,2].plot(dt_range, y3, '--')
a[0,2].plot(x[idx3], yhat3, 'g-')

a[0,3].plot(dt_range, y4, '--')
a[0,3].plot(x[idx4], yhat4, 'g-')

a[0,4].plot(dt_range, y5, '--')
a[0,4].plot(x[idx5], yhat5, 'g-')

a[1,0].plot(dt_range, y6, '--')
a[1,0].plot(x[idx6], yhat6, 'g-')

a[1,1].plot(dt_range, y7, '--')
a[1,1].plot(x[idx7], yhat7, 'g-')

a[1,2].plot(dt_range, y8, '--')
a[1,2].plot(x[idx8], yhat8, 'g-')

a[1,3].plot(dt_range, y9, '--')
a[1,3].plot(x[idx9], yhat9, 'g-')

a[1,4].plot(dt_range, y10, '--')
a[1,4].plot(x[idx10], yhat10, 'g-')

fig = plt.gcf()
fig.set_size_inches(14,6)
fig.autofmt_xdate()
plt.savefig('/home/6ru/python_scripts/moving_average.png')
print('Figure saved.')
