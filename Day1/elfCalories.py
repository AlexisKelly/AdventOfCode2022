
calorieTotals = []
TotalCaloriesForElf = 0

day1Input = open("Day1/Day1Task1Input.txt", "r")

for calorieLine in day1Input:
    if calorieLine.strip() == "":
        calorieTotals.append(TotalCaloriesForElf)
        TotalCaloriesForElf = 0
    else:
        TotalCaloriesForElf = TotalCaloriesForElf + int(calorieLine)
calorieTotals.sort()
TopThreeCalorieTotal = calorieTotals[-1] + calorieTotals[-2] + calorieTotals[-3]
print("MostCalories:"+str(calorieTotals[-1]))
print("SecondMostCalories:"+str(calorieTotals[-2])+" ThirdMostCalories:"+str(calorieTotals[-3]))
print("TopThreeCalories:"+str(TopThreeCalorieTotal))