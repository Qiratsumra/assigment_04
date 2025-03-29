# Milestone #1: Mars Weight Calculator
def main():
    earth = int(input('Enter a weight of earth: '))
    mars_weight = round(earth * 0.378, 2)
    print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == '__main__':
    main()