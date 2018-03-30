#Somu    30th March 2018
#Project 2018: Programming and Scripting
#Iris Data set: Iris Setosa anlaysis
#Technical Reference : 
# https://stackoverflow.com/
# http://pandas.pydata.org/pandas-docs/version
# https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Gname,Gnamei,Gnameo = '','',''
Lattributes,Lvalue =[],[]

# Function to create list for petel length, petal width, Sepal length and sepal width
def fstore(line):
        Gplen = line.split(',')[0]
        Gpwid = line.split(',')[1]
        Gslen = line.split(',')[2]
        Gswid = line.split(',')[3]
        Lvalue.append ([float(Gplen),float(Gpwid),float(Gslen),float(Gswid)])

# Read the iris Data file and store the Setosa attributes value by calling function fstore
with open("data/iris.csv") as f:
        for line in f:
            Gnameo   = str(line.split(',')[4]).rstrip()
            if Gnameo == 'Iris-setosa':
                    fstore(line)

# Feed the data into Pandas dataframe           
s = pd.DataFrame(Lvalue, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])

# mean, minimum, maximum and standard diviation
print (s.describe(include='all'))

#Plot the graph petal length vs Sepal length
s.plot(x='Petal Length',y='Sepal Length',kind='scatter')
# show the graph
plt.show()

#Plot the graph petal length vs Sepal length
s.plot(x='Petal Width',y='Sepal Width',kind='scatter')
plt.show()

# show the graph
s.plot(kind='box')
plt.show()