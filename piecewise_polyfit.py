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
print(results)

# Open outiers csv
outliers = []
with open("/home/6ru/python_scripts/outlier_list.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar="|")
	for row in reader:
		outliers.append(row)
print(outliers)

outliers = [list( map(int,i) ) for i in outliers]
print(outliers)

# Adjust S2 list and covert to numpy
ndre = np.array(results)
ndre = np.where(ndre=='', np.nan, ndre) # Set nan
ndre = np.delete(ndre,0,0) # Delete first row
ndre = np.delete(ndre,0,1) # Delete first obj in each row
ndre = ndre.astype(float) # Convert strings to floats
print(ndre)

# Create x-axis values and set as datetime
dt_list = np.array(["2018_01_15", "2018_01_30", "2018_02_14",
		"2018_03_01",
		"2018_03_16", "2018_03_31", "2018_04_15", "2018_04_30",
		"2018_05_15",
		"2018_05_30", "2018_06_14", "2018_06_29", "2018_07_14",
		"2018_07_29",
		"2018_08_13", "2018_08_28", "2018_09_12", "2018_09_27",
		"2018_10_12",
		"2018_10_27", "2018_11_11", "2018_11_26", "2018_12_11",
		"2018_12_26", "2018_12_31"])

date_range = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_list]

# Create 3D array
new_arr = []
for val in ndre:
	for i in range(0,24):
		new_arr.append([dt_list[i], val[i]])
#print(new_arr)

f = lambda new_arr, n=25: [new_arr[i:i+n] for i in range(0, len(new_arr), n)] #Split 2D into 3D list
new_arr = f(new_arr)
#print(new_arr)


# Set up for polyfit
# Select correct outlier index [[**][..][..]] etc

print("Outlier index list for sample 1: " + str(outliers[0]))

# Select outlier value from new_arr [[[.., ..][**, **][.., ..]][etc]]
def select_outliers(outlier_sel):
	for i in range(0,10):
		an_arr = new_arr[i] #Select 1st, 2nd, etc list of lists from new_arr
		outlier_val = an_arr[outlier_sel[0]] # Select first index pos 
		return outlier_val[1] # Select value

o1_1 = select_outliers(outliers[0])
o2_1 = select_outliers(outliers[1])
o3_1 = select_outliers(outliers[2])
o4_1 = select_outliers(outliers[3])
o5_1 = select_outliers(outliers[4])
o6_1 = select_outliers(outliers[5])
o7_1 = select_outliers(outliers[6])
o8_1 = select_outliers(outliers[7])
o9_1 = select_outliers(outliers[8])
o10_1 = select_outliers(outliers[9])
print("Outlier value for sample 1: " + str(o1_1))

#[[2,5][5][1,20][...][10th]]
def get_values(outlier_list):
	tmp = outlier_list[0] # Select first outlier index for sample (x)
	# Create new array of relevent polynomial values centered around tmp
	#b1, b2, b3, a1, a2, a3 = tmp - 1, tmp - 2, tmp - 3, tmp + 1, tmp +	2, tmp + 3
	cur_out = tmp
	if cur_out == 0:
		a1, a2, a3 = cur_out + 1, cur_out + 2, cur_out + 3
		poly_list = list([new_arr[0][a1], new_arr[0][a2],
				new_arr[0][a3]])
	elif cur_out == 1:
		b1, a1, a2, a3 = cur_out - 1, cur_out + 1, cur_out + 2, cur_out + 3
		poly_list = list([new_arr[0][b1], new_arr[0][a1], new_arr[0][a2],
				new_arr[0][a3]])
	elif cur_out == 2:
		b1, b2, a1, a2, a3 = cur_out - 1, cur_out - 2, cur_out + 1, cur_out + 2, cur_out + 3
		poly_list = list([new_arr[0][b2], new_arr[0][b1],
			new_arr[0][a1], new_arr[0][a2], new_arr[0][a3]])
	elif cur_out == 24:
		b1, b2, b3 = cur_out - 1, cur_out - 2, cur_out - 3
		poly_list = list([new_arr[0][b3], new_arr[0][b2], new_arr[0][b1]])
	elif cur_out == 23:
		b1, b2, b3, a1 = cur_out - 1, cur_out - 2, cur_out - 3, cur_out + 1
		poly_list = list([new_arr[0][b3], new_arr[0][b2], new_arr[0][b1], 
				new_arr[0][a1]])
	elif cur_out == 22:
		b1, b2, b3, a1, a2 = cur_out - 1, cur_out - 2, cur_out - 3, cur_out + 1, cur_out + 2
		poly_list = list([new_arr[0][b3], new_arr[0][b2], new_arr[0][b1], 
				new_arr[0][a1], new_arr[0][a2]])
	else:
		b1, b2, b3, a1, a2, a3 = cur_out - 1, cur_out - 2, cur_out - 3, cur_out + 1, cur_out + 2, cur_out + 3
		poly_list = list([new_arr[0][b3], new_arr[0][b2], new_arr[0][b1], 
				new_arr[0][a1], new_arr[0][a2], new_arr[0][a3]])
	return poly_list

