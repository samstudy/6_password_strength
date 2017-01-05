import re

def get_password_strenght(password):
    strength = 0
    if re.search(r'[0-9]',password):
        strength += 1
    if re.search(r'[A-Z]',password):
        if len(password) > 3:
            strength += 2
        if len(password) == 2:
            strength +=1
    if re.search(r'[a-z]',password):
        if len(password) > 3:
            strength += 2
        if len(password) == 2:
            strength +=1
    if len(password) > 8:
        strength +=1
    if len(password) > 12:
        strength +=2
    if re.search(r'[ !#$%&():*+,-./[\\\]^_`{|}~]', password):
        strength +=2
    return strength
        

if __name__ == '__main__':
    print('Now we will estimate your password\'s strength,1--weak... 10--strongest')
    password = input('Please input your password:')
    print('Your password\'s strength is',get_password_strenght(password))