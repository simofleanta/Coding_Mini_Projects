
"""Access info in the nested json below, the data is covid data from Code for Romania 2020""" 
#import json
#open file
#learn get a property from a nested object
import json

with open('datelazi.json', 'r') as file:
    s=json.load(file)

print(s)

print(s['charts']['dailyStats']['contains'])
print(s['currentDayStats'])
print(s['currentDayStats']['numberCured'])
print(s['currentDayStats']['numberInfected'])
print(s['currentDayStats']['numberDeceased'])
print(s['currentDayStats']['percentageOfMen'])
print(s['currentDayStats']['percentageOfWomen'])
print(s['currentDayStats']['distributionByAge'])
print(s['currentDayStats']['countyInfectionsNumbers'])



























































"""print("country: ",python_obj["name"])

print(json_obj[1])#the 1st or fourth character
print(json_obj[4])

print(python_obj)
print(python_obj['country'])
print(python_obj['name'])
print(python_obj['age'])
#so convert to python obj in order to easily operate through 
#to convert to py obj use loads

Convert python object to json data
#using dumps to convert to json data 
python_object={"Country":"Belgium","Name":"Arthur","Age":40}
json_data=json.dumps(python_object)
print(json_data)"""