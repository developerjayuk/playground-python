class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("The Lord of the Rings")
book2 = Book("Wuthering Heights")

shelf = BookShelf(book1, book2)
books = [str(book) for book in shelf.books]

print(shelf)
print(books)
