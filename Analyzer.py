import json
import pandas as pd

json_file_path = 'Database.json'


# With Pandas
with open(json_file_path, 'r') as f:
    data = json.load(f)
df = pd.json_normalize(data['movies'])
#print(df.head())

df['year'] = df['year'].astype(int)
after08 = df[df['year'] > 2008]
before08 = df[df['year'] <= 2008]

rating1 = after08['rating'].mean()
rating2 = before08['rating'].mean()

print(f"Average rating after 2008: {rating1}")
print(f"Average rating before 2008: {rating2}")


'''
#If I want to implement a way to add onto the movies list in the future

with open("Database.json", 'a') as fp:
    json.dump(movieList, fp, indent = 4)

with open("Database.json") as f:
    print(f.read())
'''
