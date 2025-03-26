def is_odd(value: int):
    
    remainder = value % 2  
    return remainder == 1

def main():
    for i in range(1,11):
        if is_odd(i):
            print(f'{i} odd')
        else:
            print(f'{i} even')

if __name__ == '__main__':
    main()