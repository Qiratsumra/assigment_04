def main():
    is_adult = 18
    user_age = int(input('Enter your age: '))
    if is_adult >= user_age:
        print(bool(1))
    else:
        print(bool(0))

if __name__ == '__main__':
    main()

