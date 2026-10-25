# user input
name = input("Enter your name: ")
print(name)

height = int(input("Enter the height of a box: "))
width = int(input("Enter the width of a box: "))
output = "A box with a height of {} and width of {} has an area of {}"
print (output.format(height, width, height * width))