import math

def divide(first, second):
    if second == 0:
        result = math.inf
    else:
        result = first / second
    return result

# print(divide(4,2))
# print(divide(4,0))
