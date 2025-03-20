print('\t \033[1m Square Converter By Qirat Saeed')

def main():
    while True:
        square_number = int(input('Enter the number to get the square value: '))
        print(square_number*square_number)
        continue_condition = input('Do you want more square values: yes/no: ').lower()
        if continue_condition not in ['yes','y']:
            print('Thanks for using!')
            break

if __name__ == '__main__':
    main()