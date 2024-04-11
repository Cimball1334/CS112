##CS 112 _ 233 Python lab 4
#Author Craig Kimball
#Date 9/121/2021 11:30AM 

#Lab Description:
# based on an inputed number, create 2 functions that output 
# the sum and product of all integers up to that number


#initial input of user number
user_num = int(input("Pick a number: "))

#fuction returns the sum of all integers up to the inputed user num
def cal_sum(num):
    sum = 0
    for i in range(1,user_num,1):
        sum+=i
        
    return sum

#function returns the prduct of all integers up to the inputed user num
def cal_prod(num):
    prod = 1
    for i in range(1,user_num,1):
        prod *= i
        
    return prod

print('Sum: {:,} \nProd: {:,}'.format(cal_sum(user_num), cal_prod(user_num)),sep='\n')