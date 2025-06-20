import random



rounds_played = 0
enemy_win = 0
user_win = 0
choices = ["rock","paper","scissors"]
emoji = [" 🗿"," 📄"," ✂️"]
rounds = 0



def get_choices():
    global user_choice
    global opponent_choice

    user_choice = input("Choose your choice\n\n1. Rock\n2. Paper\n3. Scissors\n\n")

    if user_choice.isdigit() == True and int(user_choice) > 0 and int(user_choice) < 4:
        user_choice = int(user_choice)
        print("You have selected: " + choices[user_choice - 1].capitalize() + emoji[user_choice - 1])
        opponent_choice = random.choice(choices)
        print("The enemy has selected: " + opponent_choice.capitalize() + emoji[choices.index(opponent_choice)])
    else:
        print("Please select a valid choice only!")
        get_choices()



def start_game():
    global rounds

    rounds = input("How many rounds to you want to play? ")

    if rounds.isdigit() == True and int(rounds) > 0:
        rounds = int(rounds)
        print("You have selected to play " + str(rounds) + " rounds!")
        gameloop()
    else:
        print("Please select a valid number of rounds")
        start_game()



def gameloop():
    for i in range(rounds): 
        global enemy_win 
        global user_win
        global rounds_played

        get_choices()

        if choices[user_choice-1] == opponent_choice :
            print("Draw! 🔄")
            rounds_played += 1
        elif (choices[user_choice - 1] == "rock " and opponent_choice == "scissors") or \
            (choices[user_choice - 1] == "paper" and opponent_choice == "rock") or \
            (choices[user_choice - 1] == "scissors" and opponent_choice == "paper"):
            
            print("You win! ✔️")
            rounds_played += 1
            user_win += 1
            print("You have played " + str(rounds_played) + " rounds!")
            print("Current result: " + str(user_win) + ":" + str(enemy_win))
        else:
            print("You lose! ❌")
            rounds_played += 1
            enemy_win += 1
            print("You have played " + str(rounds_played) + " rounds!")
            print("Current result: " + str(user_win) + ":" + str(enemy_win))



start_game()