#Somu    30th March 2018
#Project 2018: Programming and Scripting
#Iris Data set: Iris Setosa anlaysis
#Technical Reference : https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm

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
print (s.plot(x='Petal Length',y='Sepal Length'))
plt.show()

#df = pd.read_csv("data/iris.csv")
#print (df)

#print (Lattributes)

# Define the variables. counter for each flower in the iris dataset
# Gname = variable to hold flower names
# Gp/slen = Variables to hold the petal and sepal length and width

# counter1, counter2,counter3 = 1,1,1
# Gplen,Gpwid,Gslen,Gswid = 0.0,0.0, 0.0,0.0
# Gname,Gnamei,Gnameo = '','',''

# # Function to print the name, petel length, petal width, Sepal length and sepal width
# def printiris(line):
#         Gplen = float(str(line.split(',')[0]))
#         Gpwid = float(str(line.split(',')[1]))
#         Gslen = float(str(line.split(',')[2]))
#         Gswid = float(str(line.split(',')[3]))
#         print ("{:04.2f}  {:04.2f}  {:04.2f}  {:04.2f}".format (Gplen,Gpwid,Gslen,Gswid))

# # Store all the distinct flower names 
# flowers = set()
# with open("data/iris.csv") as f:
#         for line in f:
#             Gname   = str(line.split(',')[4]).rstrip()
#             flowers.add(Gname)

# #Read the file and print the petel /Sepal details for each flower 
# with open("data/iris.csv") as f:
#         for line in f:
#             Gnameo   = str(line.split(',')[4]).rstrip()
#             if Gnameo == 'Iris-virginica':
#                 if counter1 == 1: 
#                     print ("{:^20}".format(Gnameo))
#                     printiris(line)
#                     counter1 += 1
#                 else:
#                    printiris(line)
#             if Gnameo == 'Iris-versicolor':
#                 if counter2 == 1: 
#                     print ("{:^20}".format(Gnameo))
#                     printiris(line)
#                     counter2 += 1
#                 else:
#                    printiris(line)
#             if Gnameo == 'Iris-setosa':
#                 if counter3 == 1: 
#                     print ("{:^20}".format(Gnameo))
#                     printiris(line)
#                     counter3 += 1
#                 else:
#                    printiris(line)                    
