# Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

d=d1.get('simple_key')
print(d)

d=d2['k1']['k2']
print(d)
d=d3['k1'][0]['nest_key'][1]
print(d)

"""Below are the two lists convert it into the dictionary"""
#use dict
#use zip

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d=dict(zip(keys,values))
print(d)
#---------------------------------------------
"""Access the value of key ‘history’"""

#nested dict

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

s=sampleDict['class']['student']['marks']['history']
print(s)

#-------------------------------------------------------------



