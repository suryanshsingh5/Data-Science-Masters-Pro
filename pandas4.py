titanic.describe() # tells each and every detail
titanic.tail(), titanic.head()
titanic.T # transpose
# apply: used after dataframe's specific column and followed by a function
def changeName(name):
    return 'This is : ' + name

titanic['NameOfThePassenger'].apply(changeName)
titanic.count() #count all the things
titanic.isnull()
titanic.dtypes # gives type of each and every data

# to append a row

row1234 = titanic[0:1] # row creaeted, but it is a series
titanic._append(row1234) # that series appended easily into the existing dataframe  AND THIS METHOD IS DEPRICATED
pd.concat([titanic, pd.DataFrame(row1234)]) # that series needs to convert into dataframe
titanic=pd.concat([titanic, pd.DataFrame(row1234)]) # this method will not make the permanent change so we have to reassign it for permanent change
titanic
# delete the duplicate values
titanic.drop_duplicates(inplace= True) # this method will not make the permanent change so we have to add inplace= True
titanic
# to reset the index again from zero
titanic.reset_index(drop=True, inplace=True) # this method will not make the permanent change so we have to add inplace= True
# drop=True is used so that the backed up column for the index reset reference got deleted
titanic