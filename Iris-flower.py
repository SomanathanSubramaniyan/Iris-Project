#Somu    30th March 2018
#Project 2018: Programming and Scripting
#Iris Data set: Iris Setosa anlaysis
#Technical Reference : 
# https://stackoverflow.com/
# http://pandas.pydata.org/pandas-docs/version
# https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm
# https://matplotlib.org/api/pyplot_api.html
# https://matplotlib.org/examples/index.html
# https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Gname,Gnamei,Gnameo = '','',''
Lsetosa,Lvirginica,Lversi =[],[],[]

# Function to create list for petel length, petal width, Sepal length and sepal width for each flower type
def fstore(line):
        Gplen = line.split(',')[0]
        Gpwid = line.split(',')[1]
        Gslen = line.split(',')[2]
        Gswid = line.split(',')[3]
        Gnameo  = str(line.split(',')[4]).rstrip()
        if Gnameo == 'Iris-setosa':
                Lsetosa.append ([float(Gplen),float(Gpwid),float(Gslen),float(Gswid)])
        elif Gnameo == 'Iris-versicolor':
                Lversi.append ([float(Gplen),float(Gpwid),float(Gslen),float(Gswid)])
        elif Gnameo == 'Iris-virginica':
                Lvirginica.append ([float(Gplen),float(Gpwid),float(Gslen),float(Gswid)])

# Read the iris Data file and store the Setosa attributes value by calling function fstore
with open("data/iris.csv") as f:
        for line in f:
                fstore(line)

# Feed each flower measurement into Pandas dataframe           
dfsetosa = pd.DataFrame(Lsetosa, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])
dfvirginica = pd.DataFrame(Lvirginica, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])
dfversi = pd.DataFrame(Lversi, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])

# mean, minimum, maximum and standard diviation
print (dfsetosa.describe(include='all'))
print (dfvirginica.describe(include='all'))
print (dfversi.describe(include='all'))

data = {'Iris-setosa':dfsetosa,
        'Iris-versicolor':dfversi,
        'Iris-virginica': dfvirginica}

p = pd.Panel (data)

#print(dfsetosa)
x = range(1,50)
print (x)
print (dfsetosa)
#plt.scatter(x[:0],dfsetosa.loc["0":"49","Petal Length"])
#plt.scatter(x[:0],dfvirginica.loc["0":"49","Petal Length"])
#plt.show()

#print (p)
#p.plot(kind='scatter')


# #Plot the graph petal length vs Sepal length
# dfsetosa.plot(x='Petal Length',y='Sepal Length',kind='scatter')
# # show the graph
# plt.show()

# #Plot the graph petal length vs Sepal length
# dfsetosa.plot(x='Petal Width',y='Sepal Width',kind='scatter')
# plt.show()

# # show the graph
# dfsetosa.plot(kind='box')
# plt.show()