#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 9
# Date: 11/20/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------


class DataError(Exception):
    #constructor that takes  in a msg string    
    def __init__(self, msg):
        self.msg = msg
        
    #to string method that prints the msg
    def __str__(self):
        return self.msg


class Detective:
    #constructor method
    #name: str, the name of the detective
    #cases: list of str of case names
    #solved_cases: list of str of cases that have been solved
    def __init__(self, name, cases, solved_cases):
        #try start
        try:
            
            if len(solved_cases) > len(cases):
                
                #num of solved cases is larger than the number of cases total
                raise DataError("Solved cases cannot be more than total cases!")
            
            #sets instance methods
            self.name = name
            self.cases = cases
            self.solved_cases = solved_cases
            self.num_cases = len(cases)
            self.num_solved = len(solved_cases)
            
        #catches raised error   
        except DataError as error:
            print(error)

    #to string method
    def __str__(self): 
        #"Detective Mark Halpert: total cases 4, solved 2, failed 2."
        return ('Detective {}: total cases {}, solved {}, failed {}.'.format(self.name,len(self.cases),len(self.solved_cases),self.num_failed_cases()))
   
    #Returns the number of failed cases for a given detective object
    def num_failed_cases(self):
        #cats to sets to take advantage of their opperations to return the lenght of items only in the first list, cases
        return len(set(self.cases)-set(self.solved_cases))
    
    #Adds information for either solved or unsolved cases 
    #new_cases: list of str containing unique case names to that detective
    #new_solved: list of ints indicating the position in new_cases of solved cases   
    def add_new_cases(self, new_cases, new_solved):  
        
        #try start
        try:
            if len(new_solved) > len(new_cases):
                raise DataError("New solved cases cannot be more than new cases!")  
                
            #adds cases to solved cases first
            for i in range(len(new_solved)):
                #appends the solved_cases instance list
                #new_cases [ index defined by new_solved [ current iteration i] ]
                self.solved_cases.append(new_cases[new_solved[i]-1])
               
            #adds all the new cases to the cases list   
            for c in range(len(new_cases)):
                self.cases.append(new_cases[c])
                
            #updates instance variables   
            self.num_cases = len(self.cases)
            self.num_solved = len(self.solved_cases) 
          
        #catches error raised       
        except DataError as error:
            print(error)
        
    #Gets a list of failed cases    
    def failed_cases(self):
        rtn = []
        for c in self.cases:
            if c not in self.solved_cases:
                rtn.append(c)
        return rtn
    
    
    
    
# d = Detective('First Last',['Case 1','Case 2','Case 3','Case 4'],['Case 2','Case 4'])
# print(d)
# print(d.failed_cases())
# print(d.num_failed_cases())
# d.add_new_cases(['Case 5','Case 6'], [2])
# print(d.failed_cases())
# print(d.cases)


        
        