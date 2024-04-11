#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 6
# Date: 11/1/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------

# .get(), .append() and/or .insert().     allowed
# round(), min(),    range()    and    len() allwoed


#the function returns a float of a 5% weighed score for reading assignments
def wreadings(grades, drop = 0): 
    #selection sort implemented using temporary variables 
    for i in range(len(grades)):
        for j in range(i+1, len(grades)):
            if(grades[i] > grades[j]):
                temp = grades[i]
                grades[i] = grades[j]
                grades[j] = temp
    
    #removes the lowest grades
    grades = grades[drop:]
    
    grade_sum = 0
    for grade in grades:
        grade_sum += grade
    
    return round((grade_sum / len(grades)) * 10 * 0.05,2)

# print(wreadings([10,9,8,9]))

#the function returns float of a 10% weighted score for lab assignments
def wlabs(grades, drop = 0):
    #selection sort implemented using temporary variables 
    for i in range(len(grades)):
        for j in range(i+1, len(grades)):
            if(grades[i] > grades[j]):
                temp = grades[i]
                grades[i] = grades[j]
                grades[j] = temp
                
    #removes the lowest grades
    grades = grades[drop:]
    
    grade_sum = 0
    for grade in grades:
        grade_sum+=grade
        
    return round((grade_sum / len(grades)) * 10 * 0.1,2)

# print(wlabs([5,8,0],2))

#function returns a float of a 40% weighted score for the lab assignments
def wPAs(grades, drop = 0):
    #selection sort implemented using temporary variables 
    for i in range(len(grades)):
        for j in range(i+1, len(grades)):
            if(grades[i] > grades[j]):
                temp = grades[i]
                grades[i] = grades[j]
                grades[j] = temp
                
    #removes the lowest grades
    grades = grades[drop:]
    
    grade_sum = 0
    for grade in grades:
        grade_sum+=grade
        
    return round((grade_sum / len(grades)) * 2 * 0.4,2)

# print(wPAs([40,10,35,5],1))

#function returns a list of floats with a 10% midterms and 25% final exam weighted grade
def wexams(mt1 = 100, mt2 = 100, fe = 250):
    return [mt1 * 0.1, mt2 * 0.1, fe * 0.1]


# The function returns a tuple that contains 2 parameters, the final_score (int)
# which is the result of round(total_score) and the final letter grade (string)
# based on this scheme:
def finalGrade(reading, labs, PAs, mt1=100, mt2=100, fe=250):
    [[1,2,3,4,5], 6, 0]
    [[1,2,3,4],0]
    
    #ensures that all parameters have a index of 1 with the default drop value
    reading.append(0)
    labs.append(0)
    PAs.append(0)

    #calculates the exam scores based on their weighted grades    
    exam_total = 0
    exams = wexams(mt1, mt2, fe)
    for exam in exams:
        exam_total +=exam
    
    #adds up total score
    total_score = wreadings(reading[0],reading[1]) + wlabs(labs[0],labs[1]) + wPAs(PAs[0],PAs[1]) + exam_total
    
    #rounds to make final score
    final_score = round(total_score)
    
    #conditional to determine the letter grade based on given grading scale and final_score
    grade = 'A+' if final_score > 98 else 'A' if final_score > 88 else 'A-' if final_score > 90 else 'B+' if final_score > 88 else 'B' if final_score > 82 else 'B-' if final_score > 80 else 'C+' if final_score > 78 else 'C' if final_score > 72 else 'C-' if final_score > 70 else 'D' if final_score >= 60 else 'F'
    
    return (final_score, grade)




# print(finalGrade([[10,9,8,9]], [[5,8,0],2], [[40,10,35,5],1], mt2=70))
# #(77, 'C')
# print(finalGrade([[10,9,9,10],2], [[6,2,10],2], [[50,0]], mt2=90))
#(79, 'C+')