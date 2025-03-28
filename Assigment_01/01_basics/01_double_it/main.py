def main():
    user_num = int(input('Enter a number: '))
    while user_num <100:
        user_num*=2
        print(f'Doubled value is: {user_num}')
    print("Final value reached 100 or more. Program terminated.")

if __name__ == '__main__':
    main()