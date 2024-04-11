#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 4
# Date: 10/7/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
def swap_text(text):
    rtn = ''
    #for loop that goes through each pair, only goes to even index, so I must check if its a single character
    for i in range(0,len(text),2):
        #checks if there is a character after the current
        if i < len(text)-1:
            rtn += text[i+1]+text[i]
        #if no character (last character) then just add current
        else:
            rtn += text[i]
               
    return rtn

def which_day(numbers):
    rtn = ''
    sum1 = 0
    sum2 = 0
    #loops through every number by index
    for i in range(len(numbers)):
        #if the index is even add to sum1
        if i%2 == 0:
            sum1+=numbers[i]
        #if the index is not even (odd) add to sum2
        else:
            sum2+=numbers[i]
    rtn = 'Monday' if abs(sum1-sum2)%7 == 1 else 'Tuesday' if abs(sum1-sum2)%7 == 2 else 'Wednesday' if abs(sum1-sum2)%7 == 3 else 'Thursday' if abs(sum1-sum2)%7 == 4 else 'Friday' if abs(sum1-sum2)%7 == 5 else 'Saturday' if abs(sum1-sum2)%7 == 6 else 'Sunday'
    
    return rtn


def delete_duplicates(items):
    #since i cannot remove or delete items from the list I must start with a new one
    rtn = []
    
    #when in doubt use a flag
    #I used a flag here because it allows me to make an action after checking every element of the new list 
    is_duplicate = False
    
    #loops through every element in original list
    for i in range(len(items)):
        is_duplicate = False
        
        #since I cant use in I am checking if the current item is in the new list already by checking against every item already in it.
        #essential this is my own 'in' function
        for j in range(len(rtn)):
            if items[i] == rtn[j]:
                    #updates flag state
                    is_duplicate = True
                    
        #logic statement says if its not in the new list add it 
        if(not(is_duplicate)):
            rtn.append(items[i])       

    return rtn

def final_guests(draft_guests, new_guest):
    rtn = []
    
    alphabet = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    current_name_index = 0
    new_name_index = 99
    #runs this section of code if and only if the list and new guest are populated
    if len(draft_guests) > 0 and len(new_guest) >0 and draft_guests[0] != '':
        
        #this function checks the alphabetical idex of the new guest name
        for i in range(len(alphabet)):
            if new_guest[0] == alphabet[i]:
                new_name_index = i
        #this loop go through ever guest of the draft list
        for guest in draft_guests:
            
            #gets the alphabetical index of the current guest
            for i in range(len(alphabet)):
                
                if guest[0] == alphabet[i]:
                    current_name_index = i
            #compares indexes to confirm order and adds the current guest and new guest in their respective places    
            if new_name_index < current_name_index and new_name_index >= 0:
                rtn.append(new_guest)
                #this statement makes sure the new guest cant be added multiple times
                new_name_index = -1
                rtn.append(guest)
            else:
                rtn.append(guest)
        
        #confirms that the name was added somewhere, if not adds it to the end
      
        if(26 > new_name_index > 0):
            rtn.append(new_guest)
    
    #checks for the possibility that the new guest is an empty string and adds it to the front
    if(len(draft_guests) > 0 and len(new_guest) <= 0):
        rtn = [new_guest]
        for guest in draft_guests:
            rtn.append(guest)  
            
    #checks for the possibility that the guest list is '' and the new guest hasnt been added
    #has to check to see if list is populated to avoid index errors
    if(len(draft_guests) >0):
        if(draft_guests[0] == ''):
            for guest in draft_guests:
                rtn.append(guest)  
            rtn.append(new_guest)
    #checks to see if the list remains empty, and adds the new guest to the list         
    if(len(rtn) == 0):
        rtn.append(new_guest)
    return rtn

