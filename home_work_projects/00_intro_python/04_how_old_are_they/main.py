print('Welcome to\033[1m Age-Related Riddle!')
def main():
    anthon :int = 21
    beth :int = 6 + anthon
    chen :int = 20 + beth
    drew :int = chen +anthon
    ethan :int = chen

    print(f'''Anthon is {anthon} years old.\nBeth is {beth} years old.\nChen is {chen} years old.\nDrew is {drew} years old.\nEthan is {ethan} years old.
''')

if __name__ == '__main__':
    main()