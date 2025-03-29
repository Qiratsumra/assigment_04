# Code for Problem 01
def main():
    fruits = ['apple','banana','orange','grape','pineapple']

    # The length of fruits is now to print
    print(f'The lenght of Fruit List is: {len(fruits)}')

    # Now Add the mango in the last of the list
    fruits.append('mango')

    # Now Print the updated list
    print(f'Updated fruits list is {fruits}')

# Code for Problem 02
def play_indexing_game():
    # Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.
    mix_list = ['Apple',30,'Realme C21']

    while True:
        print("\n Mix List:", mix_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        user_choice =  int(input('Enter your choice: '))

        if user_choice == 1:
            try:
                index = int(input('Enter index number to acccess indexing is starts with 0'))
                print(mix_list[index])
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif user_choice == 2:
            try:
                index = int(input('Enter the modify index nuimber: '))
                new_value = input('Enter a new value: ')
                updated_value = mix_list[index]
                updated_value = new_value
                print(f'Updated value is {updated_value}')
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif user_choice == 3:
            try:
                start = int(input('Enter the starting index: '))
                end = int(input('Enter the ending index value: '))
                slice_list = mix_list[start:end]
                print(f'Sliced list is {slice_list}')
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif  user_choice == 4:
            print('Exiting the game.......')
            break
        else:
            print('Invalid Choice')

if __name__ == '__main__':
    main()
    play_indexing_game()