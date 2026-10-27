def add(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}.")


add(4, 9)

# alternative lambda function syntax
add_lambda = lambda x, y: x + y
result = add_lambda(4, 9)
print(f"The sum of 4 and 9 is {result}.")

# alternative example using map
def double(x):
    return x * 2

sequence = [1, 2, 4, 8, 12]
doubled = list(map(double, sequence))
print(doubled)

# another using map with a lambda function
doubled_lambda = [x * 2 for x in sequence]
print(doubled_lambda)
