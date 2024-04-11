#CS 112 _ 233 Python lab 10
#Author Craig Kimball
#Date 11/2/2021 11:30AM 

def savings(bal,years):
     
    if years == 0:
        rtn = int(bal*100)/100
        return rtn
    else:
        bal*=1.06
        rtn = savings(bal, years-1)
        
    return rtn    
    
# print(savings(1000, 20))
# print(savings(5000, 20))
# print(savings(500, 20))