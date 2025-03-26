def main():
    user_number = int(input('Enter the number: '))
    while user_number<=100:
        print(user_number,end='  ')
        user_number *=2
    print(user_number)

if __name__ == '__main__':
    main()