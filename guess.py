import random

def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no:
        guess = int(input(f"Guess number between 1 to {x}: "))
        if guess < random_no:
            print(f"Sorry, the guess number is too low: ")
        elif guess > random_no:
            print(f"Sorry, the guess number is too high: ")
    
    print(f"Ohoo, you hit the jackpot its {random_no}")
    
#guess(25)

def computer_guess(x):
    low =1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f" Hey, Is {guess} is too High (H), too Low (L) , is it correct (C)").lower()
        
        if feedback == 'h':
            guess = guess - 1
        elif feedback == ' l':
            guess = guess +1
    print(f"Yay, computer guess the correct number {guess}")
computer_guess(400)