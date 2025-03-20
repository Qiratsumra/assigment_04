print('\033[1m Agreement Bot By Qirat')

def main_bot():
    user_animal = input('Enter your favorite animal is: ')
    favorite =  f'My Favorite animal is also \033[3m{user_animal} .'
    print(favorite)

if __name__ == '__main__':
    main_bot()