class myChoices:
    rock = "X"
    paper = "Y"
    scissors = "Z"

class elfChoices:
    rock = "A"
    paper = "B"
    scissors = "C"

win = 6
draw = 3
lost = 0
rock = 1
paper = 2
scissors = 3
score = 0

def rockChosen (score):
    match myChoice:
        case myChoices.rock:
            score = (score + rock + draw)
        case myChoices.paper:
            score = score + paper + win
        case myChoices.scissors:
            score = score + scissors + lost
    return score

def paperChosen (score):
    match myChoice:
        case myChoices.rock:
            score = score + rock + lost
        case myChoices.paper:
            score = score + paper + draw
        case myChoices.scissors:
            score = score + scissors + win
    return score

def scissorsChosen (score):
    match myChoice:
        case myChoices.rock:
            score = score + rock + win
        case myChoices.paper:
            score = score + paper + lost
        case myChoices.scissors:
            score = score + scissors + draw
    return score



day2Input = open("Day2/Day2Input.txt", "r")

for eachRound in day2Input:

    opponentChoice = eachRound[0]
    myChoice = eachRound[2]

    match opponentChoice:
        case elfChoices.rock:
            score = rockChosen(score)
        case elfChoices.paper:
            score = paperChosen(score)
        case elfChoices.scissors:
            score = scissorsChosen(score)

print("FinalScore:"+str(score))


