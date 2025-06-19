import random

rounds_played = 0
enemy_win = 0
user_win = 0
choices = ["rock","paper","scissors"]
rounds = 0


#ask user how many rounds they want to play
rounds = int(input("How many rounds to you want to play? "))


#function to get and verify choices
def get_choices():
    global user_choice
    global opponent_choice
    user_choice = int(input("Choose your choice\n\n1. Rock\n2. Paper\n3. Scissors\n\n"))

    if not isinstance(user_choice, int):
        user_choice = input("Please select your choice with a number only\n\n1. Rock\n2. Paper\n3. Scissors\n\n")
    else:
        print("You have selected: " + choices[user_choice - 1].capitalize())
        opponent_choice = random.choice(choices)
        print("The enemy has selected: " + opponent_choice.capitalize())


#gameloop
for i in range(rounds-1): 
    get_choices()
    
    if choices[user_choice-1] == opponent_choice :
        print("Draw!")
        rounds_played = rounds_played + 1
    elif (choices[user_choice - 1] == "rock" and opponent_choice == "scissors") or \
         (choices[user_choice - 1] == "paper" and opponent_choice == "rock") or \
         (choices[user_choice - 1] == "scissors" and opponent_choice == "paper"):
        
        print("You win!")
        rounds_played = rounds_played + 1
        user_win = user_win + 1
        print("You have played " + str(rounds_played) + " rounds!")
        print("Current result: " + str(user_win) + ":" + str(enemy_win))
    else:
        print("You lose!")
        rounds_played = rounds_played + 1
        enemy_win = enemy_win + 1
        print("You have played " + str(rounds_played) + " rounds!")
        print("Current result: " + str(user_win) + ":" + str(enemy_win))

### add maximum amount of rounds to be played
### verify that user can only enter integers
### add winning screen
### improve gameloop print text
