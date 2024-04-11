#CS 112 _ 233 Python lab 3
#Author Craig Kimball
#Date 9/14/2021 11:30AM 


#Rates
#10k and below : 0.5% of the price
#10k to 25k : 1% of the price
#25k and over : 2% of the price

#discounts 
#18-25 : 0%
#25 - 40 : 5%
#40 - 60 : 10%
#60 and over : 15%

#students get 10$ discount

#any customer that has an accident is increased by 20 and no promo code

def calcMonthlyRate(price, age, accident,promocode):
    total = 0
    if price < 10000 :
        rate = 0.005 * price
        #total = rate * price
    elif price <25000 :
        rate = 0.01 * price
        #total = rate * price
    else:
        rate = 0.02 * price
        #total = rate * price
    if age < 25 :
        pass
    elif age < 40 :
        rate*= 0.95
    elif age < 60 :
        rate*= .90
    elif age > 59 :
        rate*= .85

    if promocode == 'MASONPATRIOTS2021' :
        promo = True
    else:
        promo = False
        
    if accident == 'yes' :
        acc = True
    else:
        acc= False
        
    if(acc):
        if(promo):
            total += total*.2
            rate*=1.2
        else:
            total += total*.2
            rate*=1.2
    else:
        if(promo):
            rate-= 10  
        else:
            pass
       
    #forcing the 2 decimal places rounding 
    # rate *= 100
    # print(rate)
    # rate = int(rate)
    # print(rate)
    # rate = float(rate/100)
    return rate
            
print('{:.2f}'.format(calcMonthlyRate(23500, 19, 'yes', 'MASONPATRIOTS2021')))
print('{:.2f}'.format(calcMonthlyRate(7650, 27, 'no', 'MASONPATRIOTS2021')))
print('{:.2f}'.format(calcMonthlyRate(28653, 45, 'no', 'MASONPATRIOTS2000')))          
print('{:.2f}'.format(calcMonthlyRate(9320, 65, 'yes', 'MASON2021')))
