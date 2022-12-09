import random
input = open("2022/7/input.txt", "r")

root = {}

def getDirByPath(path):
    if path == "/":
        return root
        
    directories = path[1:-1].split("/")

    currentDir = root
    for dir in directories:
        currentDir = currentDir[dir]

    return currentDir

dirSizes = {}
def calcDirectorySize(dirName, dir):
    size = 0
    for name, value in dir.items():
        if isinstance(value, int):
            size += value
        else:
            size += calcDirectorySize(name, value)

    dirSizes[dirName + str(random.randrange(0, 1000000000))] = size
    return size

def firstHalf():  
    currentDir = root
    path = "/"

    i = 0
    while line := input.readline().replace("\n", ""):
        i += 1
        if i == 100:
            pass

        #print(line)

        args = line.split(" ")
        if ((arg0 := args[0]) == "$"):
            match args[1]:
                case "cd":
                    match arg2 := args[2]:
                        case "/":
                            path = "/"
                            currentDir = root
                        
                        case "..":
                            path = path[:path[:-2].rindex("/")] + "/"
                            currentDir = getDirByPath(path)

                        case _:
                            path += (arg2 + "/")
                            if (arg2 not in currentDir):
                                currentDir[arg2] = {}
                            currentDir = currentDir[arg2]
                
                case "ls":
                    pass
        else:
            if arg0 == "dir":
                pass
            else:
                currentDir[args[1]] = int(arg0)

    calcDirectorySize("/", root)
    # print(
    #     sum(list(
    #         filter(
    #             lambda dirSize: dirSize <= 100000,
    #             dirSizes.values()
    #         )
    #     ))
    # )


def secondHalf():
    firstHalf()

    totalSize = max(dirSizes.values())
    availableSpace = 70000000 - totalSize
    neededSpace = 30000000 - availableSpace

    print(
        min(list(
            filter(
                lambda dirSize: dirSize >= neededSpace,
                dirSizes.values()
            )
        ))
    )
      

secondHalf()