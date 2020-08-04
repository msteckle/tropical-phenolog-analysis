import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime as dt
import matplotlib.dates as mdates

matplotlib.use("Agg")

array = np.array([np.nan, 0.4093, 0.556966, np.nan, 0.553736,
	   	0.555929, 0.552511, 0.551647, 0.467446, 0.53358,
	  	0.575322, 0.58483, np.nan, 0.574833, 0.569527,
		0.557512, 0.555366, 0.549166, 0.542689, 0.547096,
	   	0.533845, 0.568141, 0.486156, 0.425396, np.nan])
	
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

x = mdates.date2num(date_range)
y = array
idx = np.isfinite(x) & np.isfinite(y)

z = np.polyfit(x[idx], y[idx], 3)
p = np.poly1d(z)
p30 = np.poly1d(np.polyfit(x[idx], y[idx], 50))

dt = mdates.date2num(date_range)	
xp = np.linspace(dt.min(), dt.max(), 100)

plt.plot(xp, p(xp), '-')
plt.plot(x, y, '.')
plt.plot(xp, p30(xp), '--')

fig = plt.gcf()
fig.autofmt_xdate()
plt.savefig('/home/6ru/python_scripts/single_polyfit.png')
print("Figure saved.")
