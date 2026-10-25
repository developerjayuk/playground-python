friends = ["Ted", "Bonnie", "Claire"]
print("Jen" in friends)
print("Ted" in friends)

classic_books = {"harry potter", "lord of the rings", "bible"}

user_book = input("What was the last book you read: ").lower()

if user_book in classic_books:
    print("That is one of the classic books")
else:
    print("Not one of the classics")
    
    
