# string formatting
name = "Jason"
greeting = f"Hello, {name} from f string"
print(greeting)

longer_intro = "Hello {}. Today is {}."
formatted = longer_intro.format("Jason", "Friday")
print(formatted)