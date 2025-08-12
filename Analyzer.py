import json

movieList = {
    "movies": [
        {
            "title":"The Godfather",
            "rating":8.7,
            "year":"1972"
        },
        {
            "title":"the Matrix",
            "rating":8.7,
            "year":"1999"        
        },
        {
            "title":"Interstellar",
            "rating":8.6,
            "year":"2014"        
        }
    ]
}


with open("Database.json", 'w') as fp:
    json.dump(movieList, fp, indent = 4)

with open("Database.json") as f:
    print(f.read())