poly1_1 = np.array(get_values(outliers[0]))
#poly2_1 = np.array(get_values(outliers[1]))
poly3_1 = np.array(get_values(outliers[2]))
poly4_1 = np.array(get_values(outliers[3]))
poly5_1 = np.array(get_values(outliers[4]))
poly6_1 = np.array(get_values(outliers[5]))
poly7_1 = np.array(get_values(outliers[6]))
poly8_1 = np.array(get_values(outliers[7]))
poly9_1 = np.array(get_values(outliers[8]))
poly10_1 = np.array(get_values(outliers[9]))
print("List for polyfit: " + str(poly1_1))

# Create appropriate date ranges
dt_rg1 = np.array(poly1_1[:, 0], dtype=str)
#dt_rg2 = np.array(poly2_1[:, 0], dtype=str)
dt_rg3 = np.array(poly3_1[:, 0], dtype=str)
dt_rg4 = np.array(poly4_1[:, 0], dtype=str)
dt_rg5 = np.array(poly5_1[:, 0], dtype=str)
dt_rg6 = np.array(poly6_1[:, 0], dtype=str)
dt_rg7 = np.array(poly7_1[:, 0], dtype=str)
dt_rg8 = np.array(poly8_1[:, 0], dtype=str)
dt_rg9 = np.array(poly9_1[:, 0], dtype=str)
dt_rg10 = np.array(poly10_1[:, 0], dtype=str)
print("Date range for sample 1: " + str(dt_rg1))

dt_rg1 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg1]
#dt_rg2 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg2]
dt_rg3 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg3]
dt_rg4 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg4]
dt_rg5 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg5]
dt_rg6 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg6]
dt_rg7 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg7]
dt_rg8 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg8]
dt_rg9 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg9]
dt_rg10 = [dt.datetime.strptime(d, '%Y_%m_%d').date() for d in dt_rg10]

# Create value list for polyfit
poly1_1 = np.array(poly1_1[:, 1], dtype=float)
#poly2_1 = np.array(poly2_1[:, 1], dtype=float)
poly3_1 = np.array(poly3_1[:, 1], dtype=float)
poly4_1 = np.array(poly4_1[:, 1], dtype=float)
poly5_1 = np.array(poly5_1[:, 1], dtype=float)
poly6_1 = np.array(poly6_1[:, 1], dtype=float)
poly7_1 = np.array(poly7_1[:, 1], dtype=float)
poly8_1 = np.array(poly8_1[:, 1], dtype=float)
poly9_1 = np.array(poly9_1[:, 1], dtype=float)
poly10_1 = np.array(poly10_1[:, 1], dtype=float)
print("Values for polyfit: " + str(poly1_1))

# Generate polynomials
def make_poly(an_array, a_date):
	x = mdates.date2num(a_date)
	y = an_array
	idx = np.isfinite(x) & np.isfinite(y) # Ignore Nan
	return idx

