def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


grades: list[int] = [1, 89, 65]

print("Welcome to the average grade problem")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("All calculations have been done")
