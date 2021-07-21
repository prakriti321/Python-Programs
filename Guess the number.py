import random
no=random.randint(1,20)

end_game = False
lives = 9
while not end_game:

    guess =int(input("\nEnter a no. : "))
    if guess > no:
        print("Number is lesser than your guess !")
        lives-=1
        print(f"Lives left : {lives}")
    elif guess < no:
        print("Number is greater than your guess !")
        lives-=1
        print(f"Lives left : {lives}")
    elif guess == no :
        print("Congrats You guessed correct ! its ",no)
        ans = input("Do you want to play again ? 'y' for Yes, 'n' for No :- ")
        if ans == 'n':
            end_game = True
        else:
            end_game = False
            lives=9

    if lives == 0:
        print("Game Over")
        ans=input("Do you want to play again ? 'y' for Yes, 'n' for No :- ")
        if ans == 'n':
            end_game = True
        else:
            end_game = False
            lives = 9
    else:
        continue
