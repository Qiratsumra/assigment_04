def main():
    # Create empyty dictionary
    contacts = {}

    while True:
        print('\n Contact Books')
        print('1. Create Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Search Contact')
        print('6. Count Contact')
        print('7. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:  # Create Contact
            name = input('Enter name: ')
            if name in contacts:
                print(f'\033[1m{name} Contact already exists')
            else:
                age = input('Enter age: ')
                email = input('Enter email: ')
                phone = input('Enter phone: ')
                contacts[name]= {'age': int(age), 'email': email, 'phone': phone}
                print(f'\033[1m {name} Contact created successfully')
        elif choice == 2: # View Contact
            name = input('Enter name: ')
            if name in contacts:
                contact = contacts[name]
                print(f'Name: {name}')
                print(f'Age: {contact["age"]}')
                print(f'Email: {contact["email"]}')
                print(f'Phone: {contact["phone"]}')
            else:
                print(f'\033[1m{name} Contact does not exists')
        elif choice == 3: # Update Contact
            name = input('Enter name: ')
            if name in contacts:
                age = input('Enter age: ')
                email = input('Enter email: ')
                phone = input('Enter phone: ')
                contacts[name]= {'age': int(age), 'email': email, 'phone': phone}
                print(f'\033[1m{name} Contact updated successfully')
            else:
                print(f'\033[1m{name} Contact does not exists')
        elif choice ==4 : # Delete Contact
            name = input('Enter name: ')
            if name in contacts:
                del contacts[name]
                print(f'\033[1m{name} Contact deleted successfully')
            else:
                print(f'\033[1m{name} Contact does not exists')
        elif choice == 5: # Search Contact
            search_name = input('Enter name to search: ')
            found = False
            for name, contact in contacts.items():
                if search_name.lower() in name.lower():
                    print(f'Name: {name}')
                    print(f'Age: {contact["age"]}')
                    print(f'Email: {contact["email"]}')
                    print(f'Phone: {contact["phone"]}')
                    found = True
            if not found:
                print(f'\033[1m{search_name} Contact does not exists')
        elif choice == 6: # Count Contact
            print(f'Total contact in your phone book : {len(contacts)}')
        
        elif choice == 7:
            print('Closed the phone books')
            break
        else:
            print('Invalid input')

if __name__ == '__main__':
    main()