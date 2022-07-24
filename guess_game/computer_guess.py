"""
    Python program to guess a secret number that the computer has picked from a range of number at random. If the guess of the user is too low or too high we use inform the user that its too low, too high or out of range.
"""
import random

def start(min, max):
    secret_number=random.randint(min, max)
    lifes=5
    trials=0
    while lifes!=0:
        trials+=1
        lifes-=1
        try:
            guess=int(input("guess: "))
        except ValueError:
            print("An error occured..enter an integer")
            continue
        if guess > max:
            print("==>Number out of ranger...Quite High")
        elif guess < min:
            print("==>Number out of ranger...Quite Low")
        elif guess > secret_number:
            print("==>Number too high, guess again!")
        elif guess < secret_number:
            print("==>Number too low guess try again!")
        
        
        else:
            print(f"Hurray, you got the secret number {secret_number}, in {trials} trials")
            break
        print(f"==>You have {lifes} trials left")
    else:
        print(f"GAMEOVER....The secret number was {secret_number}")
        
def main():
    MIN_=1
    MAX_=2
    start(MIN_, MAX_)
    while True:
        print("Do you want to play again?(y/n)")
        choice=input(">>> ")
        if choice=="y":
            start(MIN_, MAX_)
        elif choice=="n":
            break
        else:
            print("Wrong Input...")
            continue
main()