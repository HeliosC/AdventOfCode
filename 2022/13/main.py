import ast
import functools

def parseData():
    return [[ast.literal_eval(packet) for packet in pair.split("\n")] for pair in open("2022/13/input.txt", "r").read().split("\n\n")]

def firstHalf():
    data = parseData()
    goodpairs = 0
    for i, pair in enumerate(data, start=1):
        (packet1, packet2) = pair
        if compareLists(packet1, packet2) == -1:
            goodpairs += i
    print(goodpairs)

def compareLists(list1, list2):
    for i in range(len(list1)):
        if len(list2) <= i:
            return 1

        item1, item2 = list1[i], list2[i]

        if not isinstance(item1, int) :
            if not isinstance(item2, int):
                if (result := compareLists(item1, item2)) != 0:
                    return result
                else:
                    continue
            else: 
                if (result := compareLists(item1, [item2])) != 0:
                    return result
                else:
                    continue
        elif not isinstance(item2, int):
            if (result := compareLists([item1], item2)) != 0:
                return result
            else:
                continue

        if item1 > item2:
            return 1
        elif item1 < item2:
            return -1
    else:
        if len(list2) > len(list1):
            return -1
        else:
            return 0

def secondHalf():
    rawData = parseData()
    data = []
    for item in rawData:
        data.extend(item)
    
    KEY1 = [[2]]
    KEY2 = [[6]]
    data.append(KEY1)
    data.append(KEY2)

    sortedList = sorted(data, key=functools.cmp_to_key(compareLists))
    print((sortedList.index(KEY1) + 1) * (sortedList.index(KEY2) + 1))

secondHalf()