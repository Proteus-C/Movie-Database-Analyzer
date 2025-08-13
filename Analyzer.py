import json
import pandas as pd

def addMovie(fileData, name, rating, year):
    movieName = name
    movieRating = rating
    movieRelease = year

    movieList = {"title":movieName, "rating":movieRating, "year":movieRelease}

    with open("Database.json", 'a') as fp:
        json.dump(movieList, fp)
        fp.write("\n")


exit = False
while exit != True:
    #Gets the file path    
    json_file_path = 'Database.json'
    # Puts data into database with Pandas
    with open(json_file_path, 'r') as fp:
        data = pd.read_json(fp, lines = True)

    choice = input("Do you want to compare movie [ratings] before/after 2008 or [add] a movie to the list or exit?\n")
    if choice == "add":
        addMovieName = input("Enter a movie name: ")
        addMovieRating = float(input("Enter the movie's rating: "))
        addMovieYear= int(input("Enter the movie's release year: "))
        addMovie(data, addMovieName, addMovieRating, addMovieYear)
        print("done!")
    elif choice == "ratings":
        #Uses Boolean Indexing with Pandas
        after08 = data['year'] > 2008
        before08 = data['year'] <= 2008

        ratingsAfter = data.loc[after08, 'rating']
        ratingsBefore = data.loc[before08, 'rating']
        rating1 = ratingsAfter.mean()
        rating2 = ratingsBefore.mean()

        print(f"Average rating after 2008: {rating1}")
        print(f"Average rating before 2008: {rating2}")  

    elif choice == "exit":
        exit = True
    else:
        print("Enter either: [ratings] or [add] or [exit]")
