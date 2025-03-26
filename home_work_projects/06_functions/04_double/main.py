def double_number (num):
    return num*num

def main():
    user_number = int(input('Enter the number: '))
    doubleNumber = double_number(user_number)
    print('Square value is: ', doubleNumber)

if __name__ == '__main__':
    main()