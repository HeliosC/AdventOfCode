import re
import queue as Queue

input = open("2022/5/input.txt", "r")

def parseInitialStacks():
    stacks = {}
    while line := input.readline().replace("\n", ""):
        items = list(
            filter(
                lambda e: len(e) != 0,
                re.split('\[|\]', line)
            )
        )

        if (len(items) < 2):
            continue

        itemstack = 0
        for item in items:
            spaces = item.count(" ")
            match spaces:
                case 0:
                    if itemstack in stacks:
                        stacks[itemstack].append(item)
                    else:
                        stacks[itemstack] = [item]

                case 1:
                    itemstack += 1
                    
                case _:
                    itemstack += (spaces + 3)//4 

    return stacks

def firstHalf():
    stacks = parseInitialStacks()

    # Convert lists to queues
    queues = {}
    for i, stack in stacks.items():
        queues[i] = Queue.LifoQueue()
        while len(stack) > 0:
            queues[i].put(stack.pop())
            
    while line := input.readline().replace("\n", ""):
        # Parse input and convert to integers
        match = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        (quantity, initialStack, finalStack) = [int(i) for i in match.groups()]

        for _ in range(quantity):
            queues[finalStack - 1].put(queues[initialStack - 1].get())

    print("".join([queues[i].get() for i in range(len(queues))]))

def secondHalf():
    stacks = parseInitialStacks()

    # Convert lists to queues
    queues = {}
    for i, stack in stacks.items():
        queues[i] = Queue.LifoQueue()
        while len(stack) > 0:
            queues[i].put(stack.pop())
            
    while line := input.readline().replace("\n", ""):
        # Parse input and convert to integers
        match = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        (quantity, initialStack, finalStack) = [int(i) for i in match.groups()]

        tempQueue = Queue.LifoQueue()
        for _ in range(quantity):
            tempQueue.put(queues[initialStack - 1].get())

        while not tempQueue.empty():
            queues[finalStack - 1].put(tempQueue.get())

    print("".join([queues[i].get() for i in range(len(queues))]))


secondHalf()