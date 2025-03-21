def main():
    while True:
        starter_sentence = 'I learned to program and used Python to make my'
        adjective = input('Please type an adjective: ')
        noun = input('Please type a noun: ')
        verb = input('Please type a verb: ')

        print(f'\033[1m{starter_sentence} {adjective} {noun} {verb}.')
        runing_condition  = input('Do you want more: yes/no ').lower()
        if runing_condition not in  ['yes','y']:
            print('Thanks for using!')
            break

if __name__ == '__main__':
    main()