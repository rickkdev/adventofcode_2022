from filereader import initArrayFromFile

""" my_array = ["A Y", "B X", "C Z"]
print("my_array: ", my_array) """

array = initArrayFromFile()

# First column

# Rock
A = 1
# Paper
B = 2 
# Scissors
C = 3

# Second column
# Rock
X = 1
# Paper
Y = 2
# Scissors
Z = 3

# Round result
Lost = 0
Draw = 3
Win = 6

def calculate_pick(player1, code):

    decrypt = {
    "X": "loose",
    "Y": "draw",
    "Z": "win"
    }

    rulesToLoose = {
        "A": "Z",
        "B": "X",
        "C": "Y",
    }

    rulesToWin = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }

    rulesToDraw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    if decrypt[code] == "loose":
        return rulesToLoose[player1]
    elif decrypt[code] == "win":
        return rulesToWin[player1]
    else:
        return rulesToDraw[player1]

def rock_paper_scissors(player_1, player_2):
   
    rules = {
        "A": "Z",
        "B": "X",
        "C": "Y",
        "Z": "B",
        "X": "C",
        "Y": "A"
    }
    
    if rules[player_2] == player_1:
        return 6
    elif rules[player_1] == player_2:
        return 0
    else:
        return 3
    
result = []

choiceBonus = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

for i in array: 
    strings = i.split()
    my_pick = calculate_pick(strings[0], strings[1])
    gameResult = rock_paper_scissors(strings[0], my_pick)
    gameResult += choiceBonus[my_pick]
    result.append(gameResult)
  
print(sum(result)) 

 




