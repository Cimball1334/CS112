age = int(input("How old is she? (in years):"))
weight = int(input("How much does she weight? (in pounds):"))
height = int(input("How tall is she? (in inches):"))
intake = int(input("How much does she take in a day? (in kcal):"))

def calorie():
    #female who does moderate exercise
    return 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

cal = calorie()
ideal = cal*1.55
perc = (intake/ideal)*100

print('BMR: {:.2f} kcal'.format(cal))
print('Her ideal intake for a day is {:0.2f} kcal.'.format(ideal))
print('Her intake is {:.2f}% of what is recommended.'.format(perc))