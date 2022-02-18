#Password Generator

'''
symbols, numbers, alpha
create 12 character passwords with a random combination of these characters.
'''

import random

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+","-", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", ")"]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

### BUILD THE 12 CHARACTER PASSWORD ###
sym = random.sample(range(0, len(symbols)), 4) #get 4 symbols
abc = sym = random.sample(range(0, len(alpha)), 4) #get 4 letters
num = sym = random.sample(range(0, len(numbers)), 4) #get 4 numbers


sy = [symbols[sym[0]], symbols[sym[1]], symbols[sym[2]], symbols[sym[3]]]
al = [alpha[abc[0]], alpha[abc[1]], alpha[abc[2]], alpha[abc[3]]]
nu = [numbers[num[0]], numbers[num[1]], numbers[num[2]], numbers[num[3]]]

p = (sy + al + nu)

random.shuffle(p) #shuffle the password

print("Your Password:", "".join(map(str, p))) 