import re
import queue as Queue
from math import lcm

regex = (r"Monkey (\d):\n"
	r"  Starting items: (.*)\n"
	r"  Operation: new = old (\W) (\S*)\n"
	r"  Test: divisible by (\d*)\n"
	r"    If true: throw to monkey (\d)\n"
	r"    If false: throw to monkey (\d)")

input = open("2022/11/input.txt", "r").read()

class Monkey:
    def __init__(self, monkeyId, items, operator, operand, divideTest, monkeyTrue, monkeyFalse):
        self.id = int(monkeyId)

        queue = Queue.Queue()
        for item in items.split(", "):
            queue.put(int(item))
        self.items = queue

        self.operator = operator
        self.operand = operand
        self.divideTest = int(divideTest)
        self.monkeyTrue = int(monkeyTrue)
        self.monkeyFalse = int(monkeyFalse)

        self.elementsInspected = 0

    def calculateNewWorryLevel(self, old, worryLeveldivider):
        operand = 0
        if self.operand == "old": 
            operand = old 
        else: 
            operand = int(self.operand)

        result = 0
        match self.operator:
            case '+':
                result = old + operand
            case '*':
                result = old * operand
        
        return result // worryLeveldivider

    def getNextMonkey(self, new):
        if new % self.divideTest == 0:
            return self.monkeyTrue
        else:
            return self.monkeyFalse

def parseData():
    monkeys = []
    for match in re.finditer(regex, input):
        (monkeyId, items, operator, operand, divideTest, monkeyTrue, monkeyFalse) = match.groups()
        monkeys.append(Monkey(monkeyId, items, operator, operand, divideTest, monkeyTrue, monkeyFalse))

    return monkeys

def firsthalf():
    monkeys = parseData()
    for round in range(1000):
        for monkey in monkeys:
            while not monkey.items.empty():
                monkey.elementsInspected += 1
                newWorryLevel = monkey.calculateNewWorryLevel(monkey.items.get(), 3)
                nextMonkey = monkeys[monkey.getNextMonkey(newWorryLevel)]
                nextMonkey.items.put(newWorryLevel)

    elementsInspectedlist = [monkey.elementsInspected for monkey in monkeys]
    elementsInspectedlist.sort(reverse = True)
    print(elementsInspectedlist[0] * elementsInspectedlist[1])

    #for monkey in monkeys:
    #    print("----")
    #    while not monkey.items.empty():
    #        print(monkey.items.get())

def secondhalf():
    monkeys = parseData()
    PPCM = lcm(*[monkey.divideTest for monkey in monkeys])

    for round in range(10000):
        for monkey in monkeys:
            while not monkey.items.empty():
                monkey.elementsInspected += 1
                newWorryLevel = monkey.calculateNewWorryLevel(monkey.items.get(), 1) % PPCM
                nextMonkey = monkeys[monkey.getNextMonkey(newWorryLevel)]
                nextMonkey.items.put(newWorryLevel)

    for monkey in monkeys:
        print(monkey.elementsInspected)

    elementsInspectedlist = [monkey.elementsInspected for monkey in monkeys]
    elementsInspectedlist.sort(reverse = True)
    print(elementsInspectedlist[0] * elementsInspectedlist[1])

secondhalf()