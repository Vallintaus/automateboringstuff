import time
import sys

sys.set_int_max_str_digits(500000)

def calcProd():
    # Calculate the product of the first 100 000 numbers
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f"The result is {len(str(prod))} digits long and it took {endTime - startTime} seconds to calculate")