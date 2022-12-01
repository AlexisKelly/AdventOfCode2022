MostCalories=0
ElfWithMostCalories=0
TotalCaloriesForElf = 0
CurrentElf = 1

day1Input = open("Day1/Day1Task1Input.txt", "r")

for calorieLine in day1Input:
    if calorieLine.strip() == "":
        # Check if the Total Calories is more than currently stored
        if(TotalCaloriesForElf > MostCalories):
            MostCalories = TotalCaloriesForElf
            ElfWithMostCalories = CurrentElf
        # Reset Calories and Increment Elf
        TotalCaloriesForElf = 0
        CurrentElf+=1
        print("TotalCaloriesForElfReset:"+str(TotalCaloriesForElf)+" for next elf:"+str(CurrentElf))
        print("MostCalories:"+str(MostCalories)+" is for ElfWithMostCalories:"+str(ElfWithMostCalories))
    else:
        TotalCaloriesForElf = TotalCaloriesForElf + int(calorieLine)   
        print("CurrentElf:"+str(CurrentElf)+"CurrentCaloriesLine:"+str(calorieLine)+"TotalCaloriesForElf:"+str(TotalCaloriesForElf))

print("MostCalories:"+str(MostCalories)+" is for ElfWithMostCalories:"+str(ElfWithMostCalories))