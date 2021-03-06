#Somu    30th March 2018 
#Project 2018: Programming and Scripting

# This program is divided into 3 sections 
# Section 1 : Using Iris Data, create the python-pandas data frame,
# Section 2 : Describe the Iris flower data stored in the dataframes
# Section 3 : Plot the graphs using the matplot library
# This program makes use of panda's, numpy and matplot libraries

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

#SECTION  1  -- Starts here
#Read the data from iris.csv file 
#Function to create python list for each flower with attributes
#Create Dataframes for each flower using the python List
#Setosa flower: data frame - dfsetosa  :: List name - Lsetosa
#virginica flower: data frame - dfvirginica  :: List name - Lvirginica
#versicolor flower: data frame - dfversi  :: List name - Lversi 

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
dfsetosa = pd.DataFrame(Lsetosa, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])
dfvirginica = pd.DataFrame(Lvirginica, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])
dfversi = pd.DataFrame(Lversi, columns = ['Petal Length','Petal Width','Sepal Length', 'Sepal Width'])

#SECTION  1  -- Ends here


#SECTION  2  -- Starts here
#Using the dataframe describe function, display the below for each flower
#Count of the records/data for each flower
#Mean/Average of the flower attributes - Sepal wideth and legth; Petal width and length
#Standard diviation of the each attribute
#Minumum and maximum value of the each attribute

print (("\n"),"Setosa Flower :: Data Summary")
print (("\n"),dfsetosa.describe(include='all'))
print (("\n"),"Virginica Flower :: Data Summary")
print (("\n"),dfvirginica.describe(include='all'))
print (("\n"),"Versicolor Flower :: Data Summary")
print (("\n"),dfversi.describe(include='all'))

#SECTION  2  -- Ends here


#SECTION  3  -- Starts here
#Create a dataflower called dflower, which holds the data of all the 3 flowers
#Create columsn in the dataframe (dflower) for each flower attribute
#PL-Setosa -> represents the petal length of Setosa
#....
#PW-Veri -> represents the petal width of versicolor
#Use numpy provide linespace for the X and Y axis
#Use matplot to plot the grapsh (Scatter and Box)
#PLOT and SHOW  Graphs using matplot library
#Blue colour in the Graph represents Setosa flower
#Red colout in the Graph represents Virginica flower
#Green colour in the Graph represents Versicolor flower

#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
dflower = pd.DataFrame()
#Function to create Petal dataframes
def creatpetaldataframe():
        dflower['PL-Setosa'] = pd.DataFrame(dfsetosa["Petal Length"])
        #dflower = dflower.rename(columns={'Petal Length': 'PL-Setosa'})
        dflower['PW-Setosa'] = pd.DataFrame(dfsetosa["Petal Width"])
        dflower['PL-Viginica'] = pd.DataFrame(dfvirginica["Petal Length"])
        dflower['PW-Viginica'] = pd.DataFrame(dfvirginica["Petal Width"])
        dflower['PL-Versi'] = pd.DataFrame(dfversi["Petal Length"])
        dflower['PW-Versi'] = pd.DataFrame(dfversi["Petal Width"])

#Function to create Sepal dataframes
#Data frame to hold the values of Petal legnth and width's of Iris Setosa, Virginica and Versicolor
def creatsepaldataframe():
        dflower['SL-Setosa'] = pd.DataFrame(dfsetosa["Sepal Length"])
        #dflower = dflower.rename(columns={'Sepal Length': 'SL-Setosa'})
        dflower['SW-Setosa'] = pd.DataFrame(dfsetosa["Sepal Width"])
        dflower['SL-Viginica'] = pd.DataFrame(dfvirginica["Sepal Length"])
        dflower['SW-Viginica'] = pd.DataFrame(dfvirginica["Sepal Width"])
        dflower['SL-Versi'] = pd.DataFrame(dfversi["Sepal Length"])
        dflower['SW-Versi'] = pd.DataFrame(dfversi["Sepal Width"])

#create dataframe and also, Box plot for petel length and Width
creatpetaldataframe()
color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
bp = dflower.boxplot()
bp.set_ylabel("Measurement in cm")
bp.set_xlabel("PL - Petal Length   PW - Petal Width")
plt.title("Petal Length and Width Graph")
plt.show()

