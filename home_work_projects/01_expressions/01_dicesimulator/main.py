import random #for random dice value

def main():
    min_value= 1
    max_value = 6
    roll_dice = 'yes'

    while roll_dice == 'yes':
        print('The dice has print the following random value:')
        print(f'This random value is: {random.randint(min_value,max_value)}')

        roll_dice=input('Do you want :').lower()
        if roll_dice  not in ['yes','y']:
            print('Thanks for using!')
            break

if __name__ == '__main__':
    main()