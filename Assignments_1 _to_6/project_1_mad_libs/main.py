print("Welcome to \033[1mMad Libs! Let's create a fun story.")

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
animal = input("Enter an animal: ")
exclamation = input("Enter an exclamation: ").capitalize()
adverb = input("Enter an adverb: ")

story = f'''
One {adjective1} morning, a {noun1} decided to {verb1} to the park. 
On the way, it encountered a {animal} wearing a hat. 
"{exclamation}!" shouted the {animal}. "You're {verb1}ing all wrong!"\n
The {noun1} replied, "I'm just trying to like usual!" 
Suddenly, they both heard a loud noise from above. 
They looked up and saw a {adverb} dancing cloud!\n
They spent the rest of the daying together, 
proving that even a {noun1} and {animal} can be friends.
'''

print("\nYour Mad Lib Story:\n")
print(f'\033[1m{story}')