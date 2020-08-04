#UTF-8

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#Set backend
matplotlib.use("Agg")

#Import k_10 clusters
mean_ndre = np.loadtxt(fname='/home/jbk/projects/climate/tropics/sentinel-2/clustering/k_10/results/seeds.out.manaus_ndre_2016-2019.10.final.unstd')
print("File imported")

#Create cluster list and step list
clusters = list(range(1,11))
steps = list(range(1,26))

#Create subplots
fig,a = plt.subplots(2,5,sharex=True,sharey=True)
a[0, 0].plot(steps,mean_ndre[0])
a[0, 0].set_title('Cluster_{}'.format(clusters[0]))
a[0, 1].plot(steps,mean_ndre[1])
a[0, 1].set_title('Cluster_{}'.format(clusters[1])) 
a[0, 2].plot(steps,mean_ndre[2])
a[0, 2].set_title('Cluster_{}'.format(clusters[2]))
a[0, 3].plot(steps,mean_ndre[3])
a[0, 3].set_title('Cluster_{}'.format(clusters[3]))
a[0, 4].plot(steps,mean_ndre[4])
a[0, 4].set_title('Cluster_{}'.format(clusters[4]))
a[1, 0].plot(steps,mean_ndre[5])
a[1, 0].set_title('Cluster_{}'.format(clusters[5]))
a[1, 1].plot(steps,mean_ndre[6])
a[1, 1].set_title('Cluster_{}'.format(clusters[6]))
a[1, 2].plot(steps,mean_ndre[7])
a[1, 2].set_title('Cluster_{}'.format(clusters[7]))
a[1, 3].plot(steps,mean_ndre[8])
a[1, 3].set_title('Cluster_{}'.format(clusters[8]))
a[1, 4].plot(steps,mean_ndre[9])
a[1, 4].set_title('Cluster_{}'.format(clusters[9]))
print("Plots created")

#Save figure
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 6)
plt.savefig('/home/6ru/python_scripts/Initial_Plots.png')
print("Figure saved to python scripts")
