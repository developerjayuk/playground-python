def list_avg(sequence: list[int]) -> float:
    return sum(sequence) / len(sequence)


avg = list_avg([120, 20, 30])
print(avg)


class Book:
    pass


class BookShelf:
    def __init__(self, books: list[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


book1 = Book()
book2 = Book()
test = BookShelf([book1, book2])
