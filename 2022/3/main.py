input = open("2022/3/input.txt", "r")

def calclPriority(item):
    priority = 0
    itemOrd = ord(item) # returns the number representing the unicode code (as an integer) of the character
    if (itemOrd >= ord("a")): 
        priority += (itemOrd - ord("a") + 1)
    else:
        priority += (itemOrd - ord("A") + 27)
        
    return priority 
       
def firstHalf():
    prioritiesSum = 0
    while line := input.readline().replace("\n", ""):
        # Spliting inventory
        middleIndex = int(len(line) / 2)
        compartment1 = line[:middleIndex]
        compartment2 = line[middleIndex:]

        # Finding common item
        for item in compartment1:
            if item in compartment2:
                prioritiesSum += calclPriority(item)
                break
            
    print(prioritiesSum)
    
def secondHalf():
    prioritiesSum = 0
    elfGroup = []
    while line := input.readline().replace("\n", ""):
        # Building elfGroup
        elfGroup.append(line)
    
        if (len(elfGroup) == 3):
            # Finding common item
            for item in elfGroup[0]:
                if item in elfGroup[1] and item in elfGroup[2]:
                    prioritiesSum += calclPriority(item)
                    break
           
            elfGroup = []
    
    print(prioritiesSum) 
secondHalf()