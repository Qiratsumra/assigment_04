import random

def main():
    secret = random.randint(1,50)
    while True:
        user_guess = int(input('Guessed the number from 1 to 50: '))
        if user_guess != secret:
            if user_guess> secret:
                print('TOO High!')
            elif user_guess< secret:
                print('TOO Low!')
        else:
            print('Great you Guessed the correct number')
            break


if __name__ == '__main__':
    main()