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
        addMovieRating = input("Enter the movie's rating: ")
        addMovieYear= input("Enter the movie's release year: ")
        addMovie(data, addMovieName, addMovieRating, addMovieYear)
        print("done!")
    elif choice == "ratings":
        df = data['year'].astype(int)
        dfR = data['rating']

        #Set the values from each year into the variables
        count1, count2, after08, before08 = 0, 0, 0, 0
        for i in range(0, len(df)):
            if df[i] > 2008:
                after08 += dfR[i]
                count1 += 1
            elif df[i] <= 2008:
                before08 += dfR[i]
                count2 += 1

        #Calculates the rating
        rating1 = after08 / count1
        rating2 = before08 / count2

        #Prints results
        print(f"Average rating after 2008: {rating1}")
        print(f"Average rating before 2008: {rating2}")

    elif choice == "exit":
        exit = True
    else:
        print("Enter either: [ratings] or [add] or [exit]")