#clear the dataframe and create sepal dataframe. Box plot for Sepal length and Width
dflower = pd.DataFrame()
creatsepaldataframe()
color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
bp = dflower.boxplot()
bp.set_ylabel("Measurement in cm")
bp.set_xlabel("SL - Sepal Length   SW - Sepal Width")
plt.title("Sepal Length and Width Graph")
plt.show()

#clear the dataframe and create sepal and Petal dataframes. 
dflower = pd.DataFrame()
creatpetaldataframe()
creatsepaldataframe()

#Calculate area of the Sepal flower and store the value as a column in the data frame
dflower['Setosa-SA'] = dflower['SL-Setosa'] * dflower['SW-Setosa']
dflower['Virginica-SA']= dflower['SL-Viginica'] * dflower['SW-Viginica']
dflower['Versi-SA']= dflower['SL-Versi'] * dflower['SW-Versi']

#Calculate area of the Petal flower and store the value as a column in the data frame
dflower['Setosa-PA'] = dflower['PL-Setosa'] * dflower['PW-Setosa']
dflower['Virginica-PA']= dflower['PL-Viginica'] * dflower['PW-Viginica']
dflower['Versi-PA']= dflower['PL-Versi'] * dflower['PW-Versi']

#Function to plot the graph's
def graph (name):
        dflower['x'] = np.linspace(0,10, 50)
        # Graph using matplot library :: Petal Length Vs Petal Width
        ax = dflower.plot(kind=name, x='PW-Setosa',y='PL-Setosa', color="b", label="Setosa")
        dflower.plot(kind=name, x='PW-Viginica',y='PL-Viginica', color="r", label="Virginica", ax=ax)
        dflower.plot(kind=name, x='PW-Versi',y='PL-Versi', color="g", label="Versicolor", ax=ax)
        ax.set_xlabel("Petal Width")
        ax.set_ylabel("Petal Length")
        plt.title("Petal Width Vs Petal Length Graph")
        plt.show()


        dflower['x'] = np.linspace(0,16, 50)
        dflower['xp'] = np.linspace(0,30, 50)
        #Graph using matplot library :: Sepal Length Vs Sepal Width
        ax = dflower.plot(kind=name, y='SL-Setosa',x='SW-Setosa', color="b", label="Setosa")
        dflower.plot(kind=name, x='SW-Viginica',y='SL-Viginica', color="r", label="Virginica", ax=ax)
        dflower.plot(kind=name, x='SW-Versi',y='SL-Versi', color="g", label="Versicolor", ax=ax)

        #Set the X and Y axis names and show the Graph
        ax.set_xlabel("Sepal Width")
        ax.set_ylabel("Sepal Length")
        plt.title("Sepal Width Vs Sepal Length Graph")
        plt.show()
        
        ax = dflower.plot(kind=name, y='Setosa-SA',x='x', color="b", label="Setosa")
        dflower.plot(kind=name, x='x',y='Virginica-SA', color="r", label="Virginica", ax=ax)
        dflower.plot(kind=name, x='x',y='Versi-SA', color="g", label="Versicolor", ax=ax)

        #Set the X and Y and show the Graph
        ax.set_xlabel("Data")
        ax.set_ylabel("Sepal Area")
        plt.title("Sepal Area Graph")
        plt.show()

        # Graph to plot the Petal Area
        ax = dflower.plot(kind=name, y='Setosa-PA',x='xp', color="b", label="Setosa")
        dflower.plot(kind=name, x='xp',y='Virginica-PA', color="r", label="Virginica", ax=ax)
        dflower.plot(kind=name, x='xp',y='Versi-PA', color="g", label="Versicolor", ax=ax)

        #Set the X and Y and show the Graph
        ax.set_xlabel("Data")
        ax.set_ylabel("Petal Area")
        plt.title("Petal Area Graph")
        plt.show()

#Call function graph and pass plot parameter 
#Displays Scatter and histogram graphs
graph ("scatter")
graph ("box")
graph("hist")

#SECTION  3  -- Ends here

 