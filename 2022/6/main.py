input = open("2022/6/input.txt", "r").read().replace("\n", "")

def firstHalf():     
    for i in range(len(input) - 3):
        if len(set(input[i:i+4])) == 4:
            print(i + 4)
            break

def secondHalf():
    for i in range(len(input) - 13):
        if len(set(input[i:i+14])) == 14:
            print(i + 14)
            break

secondHalf()