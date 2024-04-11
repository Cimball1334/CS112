#CS 112 _ 233 Python lab 12
#Author Craig Kimball
#Date 11/16/2021 11:30AM

#Part A
def sum_strings(*str): 
    sum = 0
    for num in str:
        
        try:
            try:
                sum+=int(num)
            except:
                sum-= float(num)
        except:
            sum = 'ValueError Exception'
        
    try:
        return round(sum)
    except:
        return sum
"""
print(sum_strings('1', '5', '-4'))
print(sum_strings('11', '15', '4.2', '3', '-3.1'))
print(sum_strings('0', '10', 'Mason', '-7'))
"""


#Part B
class Point():
    
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
       
    def __str__(self):
        return '%s, %s' % (str(self.x), str(self.y))
    
    def move_to(self,x,y):
        self.x = x
        self.y = y
        
    def move_by(self,x,y):
        self.y += y
        self.x += x

"""  
p1 = Point(2, 3)
print(p1) #prints 2, 3
p1.move_to(5, 6)
print(p1) #prints 5, 6
p1 = Point(2, 3)
print(p1) #prints 2, 3
p1.move_by(5, 6)
print(p1) #prints 7, 9
"""