idx1 = make_poly(poly1_1, dt_rg1) 
#idx2 = make_poly(poly2_1, dt_rg2)
idx3 = make_poly(poly3_1, dt_rg3)
idx4 = make_poly(poly4_1, dt_rg4)
idx5 = make_poly(poly5_1, dt_rg5)
idx6 = make_poly(poly6_1, dt_rg6)
idx7 = make_poly(poly7_1, dt_rg7)
idx8 = make_poly(poly8_1, dt_rg8)
idx9 = make_poly(poly9_1, dt_rg9)
idx10 = make_poly(poly10_1, dt_rg10)

def set_nulls(an_idx, a_date, an_array):
	x = mdates.date2num(a_date)
	y = an_array
	z4 = np.polyfit(x[an_idx], y[an_idx], 2)
	p4 = np.poly1d(z4)
	return p4

p41 = set_nulls(idx1, dt_rg1, poly1_1)
#p42 = set_nulls(idx2, dt_rg2, poly2_1)
p43 = set_nulls(idx3, dt_rg3, poly3_1)
p44 = set_nulls(idx4, dt_rg4, poly4_1)
p45 = set_nulls(idx5, dt_rg5, poly5_1)
p46 = set_nulls(idx6, dt_rg6, poly6_1)
p47 = set_nulls(idx7, dt_rg7, poly7_1)
p48 = set_nulls(idx8, dt_rg8, poly8_1)
p49 = set_nulls(idx9, dt_rg9, poly9_1)
p410 = set_nulls(idx10, dt_rg10, poly10_1)

def set_xx(a_date):
	x = mdates.date2num(a_date)
	xx = np.linspace(x.min(), x.max(), 100)
	return xx

xx1 = set_xx(dt_rg1)
#xx2 = set_xx(dt_rg2)
xx3 = set_xx(dt_rg3)
xx4 = set_xx(dt_rg4)
xx5 = set_xx(dt_rg5)
xx6 = set_xx(dt_rg6)
xx7 = set_xx(dt_rg7)
xx8 = set_xx(dt_rg8)
xx9 = set_xx(dt_rg9)
xx10 = set_xx(dt_rg10)

def set_dd(an_xx):
	dd = mdates.num2date(an_xx)
	return dd

dd1 = set_dd(xx1) 
#dd2 = set_dd(xx2)
dd3 = set_dd(xx3)
dd4 = set_dd(xx4)
dd5 = set_dd(xx5)
dd6 = set_dd(xx6)
dd7 = set_dd(xx7)
dd8 = set_dd(xx8)
dd9 = set_dd(xx9)
dd10 = set_dd(xx10)

# Create subplots
fig,a = plt.subplots(2,5,sharex=True, sharey=True)
a[0,0].plot(date_range, ndre[0], marker='.') # Create full graph
a[0,0].plot(dd1, p41(xx1), '-g') # Create polyfit graph

a[0,1].plot(date_range,ndre[1], marker='.')
#a[0,1].plot(dd2, p42(xx2), '-g')

a[0,2].plot(date_range,ndre[2], marker='.')
a[0,2].plot(dd3, p43(xx3), '-g')

a[0,3].plot(date_range,ndre[3], marker='.')
a[0,3].plot(dd4, p44(xx4), '-g')

a[0,4].plot(date_range,ndre[4], marker='.')
a[0,4].plot(dd5, p45(xx5), '-g')

a[1,0].plot(date_range,ndre[5], marker='.')
a[1,0].plot(dd6, p46(xx6), '-g')

a[1,1].plot(date_range,ndre[6], marker='.')
#a[1,1].plot(dd7, p47(xx7), '-g')

a[1,2].plot(date_range,ndre[7], marker='.')
a[1,2].plot(dd8, p48(xx8), '-g')

a[1,3].plot(date_range,ndre[8], marker='.')
a[1,3].plot(dd9, p49(xx9), '-g')

a[1,4].plot(date_range,ndre[9], marker='.')
a[1,4].plot(dd10, p410(xx10), '-g')

print("Plots created.")
polyline = np.array(p49(xx9))
print("Polyline: " + str(polyline))

# Set properties and export
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=73))
fig = plt.gcf()
fig.set_size_inches(12,7)
fig.autofmt_xdate()
plt.savefig('/home/6ru/python_scripts/S2_polynomials.png')
print("Figure saved.")


