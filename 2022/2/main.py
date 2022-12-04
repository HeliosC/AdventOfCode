import re

REGEX = r"([A-C]) ([X-Z])"
INPUT = open("2022/2/input.txt", "r")

OPPONENT_INPUTS = ['A', 'B', 'C']
USER_INPUTS = ['X', 'Y', 'Z']

def firstHalf():
    totalPoints = 0
    while line := INPUT.readline():
        match = re.search(REGEX, line)
        (opponentInout, userInput) = match.groups()
        opponentIndex = OPPONENT_INPUTS.index(opponentInout)
        userIndex = USER_INPUTS.index(userInput)

        playPoints = userIndex + 1 
        # 1 point for X (Rock), 2 for Y, 3 for Z
        
        versusPoint = 3 * (((userIndex - opponentIndex + 1) ))
        # (userIndex - opponentIndex) gives the winner because Rock < Paper < Scissor < Rock
        # So if userIndex - opponentIndex = 1, I won (I played the next item in the above list). 0 is a deuce, -1 I lose
        # We do +1 so that lose = 0, deuce = 1, win 2
        # % 3 to avoid negative results
        # and * 3 so lose = 0, deuce = 3, win = 6
        
        totalPoints += (playPoints + versusPoint)

    print(totalPoints)

def secondHalf():
    totalPoints = 0
    while line := INPUT.readline():
        match = re.search(REGEX, line)
        (opponentInout, matchResult) = match.groups()
        opponentIndex = OPPONENT_INPUTS.index(opponentInout)
        resultIndex = USER_INPUTS.index(matchResult)

        playPoints = (opponentIndex + (resultIndex - 1)) % 3 + 1
        # As sown above, if I want to win I need to play the next index played by the opponent
        # As resultIndex = 2 for a win (Z), (resultIndex - 1) = 1 for a win, 0 for a deuce, -1 for a lose
        # So (opponentIndex + (resultIndex - 1)) % 3 give what to play: 0 = rock, 1 = paper, 2 = scissor
        # And + 1 because we want 1 point for rock, 2 for paper, 3 for scissor
        
        versusPoint = resultIndex * 3
        # We want: lose (X) = 0, deuce (Y) = 3, win (Z) = 6
        # And index X = 0, index Y = 1, index Z = 2

        totalPoints += (playPoints + versusPoint)

    print(totalPoints)

secondHalf()