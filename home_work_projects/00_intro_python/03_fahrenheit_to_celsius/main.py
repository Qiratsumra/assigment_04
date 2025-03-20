print('Welcome to\033[1m Fahrenheit converter to Celsius')

def converter():
    while True:
        fehrenheit = float(input('Enter the temperature into °F: '))
        result = ((fehrenheit-32)*5)/9
        print(round(result,2))
        running = input('Do you want more.. yes/no :').lower()
        if running not in ['yes','y'] :
            print('Thanks for using !')
            break
if __name__ == '__main__':
    converter()