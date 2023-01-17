import random


burger = [1 ,2 ,3 ,4 , 5 , 6 , 7 , 8, 9, 10]

rand_num = random.randrange(0, 1000)

player_guess = int(input("the computer has picked a random number. try to guess what it is!! "))


    
while player_guess != rand_num:
    
    if player_guess > rand_num:
        print("the computers number is lower than your guess.")

    if player_guess < rand_num:
        print("the computers number is higher than your guess.")
    
    player_guess = int(input("Wrong. Guess again. "))

if player_guess == rand_num:
    print("you guessed the right number :D ")
