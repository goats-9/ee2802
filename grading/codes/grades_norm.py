import numpy as np
import pandas as pd
from math import isnan
data = pd.read_excel('marks.xlsx')      #reading input
df1 = data.loc[:,"Total" or "Marks"]    #storing marks column
x = np.array(df1)
#Population parameters
mu = df1.mean()
sig = df1.var()
#Get Z-scores
z = (x - mu)/np.sqrt(sig)
N = x.size                              #Size of Data
#x = x.reshape(N,1)                      #Converting to column
#y = np.zeros((N,1))                     #column of Assigned clusters 
#X = np.hstack((x,y))                    #stacking data and cluster
#k = 8                                   #No.of Clusters(Grades)
#
df2 = data.loc[:,"Grade"]
grades = []
s = ""
#Attach grades
for i in range(N):
    if (z[i] >= 3): s = 'A+'
    elif (z[i] >= 2): s = 'A'
    elif (z[i] >= 1): s = 'A-'
    elif (z[i] >= 0): s = 'B'
    elif (z[i] >= -1): s = 'B-'
    elif (z[i] >= -2): s = 'C'
    elif (z[i] >= -3): s = 'D'
    else: s = 'F'
    grades.append(s)

data['Grade'] = grades
data.to_excel('grades_norm.xlsx',index = False)  #writing to file
data.to_csv('grades_norm.csv',index=False)
