# formula is E = m * c**2
def main():
    C :int = 299792458
    while True:
        m = float(input('Enter the mass in kg: '))
        E = m *C **2
        print('e = m * C^2...')
        print(f'm = {m}kg')
        print(f'C = {C}m/s')
        print(f'e= {E}joules of energy')
        running_condition = input('Do you want more: yes/no: ').lower()
        if running_condition not in ['yes','y']:
            print('Thanks for using')
            break
if __name__ == '__main__':
    main()
