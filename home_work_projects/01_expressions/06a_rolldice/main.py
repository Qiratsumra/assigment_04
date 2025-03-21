import random
def main():
    while True:
        num_sides: int = 6
        die1: int = random.randint(1, num_sides)
        die2: int = random.randint(1, num_sides)
        total: int = die1 + die2
        print("Dice have", num_sides, "sides each.")
        print("First die:", die1)
        print("Second die:", die2)
        print("Total of two dice:", total)

        running_condition = input('Do you want more yes/no: ').lower()
        if running_condition not in ['yes','y']:
            print('Thanks for using! ')
            break
if __name__ == '__main__':
    main()
