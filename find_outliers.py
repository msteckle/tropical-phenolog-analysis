import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
import datetime as dt
import matplotlib
import time

# Set backend
matplotlib.use("Agg")

# Open S2 csv
results = []
with open("/home/6ru/data/S2_10Random_Samples.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		results.append(row)

# Create numpy array
array = np.array(results) # Create
array = np.where(array=='', np.nan, array) # Set nan
array = np.delete(array,0,0) # Delete first row
array = np.delete(array,0,1) # Delete first obj in each row
array = array.astype(float) # Convert strings to ints
#[[1, 2, 3, 4, ... 25]]

sorted_data = np.sort(array)
print(sorted_data)

limits = [] #[[lower,upper][lower,upper]]
for obj in array:
	q1 = np.nanpercentile(obj, 10)
	q3 = np.nanpercentile(obj, 90)
	iqr = q3 - q1
	number = iqr/2
	lower_bound = q1 - (number * q1)
	upper_bound = q3 + (number * q3)
	limits.append([lower_bound, upper_bound])
print(limits)

outlier_list = []
baby_list = []
i = 0
for lim in limits:
	j = 0
	for obj in array[i]:
		if obj < lim[0]:
			baby_list.append(j)
		j = j + 1
	outlier_list.append(baby_list)
	baby_list = []
	i = i + 1
print(outlier_list)

# Save as csv
with open("/home/6ru/python_scripts/outlier_list.csv", "w", newline="") as f:
	writer = csv.writer(f, delimiter=',', quotechar='|')
	writer.writerows(outlier_list)
print("CSV saved.")
