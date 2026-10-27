def named(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


named(name="Alice", age=30, city="New York", occupation="Engineer")


# another example of unpacking keyword arguments
def both(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


both(1, 2, 3, name="Alice", age=30, city="New York", occupation="Engineer")
