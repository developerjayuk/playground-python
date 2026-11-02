a: list = []
b: list = a

a.append(1)

print(id(a))  # Output: <some memory address>
print(id(b))  # Output: <same memory address as a>
