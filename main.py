import random

weapons = ["rock","paper","scissors"]

user_weapon = int(input("Choose your weapon\n\n1. Rock\n2. Paper\n3. Scissors\n\n"))

if not isinstance(user_weapon, int):
    user_weapon = input("Please select your weapon with a number only\n\n1. Rock\n2. Paper\n3. Scissors\n\n")
else:
    print("You have selected: " + weapons[user_weapon - 1].capitalize())
    weapon = random.choice(weapons)
    print("The enemy has selected: " + weapon.capitalize())


rounds_played = 0
enemy_win = 0
user_win = 0



for i in range(5): #Problem Area - it should allow the user & enemy to re-select their choices - currently it runs the for loop x amount in range() - call a function maybe?
        
    if weapons[user_weapon-1] == weapon :
        print("Draw!")
        rounds_played = rounds_played + 1
    elif (weapons[user_weapon - 1] == "rock" and weapon == "scissors") or \
         (weapons[user_weapon - 1] == "paper" and weapon == "rock") or \
         (weapons[user_weapon - 1] == "scissors" and weapon == "paper"):
        
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
