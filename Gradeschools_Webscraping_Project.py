# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:28:27 2020

@author: Stanley
"""



# imports
import numpy as np
from numpy import mean
from numpy import std
from matplotlib import pyplot
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Cleaning Data

# For Rating, Test Scores, College Readiness, S-T ratio
def Int(arr_series):
    nan_idx = pd.isna(arr_series)
    arr_series[nan_idx] = -1
    return arr_series.astype("int")

# Average teacher salaries
def Int2(arr_series):
    for i in range(len(arr_series)):
        if type(arr_series.iloc[i]) != float:
            arr_series.iloc[i] = (arr_series.iloc[i]).replace(",","")
    nan_idx = pd.isna(arr_series)
    arr_series[nan_idx] = -1
    
    return arr_series.astype("int")

# For Demographics
def percent(arr_series):    
    nan_idx = pd.isna(arr_series)
    arr_series[nan_idx] = -1

    lpercent = (arr_series == "<1%")
    arr_series[lpercent] = 1
    
    str_idx = (1 == (1 - (nan_idx + lpercent)))
    for i in range(len(arr_series)):
        if str_idx[i]:
            arr_series[i] = int((arr_series[i])[:-1])
    
    return arr_series
    

    


#data
df = pd.read_csv('gs_data.csv')

cg_readiness = df['College Readiness']
st_ratio_list = df['S-T ratio']

hispanic = percent(df["Hispanic"])
asian = percent(df["Asian"])
white = percent(df["White"])
black = percent(df["Black"])
avg_teacher_salaries = Int2(df['Average teacher salary'])    
    
df2 = df
df2.to_csv('gs_data2.csv')

x = Int(cg_readiness)
y = Int(st_ratio_list)

indices = []
for i in range(len(x)):
    if x[i] == -1:
        indices.append(i)
    elif y[i] == -1:
        indices.append(i)
    else:
        continue
m = []
n = []

for i in range(len(x)):
    if i in indices:
        continue
    m.append(x[i])
    n.append(y[i])
    


data1 = np.array(m)
data2 = np.array(n)


# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
print('correlation:\n', np.corrcoef(m,n))
# plot
pyplot.plot(data1, data2,'o')
slope, b = np.polyfit(m,n,1)
slope_m=[]
for i in range(len(m)):
    slope_m.append(slope*m[i])
pyplot.plot(m,slope_m +b)

pyplot.show()