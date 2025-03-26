def print_ones_digit(num):
    ones_digit = num % 10
    print("The ones digit is:", ones_digit)

def main():
    user_num = int(input("Enter an integer: "))
    print_ones_digit(user_num)

if __name__ == "__main__":
    main()
