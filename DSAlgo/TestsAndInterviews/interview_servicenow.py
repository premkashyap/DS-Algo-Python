from functools import reduce 
from operator import mul
from Stack import *

def maximum_product_of_adjacentn(lst, n):
    product=reduce(mul, lst[:n])
    global_max_product = product
    offset = 1
    for i in range(n, len(lst)):
        offset*=lst[i-n]
        product*=lst[i]
        current_product= product/offset
        if current_product>global_max_product:
            global_max_product=current_product
    return global_max_product

def validate_braces(expression):
    stack = []
    braces = {'{':'}', '(':')', '[':']'}
    for ch in expression:
        if ch in braces.keys():
            stack.append(ch)
        elif ch in braces.values():
            if len(stack) > 0 and braces[stack.pop()] == ch:
                continue
            else:
                return False
        else:
            return False
    return True if stack == [] else False
                






if __name__ == '__main__':
    #print(maximum_product_of_adjacentn([5,2,1,6,3], 2))
    print(validate_braces('{[(4)]}'))
