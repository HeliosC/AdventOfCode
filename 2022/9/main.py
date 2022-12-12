input = open("2022/9/input.txt", "r")

def firstHalf():  
    land = [['#']]
    Xh, Yh = 0, 0
    Xt, Yt = 0, 0

    while line := input.readline().replace("\n", ""):
        (direction, moves) = line.split(" ")

        for _ in range(int(moves)):
            match direction:
                case "R":
                    Xh += 1

                case "L":
                    Xh -= 1

                case "U":
                    Yh += 1

                case "D":
                    Yh -= 1

            if abs(Xh - Xt) > 1 or  abs(Yh - Yt) > 1:
                # move tail

                if Xh < Xt:
                    Xt -= 1
                elif Xh > Xt:
                    Xt += 1

                if Yh < Yt:
                    Yt -= 1
                elif Yh > Yt:
                    Yt += 1

                if Yt == -1:
                    land = [[]] + land
                    Yt = 0
                    Yh += 1

                if Xt == -1:
                    for x in range(len(land)):
                        land[x] = ['.'] + land[x]
                    Xt = 0
                    Xh += 1

                for j in range(len(land), Yt + 1):
                    land.append([])

                for i in range(len(land[Yt]), Xt + 1):
                    land[Yt].append('.')

                land[Yt][Xt] = '#'

    print(sum([list.count('#') for list in land]))

def secondHalf():  
    land = [['#']]
    rope = [[0, 0] for _ in range(10)]

    while line := input.readline().replace("\n", ""):
        (direction, moves) = line.split(" ")

        for _ in range(int(moves)):
            match direction:
                case "R":
                    rope[0][0] += 1

                case "L":
                    rope[0][0] -= 1

                case "U":
                    rope[0][1] += 1

                case "D":
                    rope[0][1] -= 1

            for i in range(1, len(rope)):
                (Xh, Yh) = rope[i-1]
                if abs(Xh - rope[i][0]) > 1 or abs(Yh - rope[i][1]) > 1:
                    # move tail

                    if Xh < rope[i][0]:
                        rope[i][0] -= 1
                    elif Xh > rope[i][0]:
                        rope[i][0] += 1

                    if Yh < rope[i][1]:
                        rope[i][1] -= 1
                    elif Yh > rope[i][1]:
                        rope[i][1] += 1

                    if rope[i][1] == -1:
                        land = [[]] + land
                        for i2 in range(len(rope)):
                            rope[i2][1] += 1

                    if rope[i][0] == -1:
                        for x in range(len(land)):
                            land[x] = ['.'] + land[x]
                        for i2 in range(len(rope)):
                            rope[i2][0] += 1

                    for j in range(len(land), rope[i][1] + 1):
                        land.append([])

                    for ii in range(len(land[rope[i][1]]), rope[i][0] + 1):
                        land[rope[i][1]].append('.')

            land[rope[-1][1]][rope[-1][0]] = '#'

    print(sum([list.count('#') for list in land]))

secondHalf()