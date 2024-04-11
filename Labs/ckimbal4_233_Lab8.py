#CS 112 _ 233 Python lab 8
#Author Craig Kimball
#Date 10/19/2021 11:30AM 
def recommender(rating) :
# Some operations to produce a recommendation based on the rating
# do not change this complex time-consuming function.
    print("The time-consuming function is called")
    if rating == 1:
        return "You may NOT like it."
    if rating == 2:
        return "You may like it."
    return "A must-watch movie!"


def process_movie_list(movie_list):
    movieDict = {}
    recomendationDict = {}

    
    for movie in movie_list:
        if movie[2] not in recomendationDict:
            recomendation = movie[2]
            recomendationDict[movie[2]] = recommender(recomendation)
        else:
            recomendation = recomendationDict[movie[2]]
            
        movieDict[movie[0]] = [movie[1],movie[2],recomendationDict[movie[2]]]
        
    return movieDict
        


movie_list = [["Titanic", 1997, 1],["Citation", 2020, 3],['Rocky', 1976, 2],['Baahubali', 2015, 3]]

print(process_movie_list(movie_list))