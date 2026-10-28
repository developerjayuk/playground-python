class Book:
    TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in Book.TYPES:
            raise ValueError(
                f"Invalid book type: {book_type}. Must be one of {Book.TYPES}."
            )
        self.book_type = book_type

    def __repr__(self):
        return f"<Book title={self.title!r}, book_type={self.book_type!r}>"

    @classmethod
    def hardcover(cls, title):
        return cls(title, cls.TYPES[0])

    @classmethod
    def paperback(cls, title):
        return cls(title, cls.TYPES[1])

    @classmethod
    def ebook(cls, title):
        return cls(title, cls.TYPES[2])


print(Book.TYPES)  # Output: ('hardcover', 'paperback', 'ebook')


# book = Book("The Great Gatsby", "will fail")
hard = Book.hardcover("The Great Gatsby")
paper = Book.paperback("To Kill a Mockingbird")

print(hard)  # Output: <Book title='The Great Gatsby', book_type='hardcover'>
print(paper)  # Output: <Book title='To Kill a Mockingbird', book_type='paperback'>
