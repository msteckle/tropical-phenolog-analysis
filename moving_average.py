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

# Adjust S2 list and covert to numpy
ndre = np.array(ndre)
ndre = np.where(ndre=='', np.nan, ndre) # Set nan
ndre = np.delete(ndre,0,0) # Delete first row
ndre = np.delete(ndre,0,1) # Delete first obj in each row
ndre = ndre.astype(float) # Convert strings to floats

# Create x-axis values and set as datetime
dt_list = np.array(["2018_01_15", "2018_01_30", "2018_02_14",
		"2018_03_01", "2018_03_16", "2018_03_31", 
		"2018_04_15", "2018_04_30", "2018_05_15",
		"2018_05_30", "2018_06_14", "2018_06_29", 
		"2018_07_14", "2018_07_29", "2018_08_13", 
		"2018_08_28", "2018_09_12", "2018_09_27",
		"2018_10_12", "2018_10_27", "2018_11_11", 
		"2018_11_26", "2018_12_11", "2018_12_26", 
		"2018_12_31"])

dt_range = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_list]


x = mdates.date2num(dt_range)
y = ndre[0]
z = np.where(y > .425, y, np.nan)
idx = np.isfinite(x) & np.isfinite(z)
print(y)
print(z)

#def smooth(val, box_pts):
#	box = np.ones(box_pts)/box_pts
#	y_smooth = np.convolve(val, box, mode='same')
#	return y_smooth

yhat = savgol_filter(z[idx], 5, 3)
		   
plt.plot(x, y, '--')
#plt.plot(x[idx], smooth(z[idx], 2), 'r-')
plt.plot(x[idx], yhat, 'g-')

fig = plt.gcf()
fig.autofmt_xdate()
plt.savefig('/home/6ru/python_scripts/moving_average.png')
print('Figure saved.')
