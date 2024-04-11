# 1. Greet the user with the message, "Welcome to the Sims4 Builder Helper!"
# 2. Ask the user: "What is the width of your lot in Sim units? "
# 3. Ask the user: "What is the length of your lot in Sim units? "
# 4. Ask the user: "What is your specific item? "
# 5. Ask the user: "What is the width of your specific item in Sim units? "
# 6. Ask the user: "What is the length of your specific item in Sim units? "
# 7. Compute the area of the lot in generic Sim square units and display it to the user
# 8. Compute the area of the lot in square feet and display it to the user
# 9. Compute the dimensions of the specific item to feet by feet and display it to the user
# 10.Compute how many of the item will fit in the lot
# a. You should also determine the percent of the lot area covered and display that to
# the user
# 11.Compute how much space is left uncovered by the item due to not enough space and
# display that to the user
# a. You should also determine what percent of the lot area is not covered and display
# that to the user
# 12.Tell the user to enjoy building!

#intro statement
print('Welcome to the Sims4 Builder Helper!')

#this is responsible for the gathering of information from the user
lotWidth = float(input('What is the width of your lot in Sim units? '))
lotLength = float(input('What is the length of your lot in Sim units? '))
item = input('What is your specific item? ')
itemWidth = float(input('What is the width of your specific item in Sim units? '))
itemLength = float(input('What is the length of your specific item in Sim units? '))

#Math section
#handles all the calculations
possibleItemsLength = int(lotLength / itemLength)
possibleItemsWidth = int(lotWidth / itemWidth)
numItems = possibleItemsLength * possibleItemsWidth

lotArea = lotLength * lotWidth
lotAreaFeet = (lotLength * 4) * (lotWidth * 4)

percentageCovered = ((((itemWidth) * (itemLength)) * numItems ) / lotArea) * 100
squaresLeft = (100 - percentageCovered) * lotArea / 100


#output section
#this is the final return to console for the user
print('The area of your lot in Sim units is',int(lotArea) , 'square units')
print('The area of your lot in square feet is', int(lotAreaFeet), 'square ft')

print('The', item,  'in the real world is about',int(itemWidth*4), 'ft by', int(itemLength*4),'ft')
print('About', int(numItems),item + 's can fit in this lot')
print('About ', int(percentageCovered),'% of the lot is covered by the ', item + "s", sep='')
print('About ', int(squaresLeft) ,' square units is left uncovered', sep='')
print('About ',int(100 - percentageCovered),'% of the lot is left uncovered', sep='')

#goodbye statement
print('Have fun building!')
#fails the last test on the tester.py due to this line giving a new line after it but all of the other test require it?
