import re


def estimate_weight(password):
    weight = ''.join(password)
    count = len(weight)
    if weight.islower():
        if count == 3:
            return 1
        if count > 3:
            return 2
        else:
            return 0
    if weight.isupper():
        if count == 3:
            return 1
        if count > 3:
            return 2
        else:
            return 0
    else:
        if count == 1:
            return 1
        if count > 1:
            return 2
        else:
           return 0

        
def check_password_uppercase(password):
    upper_case = re.findall(r'[A-Z]',password)
    return estimate_weight(upper_case)


def check_password_digit(password):
    digits = re.findall(r'[0-9]',password)
    return estimate_weight(digits)

def check_password_symbol(password):
    symbol = re.findall(r'[!#$%&():*+,-./[\\\]^_`{|}~]',password)
    return estimate_weight(symbol)


def check_password_lowercase(password):
    lower_case = re.findall(r'[a-z]',password)
    return estimate_weight(lower_case) 


def check_password_length(password):
    if len(password) > 6:
        return 1
    if len(password) > 12:
        return 2
    else:
        return 0


def get_password_strenght(password):
    count_lower_case = check_password_lowercase(password)
    count_upper_case = check_password_uppercase(password)
    count_length = check_password_length(password)
    count_digits = check_password_digit(password)
    count_symbols = check_password_symbol(password)
    return  count_upper_case + count_lower_case + count_length + count_digits + count_symbols
    
    
        

if __name__ == '__main__':
    print('Now we will estimate your password\'s strength,1--weak... 10--strongest')
    password = input('Please input your password:')
    print('Your password\'s strength is',get_password_strenght(password))
