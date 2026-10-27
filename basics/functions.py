def hello():
    print("Hello, World!")

hello()


def user_age_in_seconds(name, age):
    seconds = age * 365 * 24 * 60 * 60
    print(f"{name} is {seconds} seconds old.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
user_age_in_seconds(name, age)
