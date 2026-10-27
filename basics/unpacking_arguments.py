def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(2, 3, 4))  # Output: 24


def add(x, y):
    return x + y


nums = (5, 10)
print(add(*nums))  # Output: 15


nums_dict = {"x": 7, "y": 3}
print(add(**nums_dict))  # Output: 10


def apply(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(*args)
    else:
        return "Not a valid operator"


print(apply(1, 2, 3, operator="+"))  # Output: 6
print(apply(2, 3, 4, operator="*"))  # Output: 24
