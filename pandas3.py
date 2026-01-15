# printing our dataframe titanic
titanic
# adding a new column in data frame
titanic['NewColumn']=list(range(0,892))
# here i have added header again because it was removed at above
titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
titanic
# adding two columns
titanic['Name and Mr are added columns'] = 'Mr '+ titanic['Name']
titanic
# adding one column but on condition
titanic['Age>5']=titanic['Age']>5

# what ever is written on the left: will be displayed
# what ever is written on the right: is logic
titanic
# print the first 100 entries
titanic.head(100)
# print the last 10 entries
titanic.tail(10)
# number of rows and columns
titanic.shape
del (titanic['Age>5'])
# deleting a column using pop
titanic.pop('Sex')

titanic.rename(columns={"Name":"NameOfThePassenger"}, inplace = True)
# if we do only this then it will not change the main data table so we have two options to permanent change
# 1. reassign this value into titanic again
# 2. make the inplace= True

titanic
# row level, it is as same as list
titanic[0:100:10]

# to do so on column level, we have a ILOC function
# first [] for row, and second for column
titanic.iloc[0:100:10][0:6:2]

# if we have to slice normally at row but only one column, we have LOC function
titanic.loc[0:100:10]['Parch']

# fill the indexes in list form TO ACCESS SPECIFIC ROW AND COLUMN
titanic.loc[[0 ,1,11,3,40], ['NameOfThePassenger','Parch']]