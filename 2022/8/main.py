input = open("2022/8/input.txt", "r")

def parseData():
    data = []
    while line := input.readline().replace("\n", ""):
        data.append(list(line))

    return data

def firstHalf():  
    trees = parseData()

    visibleTrees = 0
    for y, treeLine in enumerate(trees):
        for x, treeHeigth in enumerate(treeLine):
            for i in range (0, x):
                if trees[y][i] >= treeHeigth:
                    break
            else:
                visibleTrees += 1
                continue

            for i in range (x + 1, len(treeLine)):
                if trees[y][i] >= treeHeigth:
                    break
            else:
                visibleTrees += 1
                continue

            for j in range (0, y):
                if trees[j][x] >= treeHeigth:
                    break
            else:
                visibleTrees += 1
                continue

            for j in range (y + 1, len(trees)):
                if trees[j][x] >= treeHeigth:
                    break
            else:
                visibleTrees += 1
                continue

    print(visibleTrees)

def secondHalf():  
    trees = parseData()

    # scores = [[0]* len(trees[0])] * len(trees)

    bestTreeScore = 0
    for y, treeLine in enumerate(trees):
        for x, treeHeigth in enumerate(treeLine):

            score = 1
            treeRange = 0
            for i in range (x - 1, -1, -1):
                treeRange += 1
                if trees[y][i] >= treeHeigth:
                    break    
            score *= treeRange

            treeRange = 0
            for i in range (x + 1, len(treeLine)):
                treeRange += 1
                if trees[y][i] >= treeHeigth:
                    break
            score *= treeRange
            
            treeRange = 0
            for j in range (y - 1, -1, -1):
                treeRange += 1
                if trees[j][x] >= treeHeigth:
                    break
            score *= treeRange

            treeRange = 0
            for j in range (y + 1, len(trees)):
                treeRange += 1
                if trees[j][x] >= treeHeigth:
                    break
            score *= treeRange

            if score > bestTreeScore:
                bestTreeScore = score

    print(bestTreeScore)
    
secondHalf()