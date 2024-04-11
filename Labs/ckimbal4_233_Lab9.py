#CS 112 _ 233 Python lab 9
#Author Craig Kimball
#Date 10/26/2021 11:30AM 

#method to shift the list with a positive shift index
def right_shift(list, shift):
    nlist = []
    for i in range(len(list)):
        if i < shift:
            nlist.append(list[0])
        else:
            nlist.append(list[i-shift])
    
    return nlist

#method to shift the lest with a negative shift index
def left_shift(list, shift):
    nlist = []
    for i in range(len(list)):
        if i >= -shift:
            nlist.append(list[-1])
        else:
            nlist.append(list[i+shift])
    
    return nlist
    
#method to determine what shift needs to happen based on the value of the shift index
def my_shift(list, shift):
    if shift < 0:
        return left_shift(list, shift)
    else:
        return right_shift(list, shift)
    

# print(my_shift([1,2,3,4,5,6], 3))
# print(my_shift([1,2,3,4,5,6], -3))
# print(my_shift([1,2,3,4,5,6], 0))
# print(my_shift([1,2,3,4,5,6], 10))