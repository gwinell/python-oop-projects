import unittest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.library import Book, Library


class TestBook(unittest.TestCase):
    """Тесты класса Book."""

    def test_creation(self):
        """Книга создаётся с правильными атрибутами."""
        book = Book("Война и мир", "Лев Толстой", 1869, "978-5-17-090000-1")
        self.assertEqual(book.title, "Война и мир")
        self.assertEqual(book.author, "Лев Толстой")
        self.assertEqual(book.year, 1869)
        self.assertEqual(book.isbn, "978-5-17-090000-1")

    def test_is_available_default(self):
        """Книга доступна по умолчанию."""
        book = Book("Тест", "Автор", 2000, "123")
        self.assertTrue(book.is_available)

    def test_str_contains_title(self):
        """__str__() содержит название книги."""
        book = Book("Уникальное Название", "Автор", 2000, "123")
        self.assertIn("Уникальное Название", str(book))

    def test_str_contains_author(self):
        """__str__() содержит автора."""
        book = Book("Название", "Уникальный Автор", 2000, "123")
        self.assertIn("Уникальный Автор", str(book))


class TestBookToDict(unittest.TestCase):
    """Тесты дополнительного задания: to_dict() для Book."""

    def test_to_dict_contains_all_fields(self):
        """to_dict() содержит все поля книги."""
        book = Book("Тест", "Автор", 2000, "isbn-123")
        data = book.to_dict()
        self.assertIn('title', data)
        self.assertIn('author', data)
        self.assertIn('year', data)
        self.assertIn('isbn', data)
        self.assertIn('is_available', data)

    def test_to_dict_values(self):
        """to_dict() возвращает правильные значения."""
        book = Book("Война и мир", "Лев Толстой", 1869, "isbn-1")
        data = book.to_dict()
        self.assertEqual(data['title'], "Война и мир")
        self.assertEqual(data['author'], "Лев Толстой")
        self.assertEqual(data['year'], 1869)
        self.assertEqual(data['isbn'], "isbn-1")
        self.assertTrue(data['is_available'])

    def test_to_dict_borrowed_book(self):
        """to_dict() отражает статус выданной книги."""
        book = Book("Тест", "Автор", 2000, "isbn-123")
        book.is_available = False
        data = book.to_dict()
        self.assertFalse(data['is_available'])


