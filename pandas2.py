# Working with Json

jsonExample={
  "userId": 1001,
  "name": "Sarah Williams",
  "email": "sarah.w@example.com",
  "address": {
    "street": "456 Oak Avenue",
    "city": "Portland",
    "state": "OR",
    "zipCode": "97201",
    "country": "USA"
  },
  "phone": {
    "home": "+1-503-555-0123",
    "mobile": "+1-503-555-0124"
  },
  "preferences": {
    "newsletter": "true",
    "notifications": "false",
    "language": "en"
  }
}

jsonExample
# Getting labelled column in jsonn
jsonExample["address"]
# getting data from json as we pass dictionary into data frame
json_Data=pd.DataFrame({'street': ['456 Oak Avenue'],
 'city': ['Portland'],
 'state': ['OR'],
 'zipCode': ['97201'],
 'country': ['USA']})
json_Data
# problem while fetching json directly into dataframe

# json_Data=pd.DataFrame(jsonExample["phone"]) THIS WILL GIVE ERROR BECAUSE KEYS AND CORRESPONDIG VALUES ARE NOT ARRANGED IN []

# solution
json_Data=pd.DataFrame([jsonExample["address"]])
# json_Data=pd.DataFrame({'home': ['+1-503-555-0123'], 'mobile': ['+1-503-555-0124']}) ABOVE CODE AND THIS IS EXACTLY SAME NOW DUE TO EXTRA [] ABOVE
json_Data
# converting json data frame into csv
json_Data.to_csv("jsonDataAddressCSV.csv")
# Now reading the same converted csv again
pd.read_csv("jsonDataAddressCSV.csv")
# Reading can also be done by assigning into another variable and then reading it
readCSVconvertedJson=pd.read_csv("jsonDataAddressCSV.csv")
readCSVconvertedJson
# now converting the same csv to json 
# and for this: we have to use a variable which will store csv converted json file
readCSVconvertedJson.to_json("jsonDataAddressJSON.json")

# and now to read this json converted  csv: we will need variable
pd.read_json("jsonDataAddressJSON.json")
# Reading this json can also be done by
readThatJson=pd.read_json("jsonDataAddressJSON.json")
readThatJson
