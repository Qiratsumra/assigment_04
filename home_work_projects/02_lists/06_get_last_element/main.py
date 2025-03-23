def main(lst):
    print(lst[-1]) 

n = int(input("Enter the number of elements in the list: "))
user_list = [input(f"Enter element {i+1}: ") for i in range(n)]

# Calling the function
main(user_list)
