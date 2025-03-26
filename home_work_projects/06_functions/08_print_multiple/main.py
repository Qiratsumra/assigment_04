def mutiple_message (message, repeats):
    for i in range(repeats):
        print(message)

def main():
    message = input('Enter your message: ')
    repeats = int(input('How many times you do want to repeat your message: '))
    mutiple_message(message,repeats)

if __name__ == '__main__':
    main()