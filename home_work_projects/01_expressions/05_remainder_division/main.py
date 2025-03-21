def main():
    while True:
        dividend = int(input('Please enter an integer to be divided: '))
        divisor = int(input('Please enter an integer to divided by: '))

        quotation  = dividend//divisor
        remainder  = dividend% divisor

        print(f'The result of this division is \033[1m{quotation} with a remainder of \033[1m{remainder}')
        running_conndition = input('Do you want more: yes/no ').lower()
        if running_conndition not in ['yes','y']:
            print('Thanks for using!')
            break

if __name__ == '__main__':
    main()