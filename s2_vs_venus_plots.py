import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
import datetime as dt


# Set backend
import matplotlib
matplotlib.use("Agg")

# Open venus csv with venus sample values
results = []
with open("/home/6ru/data/Venus_10Random_Samples.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		results.append(row)

# Open s2 csv with venus sample values
results1 = []
with open("/home/6ru/data/S2_10Random_Samples.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		results1.append(row)

# convert to numpy array
array = np.array(results)
array1 = np.array(results1)

# Replace '' with np.nan
array = np.where(array=='', np.nan, array)
array1 = np.where(array1=='', np.nan, array1)

# Delete first column and first row
array = np.delete(array, 0, 0) # Delete first list
array = np.delete(array, 0, 1) # Delete first obj in each list
array1 = np.delete(array1, 0, 0)
array1 = np.delete(array1, 0, 1)

# Convert strings to integers
array = array.astype(float)
print(array)
array1 = array1.astype(float)
print(array1)

# Create x-axis ticks
date_range = np.array(["2018_02_06", "2018_02_08", "2018_03_02",
		"2018_06_10", "2018_07_08", "2018_07_14", "2018_07_20",
		"2018_08_01",
		"2018_08_05", "2018_08_09", "2018_08_15", "2018_08_17",
		"2018_08_21",
		"2018_08_25", "2018_10_08", "2018_10_16", "2018_10_18",
		"2018_10_24",
		"2018_10_26", "2018_11_01", "2018_11_13", "2018_11_15"])

date_range1 = np.array(["2018_01_15", "2018_01_30", "2018_02_14",
		"2018_03_01",
		"2018_03_16", "2018_03_31", "2018_04_15", "2018_04_30",
		"2018_05_15",
		"2018_05_30", "2018_06_14", "2018_06_29", "2018_07_14",
		"2018_07_29",
		"2018_08_13", "2018_08_28", "2018_09_12", "2018_09_27",
		"2018_10_12",
		"2018_10_27", "2018_11_11", "2018_11_26", "2018_12_11",
		"2018_12_26", "2018_12_31"])

# Create subplots
date_range = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in date_range]
date_range1 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in date_range1]

fig,a = plt.subplots(2,5,sharex=True, sharey=True)
a[0,0].plot(date_range,array[0], marker='.')
a[0,0].plot(date_range1,array1[0], marker='.')
a[0,1].plot(date_range,array[1], marker='.')
a[0,1].plot(date_range1,array1[1], marker='.')
a[0,2].plot(date_range,array[2], marker='.')
a[0,2].plot(date_range1,array1[2], marker='.')
a[0,3].plot(date_range,array[3], marker='.')
a[0,3].plot(date_range1,array1[3], marker='.')
a[0,4].plot(date_range,array[4], marker='.')
a[0,4].plot(date_range1,array1[4], marker='.')
a[1,0].plot(date_range,array[5], marker='.')
a[1,0].plot(date_range1,array1[5], marker='.')
a[1,1].plot(date_range,array[6], marker='.')
a[1,1].plot(date_range1,array1[6], marker='.')
a[1,2].plot(date_range,array[7], marker='.')
a[1,2].plot(date_range1,array1[7], marker='.')
a[1,3].plot(date_range,array[8], marker='.')
a[1,3].plot(date_range1,array1[8], marker='.')
a[1,4].plot(date_range,array[9], marker='.')
a[1,4].plot(date_range1,array1[9], marker='.')
print("Plots created.")

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=73))
fig = plt.gcf()
fig.set_size_inches(12,7)
fig.autofmt_xdate()
plt.savefig('/home/6ru/python_scripts/Combined_10Sample_Plots.png')
print("Figure saved.")
