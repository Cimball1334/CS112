##Programming assignment 3
##Auth: Craig Kimball
##Date: 9/27/2021 (3:15pm)

##GMU HONOR CODE
#To promote a stronger sense of mutual responsibility, respect, trust, and fairness among all
#members of the George Mason University Community and with the desire for greater academic
#and personal achievement, we, the student members of the university community, have set for
#This Honor Code: Student Members of the George Mason University community pledge not to 
#cheat, plagiarize, steal, or lie in matters related to academic work.

#rest time method
#calculates the number of hours you need to rest by the miles driven and the brake count
#hours rested is equal to the number of times the divisor is an even number. the count stops on the first odd number
def rest_time(miles_driven, brake_count):
    rest_time = 0
    while (miles_driven > brake_count):
        if(miles_driven/brake_count % 2 == 0):
            rest_time+=1
            rest_time = miles_driven / brake_count
        else:
            break
    return rest_time

#method return the speedster id based on the integer and float values in a list
def which_speedster(feature_values):
    prod = 0
    sum = 0
    for i in feature_values:
        if int(i) == i:
            sum+=i
        else:
            if prod ==1:
                prod+=1
            prod*=i
    return prod/sum

#function return the int lifespan of an entity based on the relationship between the number of fingers on each hand, the number of toes it has
#and its divisor.
def lifespan(fingers_list, num_toes):
    life=0
    for f in fingers_list:
        life+= int(f/num_toes)
    return life

#funtion calculates the wizarding level of a student based on their spell list and restricted spells.
def wiz_level(spell_list, owl_lower_bound, owl_upper_bound):
    wizarding_level = ''
    mega_spell = 'On O.W.L'
    exp = 0
    bad = {"Crucio", "Imperio", "Avada_Kedavra"}
    ok = {"Confringo", "Sectumsempra", "Fiendfyre"}
    
    for spell in spell_list:
        mega_spell+=spell
        if spell in bad:
            exp+=0
        else:
            if spell in ok:
                if exp < owl_lower_bound:
                    exp+=7
                else:
                    exp+=5
            else:
                exp+=10
    
    if exp > owl_upper_bound:
        wizarding_level = 'Beyond O.W.L'
    elif exp < owl_lower_bound:
        wizarding_level= 'Below O.W.W'
    
    return wizarding_level + " " + "Mega Spell:" + " " + mega_spell





