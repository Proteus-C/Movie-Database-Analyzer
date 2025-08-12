import json
import pandas as pd
import numpy as np

json_file_path = 'Database.json'


# With Pandas
with open(json_file_path, 'r') as f:
    data = json.load(f)
#df = pd.json_normalize(data)
#print(df.head())

df = pd.read_json(json_file_path)
print(df.head())
#rating = df.groupby('rating')
#rating.mean()




'''
movieList = {
    "movies": [
        {
            "title":"The Godfather",
            "rating":9.2,
            "year":"1972"
        },
        {
            "title":"the Matrix",
            "rating":8.7,
            "year":"1999"        
        },
        {
            "title":"Interstellar",
            "rating":8.7,
            "year":"2014"        
        },
        {
            "title":"The Dark Knight",
            "rating":9.1,
            "year":"2008"        
        },
        {
            "title":"Transformers",
            "rating":7.1,
            "year":"2007"        
        },
        {
            "title":"Kung Fu Panda",
            "rating":7.8,
            "year":"2008"        
        },
        {
            "title":"Sin City",
            "rating":8.0,
            "year":"2005"        
        },
        {
            "title":"CoCo",
            "rating":8.4,
            "year":"2017"        
        },
        {
            "title":"Dragonball Evolution",
            "rating":2.5,
            "year":"2009"        
        },
        {
            "title":"Green Lantern",
            "rating":5.5,
            "year":"2011"        
        }
    ]
}


with open("Database.json", 'w') as fp:
    json.dump(movieList, fp, indent = 4)

with open("Database.json") as f:
    print(f.read())
'''
