print('\t \033[1m Calculator App By Qirat Saeed')

def calculator(num1,num2,operator):
    
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '/':
        if num2>0:
            result = num1 /num2
        else:
            return 'Zero Divison Error'
    elif operator == '*':
        result = num1*num2
    return f'Answer: \033[1m{result}'

num1 =float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
operator = input("Enter the operator:['+','-','/','*']: ")
print(calculator(num1,num2,operator))