import random
import string

def password_generator(length=11):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

user_length = int(input('Enter the lenght of the password!: '))
password = password_generator(user_length)
print(f'\'{password}\': Generated password')