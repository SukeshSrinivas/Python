#length,breadth = map(int, input("Enter numbers: ").split())
#Area = length*breadth
#print(int(Area))


#Tip calculator
#what was the total bill?
#what percentage of tip would you like to give 10,12,15
#how many people to split the bill

'''
billAmount = float(input("What was the total bill?:"))
tipPercentage = float(input("What percentage of tip would you like to give 10,12,15?:"))
peopleToSplitBill = float(input("How many people to split bill?:"))
totalValue = billAmount+(billAmount*tipPercentage/100)
perPersonsSplit = totalValue/peopleToSplitBill
print(f"Personwise split is {perPersonsSplit}")
'''

#Write a code to calculate the bMI
#bmi = (weight in kg/height square in m)

weightOfPerson = float(input("What is your weight in kg?:"))
heightOfPerson = float(input("What is your height in meters?:"))
bmi = weightOfPerson / (heightOfPerson**2)
print("Your BMI is " + str(bmi))


#Life in week left 
#Averge life is 4000 week