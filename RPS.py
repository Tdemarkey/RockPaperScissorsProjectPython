import random

#make variables for each individual win
user_score = 0
computer_score = 0

#Set rock paper and scissors
rps = ["rock", "paper", "scissors"]

#create our while loop
while True:
    #ask user for an input
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()  
    #create our terminate input
    if user_input == "q":
        break

    if user_input not in rps:
        continue
    
    #ask for random number
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    #make computer pick and print
    computer_pick = rps[random_number]
    print("Computer picked", computer_pick + ".")

    #make the scoring algorithm
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1

    else:
        print("You lost!")
        computer_score += 1


#print end of game
print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
print("Goodbye!")