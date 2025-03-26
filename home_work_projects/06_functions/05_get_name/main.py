def get_name():
    user_name = input('Enter your name: ')
    return user_name

def main():
    name = get_name()
    print(f'Howdy! {name} 🤠')

if __name__ == '__main__':
    main()