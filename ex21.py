# ---- ex21 函数返回值 --------
def add(a,b):
    print("Adding {} + {} ".format(a,b))
    return a+b

def substract(a,b):
    print("substracting {} - {} ".format(a,b))
    return a-b

def multiply(a,b):
    print("multiplying {} * {} ".format(a,b))
    return a*b

def divide(a,b):
    print("dividing {} / {} ".format(a,b))
    return a/b

print(add(add(divide(4,2),multiply(3,4)),substract(5,6)))
