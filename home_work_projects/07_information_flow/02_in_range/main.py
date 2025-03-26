def main():
    n = int(input(' Enter a number: '))
    low =  int(input('Enter a low number: '))
    high = int(input('Enter a high number: '))
    if n >= low and n <= high:
        print(bool(1))
    
    print(bool(0))
if __name__ == '__main__':
    main()