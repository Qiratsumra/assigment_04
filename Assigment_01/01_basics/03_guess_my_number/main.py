import random
def main():
    print('Welcome to \"Number Guessing\" Game')

    number = random.randint(1,100)
    while True : 
        guess = int(input('Enter the number from 1 to 100: '))
        if guess<number:
            print('To low Number')
        elif number <guess:
            print('To hight number')
        else:
            print('You win!')
            break
if __name__ == '__main__':
    main()