import re
import getpass


def count_password_strenght(password):
    strength = 0
    if check_password_upper_case(password):
        strength +=2
    if check_password_lower_case(password):
        strength +=1
    if check_password_digit(password):
        strength +=1
    if check_password_symbol(password):
        strength +=1
    return strength

def count_password_length(password):
    strength = 0
    if len(password) > 8:
        strength +=1
    if len(password) > 12:
        strength +=2
    if len(password) > 16:
        strength +=2
    return strength

def get_password_strenght(password):
    return count_password_length(password) + count_password_strenght(password) 


def check_password_digit(password):
    if re.search(r'[0-9]',password):
        return True


def check_password_upper_case(password):
    if re.search(r'[A-Z]',password):
        return len(password) > 2
            

def check_password_lower_case(password):
    if re.search(r'[a-z]',password):
        return len(password) > 2
            

def check_password_symbol(password):
    if re.search(r'[!#$%&():*+,-./[\\\]^_`{|}~]',password):
        return True

def get_user_password():
    pswd=getpass.getpass('Insert your password: ') 
    return pswd



if __name__ == '__main__':
    print('Now we will estimate your password\'s strength,1--weak... 10--strongest')
    password = get_user_password()
    print('Your password\'s strength is',get_password_strenght(password))