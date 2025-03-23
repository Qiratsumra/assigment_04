import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess  = int(input(f"Guess a number from between 1 aand {x}: "))
        if guess<random_number :
            print('Sorry , guess again. To low')
        elif random_number<guess :
                   print('Sorry , guess again. To high')
    print(f'Congrats, You have guessed the number {random_number} correctly!')               
guess(10)