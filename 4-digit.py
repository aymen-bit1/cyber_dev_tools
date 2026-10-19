from string import digits
from itertools import product

for password in product(digits, repeat=4):
    print(password)