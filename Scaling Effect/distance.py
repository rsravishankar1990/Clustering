#!/usr/bin/env/python

import pandas as pd
import numpy as np
import pylab as pl

'''Module checks the effect of units on measuring distances'''
def dist_compute(point1,point2):
	#Compute the euclidean distance between the two points provided
	dim = len(point1)
	distance = 0
	
	for i in range(dim):
		distance += (point1[i] - point2[i])**2 
		
	distance = distance ** 0.5
	return distance

def calc_stat(datadict):
	#Calculate the mean and the standard deviation of the keys
	keydict = {}
	keys = datadict.keys()
	for key in keys:
		#Compute the stats
		#Append the stats to the keydict dictionary
		#Return the keydict dictionary
		if key == 'Name':
			pass
		else:
			avg = np.average(datadict[key])
			std = np.std(datadict[key])
			keydict[key] = [avg,std]
			
	return keydict
	

def scale_effect():
	datadict = { 'Ravi' : (12, 95),
				 'Shankar' : (1075, 93),
				 'Raja' : (13,115)}
	graph_dist = []
	graph_scale = []
	for scale in range(1,100):
		graph_scale.append(scale)
		
		#Create scaled points
		Ravi = [datadict['Ravi'][0], datadict['Ravi'][1] * scale]
		Raja = [datadict['Raja'][0], datadict['Raja'][1] * scale]
		Shankar = [datadict['Shankar'][0], datadict['Shankar'][1] * scale]
		
		distance1 = dist_compute(Ravi,Raja)
		distance2 = dist_compute(Ravi, Shankar)
		
		dist_diff = distance1 - distance2
		
		graph_dist.append(dist_diff)

	print ("Reached the end")
	pl.plot(graph_scale, graph_dist)
	pl.xlabel('Scale')
	pl.ylabel('|Ravi,Raja| - |Ravi, Shankar|')
	pl.show()


if __name__ == "__main__":
	scale_effect()
