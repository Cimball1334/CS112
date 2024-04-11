##Programming assignment 2
##Auth: Craig Kimball
##Date: 9/13/2021 (3:55pm)
import math

#function return a bool whether cell digit is even (true) or odd (false)  
def status(cell_digit):
    return (cell_digit%2)==0

#function return a str whether last name first letter is a...z
def adjective(lastname_fstletter):
    if lastname_fstletter == 'A':
        return'awesome'
    elif lastname_fstletter == 'B':
        return'shocking'
    elif lastname_fstletter == 'C':
        return'hilarious'
    elif lastname_fstletter == 'D':
        return'fascinating'
    elif lastname_fstletter == 'E':
        return'marvelous'
    elif lastname_fstletter == 'F':
        return'unbelievable'
    elif lastname_fstletter == 'G':
        return'funny'
    elif lastname_fstletter == 'H':
        return'epic'
    elif lastname_fstletter == 'I':
        return'thrilling'
    elif lastname_fstletter == 'J':
        return'wonderful'
    elif lastname_fstletter == 'K':
        return'dramatic'
    elif lastname_fstletter == 'L':
        return'intriguing'
    elif lastname_fstletter == 'M':
        return'courageous'
    elif lastname_fstletter == 'N':
        return'beautiful'
    elif lastname_fstletter == 'O':
        return'bracing'
    elif lastname_fstletter == 'P':
        return'lively'
    elif lastname_fstletter == 'Q':
        return'dangerous'
    elif lastname_fstletter == 'R':
        return'impressive'
    elif lastname_fstletter == 'S':
        return'astonishing'
    elif lastname_fstletter == 'T':
        return'interesting'
    elif lastname_fstletter == 'U':
        return'unexpected'
    elif lastname_fstletter == 'V':
        return'surprising'
    elif lastname_fstletter == 'W':
        return'lovely' 
    elif lastname_fstletter == 'X':
        return'electrifying'
    elif lastname_fstletter == 'Y':
        return'commoving' 
    else:
        return'overwhelming'
 
#function returns str for each month Jan.... Dec   
def subject(birth_month):
    if birth_month == 'Jan':
        return 'biography'
    elif birth_month == 'Feb':
        return 'history'
    elif birth_month == 'Mar':
        return 'legend'
    elif birth_month == 'Apr':
        return 'life'
    elif birth_month == 'May':
        return 'anecdote'
    elif birth_month == 'Jun':
        return 'revenge'
    elif birth_month == 'Jul':
        return 'mission'
    elif birth_month == 'Aug':
        return 'existence'
    elif birth_month == 'Sep':
        return 'battle'
    elif birth_month == 'Oct':
        return 'chronicle'
    elif birth_month == 'Nov':
        return 'combat'
    else:
        return 'fairy tale'

#function return str for last digit of the cell number 0...9   
def complement(cell_digit):
    if cell_digit == 0:
        return 'of an adventurer'
    elif cell_digit == 1:
        return 'of a warrior'
    elif cell_digit == 2:
        return 'of a genius'
    elif cell_digit == 3:
        return 'of a movie star'
    elif cell_digit == 4:
        return 'of a hero'
    elif cell_digit == 5:
        return 'of a scientific'
    elif cell_digit == 6:
        return 'of a dreamer'
    elif cell_digit == 7:
        return 'of a cowboy' 
    elif cell_digit == 8:
        return 'of a jedi'
    else:
        return 'of an ogre'
     
#function calculates the number of months based on the last cell digit (function provided)
def months(cell_digit):
    cell_digit = int(cell_digit)
    days = (math.pow(cell_digit, ((cell_digit%2)+1)) * (cell_digit))
    months = math.ceil(days/30)
    if months == 0:
        months+=1
    
    return months

#function calls all previous defined functions to fit together the movie title
def myMovieLife(lastname_fstletter, birth_month, cell_digit):
    M = 'month'
    if months(cell_digit) > 1:
        M+='s'
    
    str_out ='The' +' '+ str(status(cell_digit)) +' '+ str(adjective(lastname_fstletter)) + ' '+str(subject(birth_month)) + ' '+str(complement(cell_digit)) +' in ' + str(months(cell_digit)) +' '+ M
    return str_out      


#myMovieLife('G', 'Jan', 6)