class TestLibraryBasic(unittest.TestCase):
    """Базовые тесты Library."""

    def setUp(self):
        """Создание тестовых данных."""
        self.book1 = Book("Война и мир", "Лев Толстой", 1869, "isbn-1")
        self.book2 = Book("Анна Каренина", "Лев Толстой", 1877, "isbn-2")
        self.book3 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "isbn-3")
        self.library = Library()

    def test_empty_library(self):
        """Новая библиотека пуста."""
        self.assertEqual(len(self.library.get_available_books()), 0)

    def test_add_book(self):
        """add_book() добавляет книгу."""
        self.library.add_book(self.book1)
        available = self.library.get_available_books()
        self.assertEqual(len(available), 1)
        self.assertIn(self.book1, available)

    def test_add_multiple_books(self):
        """Добавление нескольких книг."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.assertEqual(len(self.library.get_available_books()), 3)

    def test_add_non_book_raises(self):
        """Добавление не-Book вызывает TypeError."""
        with self.assertRaises(TypeError):
            self.library.add_book("не книга")

    def test_add_duplicate_isbn_raises(self):
        """Добавление книги с существующим ISBN вызывает ValueError."""
        self.library.add_book(self.book1)
        duplicate = Book("Другая", "Другой", 2000, "isbn-1")
        with self.assertRaises(ValueError):
            self.library.add_book(duplicate)

    def test_remove_book(self):
        """remove_book() удаляет книгу."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.remove_book("isbn-1")
        available = self.library.get_available_books()
        self.assertEqual(len(available), 1)
        self.assertNotIn(self.book1, available)

    def test_remove_nonexistent_raises(self):
        """Удаление несуществующей книги вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.library.remove_book("несуществующий-isbn")


class TestLibrarySearch(unittest.TestCase):
    """Тесты поиска."""

    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("Война и мир", "Лев Толстой", 1869, "isbn-1"))
        self.library.add_book(Book("Анна Каренина", "Лев Толстой", 1877, "isbn-2"))
        self.library.add_book(Book("Преступление и наказание", "Фёдор Достоевский", 1866, "isbn-3"))
        self.library.add_book(Book("Мир как воля", "Артур Шопенгауэр", 1818, "isbn-4"))

    def test_find_by_title_exact(self):
        """Поиск по точному названию."""
        results = self.library.find_by_title("Война и мир")
        self.assertEqual(len(results), 1)

    def test_find_by_title_partial(self):
        """Частичное совпадение названия."""
        results = self.library.find_by_title("мир")
        self.assertEqual(len(results), 2)  # "Война и мир" и "Мир как воля"

    def test_find_by_title_case_insensitive(self):
        """Поиск без учёта регистра."""
        results = self.library.find_by_title("ВОЙНА")
        self.assertEqual(len(results), 1)

    def test_find_by_title_no_results(self):
        """Поиск без результатов возвращает пустой список."""
        results = self.library.find_by_title("Несуществующая книга")
        self.assertEqual(results, [])

    def test_find_by_author_exact(self):
        """Поиск по автору."""
        results = self.library.find_by_author("Лев Толстой")
        self.assertEqual(len(results), 2)

    def test_find_by_author_partial(self):
        """Частичное совпадение автора."""
        results = self.library.find_by_author("Толстой")
        self.assertEqual(len(results), 2)

    def test_find_by_author_case_insensitive(self):
        """Поиск автора без учёта регистра."""
        results = self.library.find_by_author("толстой")
        self.assertEqual(len(results), 2)

    def test_find_by_author_no_results(self):
        """Поиск несуществующего автора."""
        results = self.library.find_by_author("Пушкин")
        self.assertEqual(results, [])


class TestLibraryBorrow(unittest.TestCase):
    """Тесты выдачи и возврата."""

    def setUp(self):
        self.library = Library()
        self.book = Book("Тест", "Автор", 2000, "isbn-test")
        self.library.add_book(self.book)

    def test_borrow_book(self):
        """borrow_book() выдаёт книгу."""
        self.library.borrow_book("isbn-test")
        self.assertFalse(self.book.is_available)

    def test_borrow_removes_from_available(self):
        """Выданная книга не в списке доступных."""
        self.library.borrow_book("isbn-test")
        available = self.library.get_available_books()
        self.assertNotIn(self.book, available)

    def test_borrow_nonexistent_raises(self):
        """Выдача несуществующей книги вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.library.borrow_book("несуществующий-isbn")

    def test_borrow_already_borrowed_raises(self):
        """Повторная выдача вызывает ValueError."""
        self.library.borrow_book("isbn-test")
        with self.assertRaises(ValueError):
            self.library.borrow_book("isbn-test")

    def test_return_book(self):
        """return_book() возвращает книгу."""
        self.library.borrow_book("isbn-test")
        self.library.return_book("isbn-test")
        self.assertTrue(self.book.is_available)

    def test_return_adds_to_available(self):
        """Возвращённая книга в списке доступных."""
        self.library.borrow_book("isbn-test")
        self.library.return_book("isbn-test")
        available = self.library.get_available_books()
        self.assertIn(self.book, available)

    def test_return_nonexistent_raises(self):
        """Возврат несуществующей книги вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.library.return_book("несуществующий-isbn")

    def test_return_not_borrowed_raises(self):
        """Возврат не выданной книги вызывает ValueError."""
        with self.assertRaises(ValueError):
            self.library.return_book("isbn-test")


class TestLibraryStatistics(unittest.TestCase):
    """Тесты дополнительного задания: статистика."""

    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("Книга 1", "Автор А", 2000, "isbn-1"))
        self.library.add_book(Book("Книга 2", "Автор А", 2001, "isbn-2"))
        self.library.add_book(Book("Книга 3", "Автор Б", 2002, "isbn-3"))

    def test_statistics_total(self):
        """Статистика содержит общее количество."""
        stats = self.library.get_statistics()
        self.assertEqual(stats['total'], 3)

    def test_statistics_available(self):
        """Статистика содержит количество доступных."""
        self.library.borrow_book("isbn-1")
        stats = self.library.get_statistics()
        self.assertEqual(stats['available'], 2)

    def test_statistics_borrowed(self):
        """Статистика содержит количество выданных."""
        self.library.borrow_book("isbn-1")
        stats = self.library.get_statistics()
        self.assertEqual(stats['borrowed'], 1)

    def test_statistics_by_author(self):
        """Статистика по авторам."""
        stats = self.library.get_statistics()
        self.assertIn('by_author', stats)
        self.assertEqual(stats['by_author']['Автор А'], 2)
        self.assertEqual(stats['by_author']['Автор Б'], 1)

    def test_statistics_empty_library(self):
        """Статистика пустой библиотеки."""
        empty_library = Library()
        stats = empty_library.get_statistics()
        self.assertEqual(stats['total'], 0)
        self.assertEqual(stats['available'], 0)
        self.assertEqual(stats['borrowed'], 0)

    def test_statistics_all_borrowed(self):
        """Статистика когда все книги выданы."""
        self.library.borrow_book("isbn-1")
        self.library.borrow_book("isbn-2")
        self.library.borrow_book("isbn-3")
        stats = self.library.get_statistics()
        self.assertEqual(stats['available'], 0)
        self.assertEqual(stats['borrowed'], 3)


class TestLibrarySorting(unittest.TestCase):
    """Тесты дополнительного задания: сортировка."""

    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("Яблоко", "Иванов", 2002, "isbn-1"))
        self.library.add_book(Book("Апельсин", "Петров", 2000, "isbn-2"))
        self.library.add_book(Book("Банан", "Андреев", 2001, "isbn-3"))

    def test_sort_by_title(self):
        """Сортировка по названию."""
        sorted_books = self.library.get_books_sorted_by('title')
        titles = [book.title for book in sorted_books]
        self.assertEqual(titles, ["Апельсин", "Банан", "Яблоко"])

    def test_sort_by_author(self):
        """Сортировка по автору."""
        sorted_books = self.library.get_books_sorted_by('author')
        authors = [book.author for book in sorted_books]
        self.assertEqual(authors, ["Андреев", "Иванов", "Петров"])

    def test_sort_by_year(self):
        """Сортировка по году."""
        sorted_books = self.library.get_books_sorted_by('year')
        years = [book.year for book in sorted_books]
        self.assertEqual(years, [2000, 2001, 2002])

    def test_sort_invalid_field_raises(self):
        """Сортировка по несуществующему полю вызывает ValueError."""
        with self.assertRaises(ValueError):
            self.library.get_books_sorted_by('invalid_field')

    def test_sort_empty_library(self):
        """Сортировка пустой библиотеки возвращает пустой список."""
        empty_library = Library()
        sorted_books = empty_library.get_books_sorted_by('title')
        self.assertEqual(sorted_books, [])

    def test_sort_does_not_modify_original(self):
        """Сортировка не изменяет порядок в библиотеке."""
        original_books = self.library.get_available_books()
        original_order = [book.isbn for book in original_books]

        self.library.get_books_sorted_by('title')

        current_books = self.library.get_available_books()
        current_order = [book.isbn for book in current_books]
        self.assertEqual(original_order, current_order)


class TestLibraryExportJson(unittest.TestCase):
    """Тесты дополнительного задания: экспорт в JSON."""

    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("Книга 1", "Автор А", 2000, "isbn-1"))
        self.library.add_book(Book("Книга 2", "Автор Б", 2001, "isbn-2"))

    def test_export_to_json_returns_string(self):
        """export_to_json() без filename возвращает строку."""
        result = self.library.export_to_json()
        self.assertIsInstance(result, str)

    def test_export_to_json_valid_json(self):
        """export_to_json() возвращает валидный JSON."""
        result = self.library.export_to_json()
        data = json.loads(result)  # Не должно вызывать исключение
        self.assertIsInstance(data, dict)

    def test_export_to_json_contains_books(self):
        """JSON содержит список книг."""
        result = self.library.export_to_json()
        data = json.loads(result)
        self.assertIn('books', data)
        self.assertEqual(len(data['books']), 2)

    def test_export_to_json_book_data(self):
        """JSON содержит данные книг."""
        result = self.library.export_to_json()
        data = json.loads(result)
        books = data['books']

        # Проверяем, что книги содержат нужные поля
        for book in books:
            self.assertIn('title', book)
            self.assertIn('author', book)
            self.assertIn('year', book)
            self.assertIn('isbn', book)

    def test_export_to_json_contains_statistics(self):
        """JSON содержит статистику."""
        result = self.library.export_to_json()
        data = json.loads(result)
        self.assertIn('statistics', data)

    def test_export_to_json_file(self):
        """export_to_json() записывает в файл."""
        import tempfile

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_filename = f.name

        try:
            self.library.export_to_json(temp_filename)

            # Проверяем, что файл создан и содержит валидный JSON
            with open(temp_filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.assertIn('books', data)
            self.assertEqual(len(data['books']), 2)
        finally:
            # Удаляем временный файл
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    def test_export_empty_library(self):
        """Экспорт пустой библиотеки."""
        empty_library = Library()
        result = empty_library.export_to_json()
        data = json.loads(result)
        self.assertEqual(data['books'], [])


class TestLibraryGetAllBooks(unittest.TestCase):
    """Тесты метода get_all_books()."""

    def setUp(self):
        self.library = Library()
        self.book1 = Book("Книга 1", "Автор", 2000, "isbn-1")
        self.book2 = Book("Книга 2", "Автор", 2001, "isbn-2")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_get_all_books(self):
        """get_all_books() возвращает все книги."""
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)

    def test_get_all_books_includes_borrowed(self):
        """get_all_books() включает выданные книги."""
        self.library.borrow_book("isbn-1")
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)
        self.assertIn(self.book1, all_books)

    def test_get_all_books_empty_library(self):
        """get_all_books() для пустой библиотеки."""
        empty_library = Library()
        all_books = empty_library.get_all_books()
        self.assertEqual(all_books, [])


class TestLibraryLen(unittest.TestCase):
    """Тесты магического метода __len__."""

    def test_len_empty(self):
        """len() для пустой библиотеки."""
        library = Library()
        self.assertEqual(len(library), 0)

    def test_len_with_books(self):
        """len() для библиотеки с книгами."""
        library = Library()
        library.add_book(Book("Книга 1", "Автор", 2000, "isbn-1"))
        library.add_book(Book("Книга 2", "Автор", 2001, "isbn-2"))
        self.assertEqual(len(library), 2)

    def test_len_after_remove(self):
        """len() после удаления книги."""
        library = Library()
        library.add_book(Book("Книга 1", "Автор", 2000, "isbn-1"))
        library.add_book(Book("Книга 2", "Автор", 2001, "isbn-2"))
        library.remove_book("isbn-1")
        self.assertEqual(len(library), 1)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Базовые тесты
    suite.addTests(loader.loadTestsFromTestCase(TestBook))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestLibrarySearch))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryBorrow))

    # Дополнительные тесты
    suite.addTests(loader.loadTestsFromTestCase(TestBookToDict))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryStatistics))
    suite.addTests(loader.loadTestsFromTestCase(TestLibrarySorting))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryExportJson))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryGetAllBooks))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryLen))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")

    if result.failures:
        print("\nПроваленные тесты:")
        for test, _ in result.failures:
            print(f"  - {test}")

    if result.errors:
        print("\nТесты с ошибками:")
        for test, _ in result.errors:
            print(f"  - {test}")

    print("=" * 70)