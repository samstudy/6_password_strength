import re

def get_password_strenght(password):
    strength = 0
    if check_password_upper_case(password):
        strength +=2
    if check_password_lower_case(password):
        strength +=1
    if check_password_digit(password):
        strength +=1
    if check_password_symbol(password):
        strength +=1
    if len(password) > 8:
        strength +=1
    if len(password) > 12:
        strength +=2
    if len(password) > 16:
        strength +=2
    return strength




def check_password_digit(password):
    if re.search(r'[0-9]',password):
        return True

def check_password_upper_case(password):
    if re.search(r'[A-Z]',password):
        if len(password) >2:
            return True
        else:
            return False

def check_password_lower_case(password):
    if re.search(r'[a-z]',password):
        if len(password) >2:
            return True
        else:
            return False
def check_password_symbol(password):
    if re.search(r'[!#$%&():*+,-./[\\\]^_`{|}~]',password):
        return True


if __name__ == '__main__':
    print('Now we will estimate your password\'s strength,1--weak... 10--strongest')
    password = input('Please input your password:')
    print('Your password\'s strength is',get_password_strenght(password))