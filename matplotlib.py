# importing the essential libraries earlier
import math as ma
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline 
# Render all Matplotlib plots inline inside the notebook cell output, instead of opening them in a separate window.
import seaborn as sns 
# it was made using pandas and matplotlib together so that it can plot graphs on dataframe (2-d data)
# Importing the titanic dataset
titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
titanic.head()
# plotting now method 2: PLOT AND THEN DISPLAY
plt.plot(titanic['Age'], color='red') # we can use color as well it is optional
plt.show()
# using seaborn and 
#reading that titanic dataset
sns.load_dataset('titanic')
# Line Plot

x=[1,2,3,4,53]
y=[2,3,33,43,22]
plt.xlabel("X values")
plt.ylabel("Y values")

# without any color
plt.title("Line Plot")
plt.plot((x,y))
plt.show()

# with color
plt.title("Line Plot")
plt.plot(x,y,color='green')
plt.show()
x,y
# Bar Plot

plt.xlabel("X values")
plt.ylabel("Y values")


# without color
plt.title("Bar Plot")
plt.bar(x,y)
plt.grid(True) # enables the grid in the graph
plt.plot(x,y,color='green')# line plot embeded, you can also merge the line plot and the bar plot if you want[]
plt.show()


# with color
plt.title("Bar Plot")
plt.bar(x,y, edgecolor='green', color='red')
plt.grid(True)
plt.plot(x,y,color='green') # line plot embeded, you can also merge the line plot and the bar plot if you want[]
plt.show()


# Histogran
data= np.random.random(100)

# bins(pipes plotted) difference
plt.title("Histogram with 20 bins")
plt.hist(data,bins=20, color='black',edgecolor='green')
plt.show()
plt.title("Histogram with 10 bins")
plt.hist(data,bins=10, color='black',edgecolor='green')
plt.show()
# withourt bins
plt.title("Histogram without bins entry")
plt.hist(data,color='black',edgecolor='green')
plt.show()
# using seaborn
plt.title("Histogram Using Seaborn")
data1=np.random.randn(100)
sns.histplot(data, edgecolor='black', color='green',kde=True) #kde: kernel density essesity meter: joins the middle nomralizes the graph
plt.show()




# Scatter Plot
plt.title('Scatter plot using matplotlib')
plt.scatter(titanic['Age'], titanic['Fare'], color='green', edgecolor='blue')
plt.show()

#using seaborn
plt.title("Using Seaborn: it maps all the numeric data automatically")
sns.pairplot(titanic)
plt.show()
#using seaborn
plt.title("Using Seaborn: mapping by column slicing")
sns.pairplot(titanic.iloc[::100])
plt.show()
# subplot: ROW, COLUMN, POSITION
data=np.random.randn(100)
# histogram
plt.subplot(2,2,2)
plt.title("Histogram")
plt.hist(data,color='black',edgecolor='green')
plt.show()

# using seaborn
plt.subplot(2,2,4)
plt.title("Histogram Using Seaborn")
sns.histplot(data, edgecolor='black', color='green',kde=True) #kde: kernel density essesity meter: joins the middle nomralizes the graph
plt.show()
plt.savefig("MyHist.png") # to save the graph

# Important concept
x = np.linspace(0,10,100) 

y1 = np.sin(x)
y2= np.cos(x)

plt.title('Plot Title')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.plot(x, y1, label='Sin') # label is optional & REFLECTED AT LEGEND
plt.plot(x, y2, label='Cos')

plt.legend(loc=2)  # Show legend & LOCATION DENOTES PLACE TO PUT IT

plt.grid(True)  # Show grid lines

plt.tight_layout()  # Adjust layout

plt.xlim(0, 5)  # Set x-axis limits
plt.ylim(-1,1)  # Set y-axis limits

plt.xticks(np.arange(0, 10, 0.5))  # Set custom tick locations on x-axis
plt.yticks([-1, 0, 1], ['Min', 'Mid', 'Max'])  # Set custom tick labels on y-axis

plt.show()