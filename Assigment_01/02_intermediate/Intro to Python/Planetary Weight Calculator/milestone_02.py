# Milestone #2: Weight Calculator for All Planets
def main():
    earth = int(input('Enter a weight of earth: '))
    planet = input("Enter a planet: ").capitalize()
    gravitical_factor = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
    }
    if planet in gravitical_factor:
        planet_weight = round(earth * gravitical_factor[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name.")
if __name__ == '__main__':
    main()