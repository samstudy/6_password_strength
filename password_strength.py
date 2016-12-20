import re

def check_password_uppercase(password):
    upper_case = len(re.findall(r'[A-Z]',password))
    if upper_case == 1:
        return 1
    if upper_case > 1:
        return 2

def check_password_lowercase(password):
    lower_case = len(re.findall(r'[a-z]',password)) 
    if lower_case == 1:
        return 1
    if lower_case > 1 :
        return 2 

def check_password_length(password):
    if len(password) > 6:
        return 1
    if len(password) > 12:
        return 2

def check_password_digit(password):
    digits = len(re.findall(r'[0-9]',password))
    if digits == 2:
        return 1
    if digits > 2:
        return 2
def check_password_symbol(password):
    symbol = len(re.findall(r'[!#$%&():*+,-./[\\\]^_`{|}~]',password))
    if symbol == 1:
        return 1
    if symbol > 2:
        return 2

def get_password_strenght(password):
    count_lower_case = check_password_lowercase(password)
    count_upper_case = check_password_uppercase(password)
    count_length = check_password_length(password)
    count_digits = check_password_digit(password)
    count_symbols = check_password_symbol(password)
    strength = count_upper_case + count_lower_case + count_length + count_digits + count_symbols
    return strength
        

if __name__ == '__main__':
    print('Now we will estimate your password\'s strength,1--weak... 10--strongest')
    password = input('Please input your password:')
    print('Your password\'s strength is',get_password_strenght(password))