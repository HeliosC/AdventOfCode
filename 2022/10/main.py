input = open("2022/10/input.txt", "r")

def addDelayed():
    a = ""

def firstHalf():
    strength = 0
    cycle = 0
    x = 1
    while line := input.readline().replace("\n", ""):
        args = line.split(" ")

        oldx = x
        oldCycle = cycle
        match args[0]:
            case "addx":
                cycle += 2
                x += int(args[1])

            case "noop":
                cycle += 1
 
        if (saveCycle := (cycle - 20) // 40) != (oldCycle - 20) // 40:
            strength += oldx * (saveCycle * 40 + 20)
            # print(cycle, x, strength)
    
    print(strength)

def secondHalf():
    screen = [[" " for _ in range(40)] for _ in range(6)]
    cycle = 0
    x = 1
    while line := input.readline().replace("\n", ""):
        args = line.split(" ")

        deltaCycle = 1
        deltax = 0
        match args[0]:
            case "addx":
                deltaCycle = 2
                deltax = int(args[1])

        for _ in range(deltaCycle):
            if abs(x - cycle % 40) <= 1:
                screen[cycle // 40][cycle % 40] = '#'

            cycle += 1
        
        x += deltax
 
    for s in screen:
        print("".join(s))

secondHalf()