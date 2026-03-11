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

book1 = Book("Война и мир", "Лев Толстой", 1869, "978-5-17-090000-1")
book2 = Book("Анна Каренина", "Лев Толстой", 1877, "978-5-17-090000-2")
book3 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "978-5-17-090000-3")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

tolstoy_books = library.find_by_author("Толстой")  # [book1, book2]
war_books = library.find_by_title("война")          # [book1]

print(library.collection)
library.borrow_book("978-5-17-090000-1")
available = library.get_available_books()
print(library.collection)# [book2, book3]
library.return_book("978-5-17-090000-1")

print(tolstoy_books)
print(war_books)
