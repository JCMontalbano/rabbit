import pandas as pd
import numpy as np
from scipy import stats

DF=pd.read_csv('sample.csv')

t_meanratelist=[]
t_maxratelist=[]
t_meancomplist=[]
t_maxcomplist=[]

for recommendation in set(DF.recommendation_id):
	subDF=DF[DF['recommendation_id']==recommendation]
	meanrate=subDF.hourly_rate.mean()
	maxrate=subDF.hourly_rate.max()
	meancomp=subDF.num_completed_tasks.mean()
	maxcomp=subDF.num_completed_tasks.max()	
	for tasker in subDF.iterrows():
		t_meanrate=(tasker[1][4])/meanrate
		t_maxrate=(tasker[1][4])/maxrate
		t_meanratelist.append(t_meanrate)
		t_maxratelist.append(t_maxrate)
		t_meancomp=(tasker[1][5])/meancomp
		t_maxcomp=(tasker[1][5])/maxcomp
		t_meancomplist.append(t_meancomp)
		t_maxcomplist.append(t_maxcomp)


#confirm that the correct length of DF column was produced:
len(t_meanratelist)/len(DF) #>>>1.0
#confirm that the proportionality is working:
np.mean(t_meanratelist)
np.mean(t_meancomplist)

#include the vectorized lists into the original DF as columns:
DF['meanrate']=t_meanratelist
DF['maxrate']=t_maxratelist
DF['meancomp']=t_meancomplist
DF['maxcomp']=t_maxcomplist



For relevant data:
stats.pointbiserialr(x,y)

#I should present this as a series of bar graphs
#https://matplotlib.org/gallery/units/bar_unit_demo.html
stats.pointbiserialr(DF.meanrate,DF.hired)
stats.pointbiserialr(DF.maxrate,DF.hired)
stats.pointbiserialr(DF.meancomp,DF.hired)
stats.pointbiserialr(DF.maxcomp,DF.hired)

x=[1,1,1,0,0,0]
y=[1,1,1,0,0,0]


list(set(DF.category))
moveDF=DF[DF['category']=='Moving Help']
mountDF=DF[DF['category']=='Mounting']
furnitureDF=DF[DF['category']=='Furniture Assembly']

stats.pointbiserialr(moveDF.meanrate,moveDF.hired)
stats.pointbiserialr(moveDF.maxrate,moveDF.hired)
stats.pointbiserialr(moveDF.meancomp,moveDF.hired)
stats.pointbiserialr(moveDF.maxcomp,moveDF.hired)

stats.pointbiserialr(mountDF.meanrate,mountDF.hired)
stats.pointbiserialr(mountDF.maxrate,mountDF.hired)
stats.pointbiserialr(mountDF.meancomp,mountDF.hired)
stats.pointbiserialr(mountDF.maxcomp,mountDF.hired)

stats.pointbiserialr(furnitureDF.meanrate,furnitureDF.hired)
stats.pointbiserialr(furnitureDF.maxrate,furnitureDF.hired)
stats.pointbiserialr(furnitureDF.meancomp,furnitureDF.hired)
stats.pointbiserialr(furnitureDF.maxcomp,furnitureDF.hired)


	len(subDF)
