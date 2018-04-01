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
# https://www.datascience.com/learn-data-science/tutorials/creating-data-visualizations-matplotlib-data-science-python

#Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the variables
Gname,Gnamei,Gnameo = '','',''
Lsetosa,Lvirginica,Lversi =[],[],[]

# fstore function: Creates list for petel length, petal width, Sepal length and sepal width for each flower type
# 3 different list are created
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

# Read the iris Data file from location data/iris.csv
# calls function "fstore" to create the list
with open("data/iris.csv") as f:
        for line in f:
                fstore(line)

# create dataframe for each flow from the list
# Setosa flower : data frame - dfsetosa  :: List name - Lsetosa
# virginica flower : data frame - dfvirginica  :: List name - Lvirginica
# versicolor flower : data frame - dfversi  :: List name - Lversi        
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



#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
dflower = pd.DataFrame()
dflower['PL-Setosa'] = pd.DataFrame(dfsetosa["Petal Length"])
#dflower = dflower.rename(columns={'Petal Length': 'PL-Setosa'})
dflower['PW-Setosa'] = pd.DataFrame(dfsetosa["Petal Width"])
dflower['PL-Viginica'] = pd.DataFrame(dfvirginica["Petal Length"])
dflower['PW-Viginica'] = pd.DataFrame(dfvirginica["Petal Width"])
dflower['PL-Versi'] = pd.DataFrame(dfversi["Petal Length"])
dflower['PW-Versi'] = pd.DataFrame(dfversi["Petal Width"])
dflower['x'] = np.linspace(0,10, 50)

# Graph :: Petal Length Vs Petal Width
ax = dflower.plot(kind="scatter", y='PL-Setosa',x='PW-Setosa', color="b", label="Setosa")
dflower.plot(kind="scatter", x='PW-Viginica',y='PL-Viginica', color="r", label="Virginica", ax=ax)
dflower.plot(kind="scatter", x='PW-Versi',y='PL-Versi', color="g", label="Versicolor", ax=ax)

ax.set_xlabel("Petal Width")
ax.set_ylabel("Petal Length")
plt.show()


#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
dflower['SL-Setosa'] = pd.DataFrame(dfsetosa["Sepal Length"])
#dflower = dflower.rename(columns={'Sepal Length': 'SL-Setosa'})
dflower['SW-Setosa'] = pd.DataFrame(dfsetosa["Sepal Width"])
dflower['SL-Viginica'] = pd.DataFrame(dfvirginica["Sepal Length"])
dflower['SW-Viginica'] = pd.DataFrame(dfvirginica["Sepal Width"])
dflower['SL-Versi'] = pd.DataFrame(dfversi["Sepal Length"])
dflower['SW-Versi'] = pd.DataFrame(dfversi["Sepal Width"])
dflower['x'] = np.linspace(0,16, 50)
dflower['xp'] = np.linspace(0,30, 50)

# Graph  :: Sepal Length Vs Sepal Width
ax = dflower.plot(kind="scatter", y='SL-Setosa',x='SW-Setosa', color="b", label="Setosa")
dflower.plot(kind="scatter", x='SW-Viginica',y='SL-Viginica', color="r", label="Virginica", ax=ax)
dflower.plot(kind="scatter", x='SW-Versi',y='SL-Versi', color="g", label="Versicolor", ax=ax)

#Set the X and Y and show the Graph
ax.set_xlabel("Sepal Width")
ax.set_ylabel("Sepal Length")
plt.show()

#Calculate area of the Sepal
dflower['Setosa-SA'] = dflower['SL-Setosa'] * dflower['SW-Setosa']
dflower['Virginica-SA']= dflower['SL-Viginica'] * dflower['SW-Viginica']
dflower['Versi-SA']= dflower['SL-Versi'] * dflower['SW-Versi']


# Graph to plot the Sepal Area
ax = dflower.plot(kind="scatter", y='Setosa-SA',x='x', color="b", label="Setosa")
dflower.plot(kind="scatter", x='x',y='Virginica-SA', color="r", label="Virginica", ax=ax)
dflower.plot(kind="scatter", x='x',y='Versi-SA', color="g", label="Versicolor", ax=ax)

#Set the X and Y and show the Graph
ax.set_xlabel("Data")
ax.set_ylabel("Sepal Area")
plt.show()


#Calculate area of the Petal
dflower['Setosa-PA'] = dflower['PL-Setosa'] * dflower['PW-Setosa']
dflower['Virginica-PA']= dflower['PL-Viginica'] * dflower['PW-Viginica']
dflower['Versi-PA']= dflower['PL-Versi'] * dflower['PW-Versi']

# Graph to plot the Petal Area
ax = dflower.plot(kind="scatter", y='Setosa-PA',x='xp', color="b", label="Setosa")
dflower.plot(kind="scatter", x='xp',y='Virginica-PA', color="r", label="Virginica", ax=ax)
dflower.plot(kind="scatter", x='xp',y='Versi-PA', color="g", label="Versicolor", ax=ax)

#Set the X and Y and show the Graph
ax.set_xlabel("Data")
ax.set_ylabel("Petal Area")
plt.show()
print (dflower['Virginica-PA'])