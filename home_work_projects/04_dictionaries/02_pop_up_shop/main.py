def main():
    fruits = {'apple': 1.5,'mango': 5, 'banana':2.5, 'orange':3}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name] # get the fruits price value
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    print("Your total is $" + str(total_cost))


if __name__ == '__main__':
    main()