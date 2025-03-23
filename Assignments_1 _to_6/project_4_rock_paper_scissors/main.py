import random
options = ('rock','paper','scissors')
player = None
running = True

player_Name = input('Enter your name: ')
while running:
    while player not in options:
        player = input('''
Enter a valid choice
1. rock
2. paper
3. scissors
''').lower()

    computer = random.choice(options)
    print(f"{player_Name}'s choice is : {player}")
    print(f"Computer's choice is : {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        print(f'{player_Name} you win!')
    else:
        print(f'You Lose! {player_Name}')

    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        print('Thanks for using!')
        break