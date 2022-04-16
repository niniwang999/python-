# this is a python code that runs a dice game called pig. for school hw 
#ver. 0.1 2022 april 16 
# by jessie wang, niniwang999@gmail.com 
import random #it imports a random function 

score = 0
WINNING_SCORE = 20
while score < WINNING_SCORE: #a loop that makes it so that hen your score is less than the winning score, which you detrimeint aboeve, it does stuff. 
    roll = random.randint (1,6) # this is defining the variable roll which makes it choose a random integer between 1 and 6 inclusive. 
    print ("You rolled a", roll) # after you roll the number gets printed. 

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
