import random 

WINNING_SCORE = 20
while score < WINNING_SCORE:
    roll = random.randint (1,6)
    print ("You rolled a", roll)

    if roll == 1:
        print ("You Lose") 
        score = 0
        break
    else:
        score += roll
        if score < WINNING_SCORE:
            c = input ("Do you want to continue? y/n") 
            if c == "n" or c == "N":
                break
if score > WINNING_SCORE: 
    print ("You Win") 
print ("Score:", score)