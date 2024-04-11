#CS 112 _ 233 Python lab 5
#Author Craig Kimball
#Date 9/28/2021 11:30AM 


def equal_sum(numbers):
    isTrue = True
    for i in range(2,len(numbers)-1): 
        if(numbers[i-1] + numbers[i-2] != numbers[i]):
            isTrue = False
    return isTrue

# print(equal_sum([6,2,8,10,18]))
# print(equal_sum([1,1,2,3,5,8,13]))
# print(equal_sum([2,1,3,2,5,1]))