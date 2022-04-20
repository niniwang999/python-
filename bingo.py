#make random number
#prompt to input a number between 1-20 
#if the number is greater than or less than the number, print that it is greater or less than. 
#when the correct number is guessed, print bingo 
#made by jessie wang 2022 april 17 by niniwang999@gmail.com 
#ver 1.0
#ver 1.2 april 20, added maximum attempts 
 
import random 

input_num = 0 # defines the variable  
input_attempt = 0
vresult = True  
BINGO_NUMBER = random.randint (1,20) # generates the bingo number 
print ("bingo number is: "+str(BINGO_NUMBER))
#input_num = input ("Please input a number between 1 and 20: ..") #prompts the user to choose a number 
def validateInput():
    input1 = input ("Please input a number between 1 and 20: ")
    if input1.isnumeric():   #check if the input is a number by using python isnumbric() function
        input_num = int(input1)
        if input_num > 20 or input_num < 1:
            print ("Invalidate input. ")
            return (0)  
        else:
            return (input_num)
    else:
        print ("Numbers only. ")
        return (0) 

#while input_num != BINGO_NUMBER: # loop

while True:
    input_num = validateInput() #print (input_num)
    if input_attempt > 3: 
        print ("You Lose, too many attempts")
        break 
    else: 
        input_attempt = input_attempt + 1  
        if input_num != 0:
            if input_num > BINGO_NUMBER:
                print ("Too big, try again: ")
            elif  input_num < BINGO_NUMBER:
                print ("Too small, try again: ") 
            else: 
                print ("BINGO!")
                break   
