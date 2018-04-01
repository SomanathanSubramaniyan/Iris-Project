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



#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
dfpetal = pd.DataFrame(dfsetosa["Petal Length"])
dfpetal = dfpetal.rename(columns={'Petal Length': 'PL-Setosa'})
dfpetal['PW-Setosa'] = pd.DataFrame(dfsetosa["Petal Width"])
dfpetal['PL-Viginica'] = pd.DataFrame(dfvirginica["Petal Length"])
dfpetal['PW-Viginica'] = pd.DataFrame(dfvirginica["Petal Width"])
dfpetal['PL-Versi'] = pd.DataFrame(dfversi["Petal Length"])
dfpetal['PW-Versi'] = pd.DataFrame(dfversi["Petal Width"])
dfpetal['x'] = np.linspace(0,10, 50)

# Graph for the three different flowers :: Petal Length Vs Petal Width
ax = dfpetal.plot(kind="scatter", y='PL-Setosa',x='PW-Setosa', color="b", label="Setosa")
dfpetal.plot(kind="scatter", x='PW-Viginica',y='PL-Viginica', color="r", label="Virginica", ax=ax)
dfpetal.plot(kind="scatter", x='PW-Versi',y='PL-Versi', color="g", label="Versicolor", ax=ax)

ax.set_xlabel("Petal Width")
ax.set_ylabel("Petal Length")
plt.show()


#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
dfpetal = pd.DataFrame(dfsetosa["Sepal Length"])
dfpetal = dfpetal.rename(columns={'Sepal Length': 'SL-Setosa'})
dfpetal['SW-Setosa'] = pd.DataFrame(dfsetosa["Sepal Width"])
dfpetal['SL-Viginica'] = pd.DataFrame(dfvirginica["Sepal Length"])
dfpetal['SW-Viginica'] = pd.DataFrame(dfvirginica["Sepal Width"])
dfpetal['SL-Versi'] = pd.DataFrame(dfversi["Sepal Length"])
dfpetal['SW-Versi'] = pd.DataFrame(dfversi["Sepal Width"])
dfpetal['x'] = np.linspace(0,10, 50)


# Graph for the three different flowers :: Petal Length Vs Petal Width
ax = dfpetal.plot(kind="scatter", y='SL-Setosa',x='SW-Setosa', color="b", label="Setosa")
dfpetal.plot(kind="scatter", x='SW-Viginica',y='SL-Viginica', color="r", label="Virginica", ax=ax)
dfpetal.plot(kind="scatter", x='SW-Versi',y='SL-Versi', color="g", label="Versicolor", ax=ax)

ax.set_xlabel("Sepal Width")
ax.set_ylabel("Sepal Length")
plt.show()


