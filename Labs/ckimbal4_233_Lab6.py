#CS 112 _ 233 Python lab 6
#Author Craig Kimball
#Date 10/5/2021 11:30AM 


#filter-score is a function that takes in a 2d list of students containing their id, age, and score
#filter score iterates through each student to determine which has the score above 90
#upon finding a score over 90 the function ends returning the current student
def filter_score(data_set):
    for student in data_set:
        if(student[2] > 90):
            return student
    return null

print(filter_score([[20,"Clyde",55],[23,"Thea",62],[18,"Otto",93]]))