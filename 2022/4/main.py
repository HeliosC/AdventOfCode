import re

REGEX = r"(\d+)-(\d+),(\d+)-(\d+)"
input = open("2022/4/input.txt", "r")

def firstHalf():
    fullOverlaps = 0
    while line := input.readline():
        # Parse input and convert to integers
        match = re.search(REGEX, line)
        (elf1start, elf1end, elf2start, elf2end) = [int(i) for i in match.groups()]
        
        # Check full overlap
        if (elf1start <= elf2start and elf1end >= elf2end) or (elf1start >= elf2start and elf1end <= elf2end):
            fullOverlaps += 1
            
    print(fullOverlaps)
    
def secondHalf():
    fullOverlaps = 0
    while line := input.readline():
        # Parse input and convert to integers
        match = re.search(REGEX, line)
        (elf1start, elf1end, elf2start, elf2end) = [int(match) for match in match.groups()]
        
        # Check partial overlap
        if elf2start <= elf1start <= elf2end or elf2start <= elf1end <= elf2end or elf1start <= elf2start <= elf1end: # Don't need to check for elf2end because in this case, one of this tests will already be true.
            fullOverlaps += 1
            
    print(fullOverlaps)

secondHalf()