def main():
    count_dict = {}

    while True:
        num = int(input("Enter a number (or press Enter to stop): "))
        if num == '':
            break

        # update the count in dict
        if  num in count_dict:
            count_dict[num] +=1
        else:
            count_dict[num] = 1
        
        # Now print the results
        for key, value in count_dict.items():
            print(f"{key} appears {value} times.")

if __name__ == "__main__":
    main()