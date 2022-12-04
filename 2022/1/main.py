input = open("2022/1/input.txt", "r")

def firstHalf():    
    maxCalories = 0
    elfCalories = 0
    while line := input.readline():
        try:
            elfCalories += int(line)
        except:
            if elfCalories > maxCalories:
                maxCalories = elfCalories
            elfCalories = 0

    print(maxCalories)

def addAndSort(tab, value):
    tab.append(value)
    tab.sort(reverse = True)

def secondHalf():    
    maxCalories = []
    elfCalories = 0
    while line := input.readline():
        try:
            elfCalories += int(line)
        except:
            if len(maxCalories) < 3:
                addAndSort(maxCalories, elfCalories)
            else:
                if elfCalories > maxCalories[-1]:
                    addAndSort(maxCalories, elfCalories)
                    maxCalories.pop()
            elfCalories = 0

    print(maxCalories, sum(maxCalories))

secondHalf()