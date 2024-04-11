#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 6
# Date: 11/1/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------

#function returns the number of times the product of division between to integers is an even number
def even_divide_count(num1, num2):
    #division is the whole number divisor of the two ints
    division = num1//num2
    #if the division is an even number
    if division % 2 == 0 and division!= 0:
        #recursive call with the current division and the second int
        return 1+even_divide_count(division, num2)
    else:
        #default case if division is never an even number
        return 0

# print(even_divide_count(13, 2))
# print(even_divide_count(24, 3))
# print(even_divide_count(9, 3))

#function returns a list that is a combination of the ys list, and the sum of each index's terms in xs list
def add_sum(xs, ys):
    #does xs contain elements?
    if len(xs) > 0:
        #contingency check for recursive call, does the list have more indexes than the current one
        if(len(xs)>1):
            #append the sum to ys list
            ys.append(sum(xs[0]))
            #recursive call that removes the first index from xs and has the new ys list
            add_sum(xs[1:],ys)
        else:
            #if xs only has one element, no recursive call is needed so append sum to ys
            ys.append(sum(xs[0]))
    #returning ys list with sums appeneded to the end, or original list if no sums were found
    return ys
    
# print(add_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]], [3, 4, 5]))
# print(add_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]], []))
# print(add_sum([[]], [3, 4, 5]))
# print(add_sum([], [3, 4, 5]))

#function returns a tuple that contains a combination of the 2 strings with characters alternating on n interval
def swap_chars(str1, str2, n):
    #i approached the problem by segmenting the strings into section of n length:
    
    #if section with n length is possible
    if (len(str1) >= n and len(str2) >= n):
        #stores a character that will be overwritten
        chr1 = str1[n-1]
        #saves the tuple here for only one recursive call
        #recursive call that shortens the strings by n
        tpl = swap_chars(str1[n:],str2[n:],n)
        #substringing to swap character
        str1 = str1[:n-1] + str2[n-1] + tpl[0]
        #substringing to swap character
        str2 = str2[:n-1] + chr1 +tpl[1]
        #return tuple of new strings
        return (str1,str2)
    #return tuple of re-ordered strings
    return (str1,str2)

# print(swap_chars("hello", "HELLO", 2)) 
# print(swap_chars("hello", "HELLO", 3))   
# print(swap_chars("what a beautiful day", "sun is shining in new year's day", 4))   

#function returns list that contains the elements of some_list reordered to a specified pattern
def modify_order(some_list):
    #does the list contain more than 2 indexes
    if(len(some_list)>=2):
        #return list and recursive call with shortened list
        return [some_list[0],some_list[-1]] + (modify_order(some_list[1:len(some_list)-1]))
    else:
        #list is already in specified order, return list
        return some_list

# print(modify_order([1, 2, 3, 4, 5, 6]))
# print(modify_order([7, 18, 'new', 4, 'hello']))
# print(modify_order([23, 74, 5, 17, 2, 0, 100, 36, 7]))
# print(modify_order([]))

#function returns the total number of possible positive subtractions 
def subtract_inc(num1, num2, num3=None):
    tempCount1 = 0
    tempCount2 = 0
    #if there is no 3rd argument
    if num3 == None:
        #if subraction is positive
        if num1 - num2 >= 0:
            #1 + recursive call with the new num1, and an incrementation to num2
            return 1 + subtract_inc(num1-num2,num2+1)
    else:
        #if there is a 3rd argument the logic must change
        #checks to see if subraction between num1 and num2 is positive
        if num1 - num2 >= 0:
            #stores the count and recursive call without num 3 for simplicity
            tempCount1 =  1 + subtract_inc(num1-num2,num2+1)
        #if the subtraction between num1 and num3 is positive
        if num1 - num3 >= 0:
            #stores the count and recursive call
            #sets num2 to num1+1 to ensure that it does not double count the posible subtractions from num2 and num1
            tempCount2 = 1 + subtract_inc(num1-num3,num1+1,num3+1)
        #returns the total count
        return tempCount1 + tempCount2
    #default case of no subtractions
    return 0
    
# print(subtract_inc(10, 2, 5))
# print(subtract_inc(10, 2))
# print(subtract_inc(10, 15, 8))
# print(subtract_inc(100, 50, 10))