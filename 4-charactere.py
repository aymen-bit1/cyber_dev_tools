from string import ascii_letters, digits, punctuation
from itertools import product

for password in product(ascii_letters + digits + punctuation, repeat=4):
    print(password)
    
