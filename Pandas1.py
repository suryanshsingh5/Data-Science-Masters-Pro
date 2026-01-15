# Pandas

import pandas as pd
#titanic csv files raw link code & CONVERTING CSV INTO READBLE TABLE
pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv") # can be printed in this type also 
# now saving this data into a variable
titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
# CONVERTING READABLE TABLE INTO CSV AGAIN
titanic.to_csv("titanicData.csv")
# now CONVERTING READABLE TABLE INTO CSV AGAIN but using a separator which will separate the data
titanic.to_csv("titanicDataSemicolon.csv", sep=";")

# type of dataframe
type(titanic)
print(titanic)
# labelled coloumns
titanic["Name"]

# checking the index of the dataframe
titanic.index
# manipulating the index number of dataframe
titanic.index= [ "Row " + str(i) for i in range(1,892)]
titanic
# checking the index of the dataframe
titanic.index
# creating a dataframe in pondas

# passing list in dataframe
df1= pd.DataFrame([1,2,3])
df1 # wihtout column index or row index = index
df3= pd.DataFrame([1,2,3], index =["one", "two", "three"])
df3 # with rows index
df2= pd.DataFrame([1,2,3], columns =["one"])
df2 # with column index


# passing dictionary in dataframe~~ it takes it as columns
df4 = pd.DataFrame({'one' : [1,2],'two': [3,4] })
df4
df5 = pd.DataFrame({'one' : [1,2],'two': [3,4] }, columns =["hello1", "hello2"], index=["hellooooooo1", "hello00002"]) # we have to give both row and colum in case of dictionary otherwise it won't print more
df5 # but values will be not printed becase name of column should me match with dict column name and here it is not
df6 = pd.DataFrame({'one' : [1,2],'two': [3,4] }, columns =["two", "one"], index=["hellooooooo1", "hello00002"]) # we have to give both row and colum in case of dictionary otherwise it won't print more
df6 # but values will be not printed becase name of column should me match with dict column name and here it is but it will interchange the place of them
# Playing with header
import pandas as pd
# here the first row will not be treated as header
titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv", header = None)
titanic