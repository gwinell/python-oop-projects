class Book:
    def __init__(self, title, author, year, isbn, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"{self.title} {self.author} {self.year} {self.isbn} {self.is_available}"

    def __repr__(self):
        return f'"{self.title}":{self.author}'


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        if 'Book' not in str(type(book)):
            raise TypeError("Не является книгой")
        self.collection.append(book)

    def remove_book(self, target_isbn):
        self.collection.remove(next((book for book in self.collection if book.isbn == target_isbn), None))

    def find_by_title(self, target_title):
        return list(filter(lambda book: target_title.lower() in book.title.lower(), self.collection))

    def find_by_author(self, target_author):
        return list(filter(lambda book: target_author.lower() in book.author.lower(), self.collection))

    def get_available_books(self):
        return list(filter(lambda book: book.is_available == True, self.collection))

    def borrow_book(self, target_isbn):
        for book in self.collection:
            if (book.isbn == target_isbn) and (book.is_available == True):
                book.is_available = False
                return "Выдано успешно"
            elif (book.isbn == target_isbn) and (book.is_available == False):
                raise ValueError("Книга уже выдана")
        raise KeyError("Книга не найдена")

    def return_book(self, target_isbn):
        for book in self.collection:
            if (book.isbn == target_isbn) and (book.is_available == False):
                book.is_available = True
                return "Выдано успешно"
            elif (book.isbn == target_isbn) and (book.is_available == True):
                raise ValueError("Книга не была выдана")
        raise KeyError("Книга не найдена")

