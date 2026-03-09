# python-oop-projects
Проекты по Python сгенерированные нейросетью Claude 4.5 Opus для изучения в формате "learning by doing"
# Серия практических задач по ООП в Python

---

## Задача 1: Первый класс — Счётчик

### Уровень сложности: 1/10

### Изучаемые концепции
- Создание класса с ключевым словом `class`
- Метод `__init__` (конструктор)
- Атрибуты экземпляра (`self`)
- Методы экземпляра

### Подробное условие

Создайте класс `Counter`, который представляет простой счётчик.

**Технические требования:**
1. Метод `__init__` должен принимать необязательный параметр `start` (начальное значение, по умолчанию 0)
2. Атрибут `value` хранит текущее значение счётчика
3. Метод `increment()` увеличивает значение на 1
4. Метод `decrement()` уменьшает значение на 1
5. Метод `reset()` сбрасывает значение к начальному
6. Метод `get_value()` возвращает текущее значение

**Файл для решения:** `counter.py`

### Примеры использования

```python
# Пример 1: Базовое использование
c = Counter()
print(c.get_value())  # 0
c.increment()
c.increment()
print(c.get_value())  # 2

# Пример 2: Начальное значение
c = Counter(start=10)
print(c.get_value())  # 10
c.decrement()
print(c.get_value())  # 9

# Пример 3: Сброс счётчика
c = Counter(start=5)
c.increment()
c.increment()
print(c.get_value())  # 7
c.reset()
print(c.get_value())  # 5 (вернулись к начальному)
```

### Дополнительные задания
1. Добавьте метод `increment_by(n)`, который увеличивает значение на `n`
2. Добавьте проверку: значение не может стать отрицательным (при попытке — остаётся 0)
3. Добавьте метод `__str__`, чтобы `print(c)` выводил `"Counter: 5"`

### Полезные ссылки для самостоятельного изучения
- "Python class __init__ method"
- "Python self keyword explained"
- "Python instance attributes vs class attributes"
- "Python default parameter values"

---

### Файл автотестов: `test_counter.py`

```python
"""
Автотесты для задачи 1: Счётчик
Запуск: python -m pytest test_counter.py -v
Или без pytest: python test_counter.py
"""

import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    """Тесты для класса Counter"""
    
    def test_create_default_counter(self):
        """Создание счётчика с начальным значением по умолчанию"""
        c = Counter()
        self.assertEqual(c.get_value(), 0)
    
    def test_create_counter_with_start_value(self):
        """Создание счётчика с заданным начальным значением"""
        c = Counter(start=10)
        self.assertEqual(c.get_value(), 10)
        
        c2 = Counter(start=-5)
        self.assertEqual(c2.get_value(), -5)
    
    def test_increment(self):
        """Метод increment увеличивает значение на 1"""
        c = Counter()
        c.increment()
        self.assertEqual(c.get_value(), 1)
        c.increment()
        c.increment()
        self.assertEqual(c.get_value(), 3)
    
    def test_decrement(self):
        """Метод decrement уменьшает значение на 1"""
        c = Counter(start=5)
        c.decrement()
        self.assertEqual(c.get_value(), 4)
        c.decrement()
        c.decrement()
        self.assertEqual(c.get_value(), 2)
    
    def test_reset(self):
        """Метод reset возвращает счётчик к начальному значению"""
        c = Counter(start=5)
        c.increment()
        c.increment()
        c.increment()
        self.assertEqual(c.get_value(), 8)
        c.reset()
        self.assertEqual(c.get_value(), 5)
    
    def test_reset_default_counter(self):
        """Reset для счётчика с начальным значением по умолчанию"""
        c = Counter()
        c.increment()
        c.increment()
        c.reset()
        self.assertEqual(c.get_value(), 0)
    
    def test_value_attribute_exists(self):
        """Атрибут value должен быть доступен"""
        c = Counter(start=7)
        self.assertEqual(c.value, 7)
    
    def test_multiple_operations(self):
        """Комбинация различных операций"""
        c = Counter(start=10)
        c.increment()
        c.increment()
        c.decrement()
        c.increment()
        self.assertEqual(c.get_value(), 12)


class TestCounterAdvanced(unittest.TestCase):
    """Дополнительные тесты (для усложнённых заданий)"""
    
    def test_increment_by(self):
        """Дополнительно: метод increment_by"""
        c = Counter()
        if hasattr(c, 'increment_by'):
            c.increment_by(5)
            self.assertEqual(c.get_value(), 5)
            c.increment_by(3)
            self.assertEqual(c.get_value(), 8)
        else:
            self.skipTest("Метод increment_by не реализован")
    
    def test_str_method(self):
        """Дополнительно: метод __str__"""
        c = Counter(start=5)
        result = str(c)
        if "Counter" in result and "5" in result:
            self.assertIn("5", result)
        else:
            self.skipTest("Метод __str__ не реализован или имеет другой формат")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 2: Прямоугольник

### Уровень сложности: 2/10

### Изучаемые концепции
- Множественные атрибуты экземпляра
- Методы, возвращающие вычисленные значения
- Взаимодействие атрибутов внутри методов

### Подробное условие

Создайте класс `Rectangle`, представляющий прямоугольник.

**Технические требования:**
1. Метод `__init__` принимает `width` (ширина) и `height` (высота)
2. Метод `area()` возвращает площадь прямоугольника
3. Метод `perimeter()` возвращает периметр прямоугольника
4. Метод `is_square()` возвращает `True`, если это квадрат
5. Метод `resize(new_width, new_height)` изменяет размеры
6. Метод `get_dimensions()` возвращает кортеж `(width, height)`

**Файл для решения:** `rectangle.py`

### Примеры использования

```python
# Пример 1: Базовые вычисления
r = Rectangle(5, 3)
print(r.area())        # 15
print(r.perimeter())   # 16
print(r.is_square())   # False

# Пример 2: Квадрат
sq = Rectangle(4, 4)
print(sq.area())       # 16
print(sq.is_square())  # True

# Пример 3: Изменение размеров
r = Rectangle(10, 5)
print(r.get_dimensions())  # (10, 5)
r.resize(7, 7)
print(r.get_dimensions())  # (7, 7)
print(r.is_square())       # True
```

### Дополнительные задания
1. Добавьте валидацию: ширина и высота должны быть положительными числами (иначе `ValueError`)
2. Реализуйте метод `scale(factor)`, который умножает оба размера на коэффициент
3. Добавьте метод `__eq__`, чтобы два прямоугольника считались равными при одинаковых размерах

### Полезные ссылки для самостоятельного изучения
- "Python return tuple from method"
- "Python raise ValueError"
- "Python __eq__ method"

---

### Файл автотестов: `test_rectangle.py`

```python
"""
Автотесты для задачи 2: Прямоугольник
Запуск: python -m pytest test_rectangle.py -v
"""

import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Тесты для класса Rectangle"""
    
    def test_create_rectangle(self):
        """Создание прямоугольника с заданными размерами"""
        r = Rectangle(5, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
    
    def test_area(self):
        """Вычисление площади"""
        r = Rectangle(5, 3)
        self.assertEqual(r.area(), 15)
        
        r2 = Rectangle(10, 10)
        self.assertEqual(r2.area(), 100)
        
        r3 = Rectangle(2.5, 4)
        self.assertEqual(r3.area(), 10.0)
    
    def test_perimeter(self):
        """Вычисление периметра"""
        r = Rectangle(5, 3)
        self.assertEqual(r.perimeter(), 16)
        
        r2 = Rectangle(10, 10)
        self.assertEqual(r2.perimeter(), 40)
    
    def test_is_square_true(self):
        """Проверка: прямоугольник является квадратом"""
        sq = Rectangle(4, 4)
        self.assertTrue(sq.is_square())
        
        sq2 = Rectangle(1, 1)
        self.assertTrue(sq2.is_square())
    
    def test_is_square_false(self):
        """Проверка: прямоугольник не является квадратом"""
        r = Rectangle(5, 3)
        self.assertFalse(r.is_square())
        
        r2 = Rectangle(10, 5)
        self.assertFalse(r2.is_square())
    
    def test_resize(self):
        """Изменение размеров прямоугольника"""
        r = Rectangle(5, 3)
        r.resize(10, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.area(), 80)
    
    def test_get_dimensions(self):
        """Получение размеров как кортежа"""
        r = Rectangle(5, 3)
        self.assertEqual(r.get_dimensions(), (5, 3))
        
        r.resize(7, 7)
        self.assertEqual(r.get_dimensions(), (7, 7))
    
    def test_dimensions_order(self):
        """Порядок в кортеже: (width, height)"""
        r = Rectangle(100, 1)
        dims = r.get_dimensions()
        self.assertEqual(dims[0], 100)  # width первый
        self.assertEqual(dims[1], 1)    # height второй


class TestRectangleAdvanced(unittest.TestCase):
    """Дополнительные тесты"""
    
    def test_validation_negative_width(self):
        """Дополнительно: отрицательная ширина вызывает ValueError"""
        try:
            r = Rectangle(-5, 3)
            # Если исключение не выброшено, проверяем есть ли валидация
            self.skipTest("Валидация не реализована")
        except ValueError:
            pass  # Ожидаемое поведение
    
    def test_validation_negative_height(self):
        """Дополнительно: отрицательная высота вызывает ValueError"""
        try:
            r = Rectangle(5, -3)
            self.skipTest("Валидация не реализована")
        except ValueError:
            pass
    
    def test_scale(self):
        """Дополнительно: метод scale"""
        r = Rectangle(4, 3)
        if hasattr(r, 'scale'):
            r.scale(2)
            self.assertEqual(r.get_dimensions(), (8, 6))
        else:
            self.skipTest("Метод scale не реализован")
    
    def test_equality(self):
        """Дополнительно: сравнение прямоугольников"""
        r1 = Rectangle(5, 3)
        r2 = Rectangle(5, 3)
        r3 = Rectangle(3, 5)
        
        if r1 == r2:  # Проверяем, реализован ли __eq__
            self.assertEqual(r1, r2)
            self.assertNotEqual(r1, r3)
        else:
            self.skipTest("Метод __eq__ не реализован")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 3: Банковский счёт

### Уровень сложности: 3/10

### Изучаемые концепции
- Инкапсуляция (защищённые атрибуты с `_`)
- Валидация данных в методах
- Выброс исключений
- Работа со строками в методах

### Подробное условие

Создайте класс `BankAccount`, представляющий банковский счёт.

**Технические требования:**
1. Метод `__init__` принимает `owner` (имя владельца) и необязательный `balance` (начальный баланс, по умолчанию 0)
2. Баланс должен храниться в защищённом атрибуте `_balance`
3. Метод `deposit(amount)` пополняет счёт. Сумма должна быть положительной, иначе `ValueError`
4. Метод `withdraw(amount)` снимает деньги. Нельзя снять больше, чем есть на счёте (`ValueError`), и сумма должна быть положительной
5. Метод `get_balance()` возвращает текущий баланс
6. Метод `transfer(other_account, amount)` переводит деньги на другой счёт
7. Метод `__str__` возвращает строку формата `"Account of {owner}: {balance} USD"`

**Файл для решения:** `bank_account.py`

### Примеры использования

```python
# Пример 1: Базовые операции
acc = BankAccount("Alice", 100)
print(acc.get_balance())     # 100
acc.deposit(50)
print(acc.get_balance())     # 150
acc.withdraw(30)
print(acc.get_balance())     # 120

# Пример 2: Ошибки валидации
acc = BankAccount("Bob", 50)
try:
    acc.withdraw(100)  # Попытка снять больше, чем есть
except ValueError as e:
    print(e)  # "Insufficient funds" или подобное сообщение

try:
    acc.deposit(-10)  # Отрицательная сумма
except ValueError as e:
    print(e)  # "Amount must be positive" или подобное

# Пример 3: Перевод между счетами
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)
acc1.transfer(acc2, 30)
print(acc1.get_balance())  # 70
print(acc2.get_balance())  # 80
print(acc1)  # "Account of Alice: 70 USD"
```

### Дополнительные задания
1. Добавьте историю транзакций: метод `get_history()` возвращает список всех операций
2. Добавьте статический атрибут `bank_name` и метод класса `get_bank_name()`
3. Реализуйте лимит на снятие за одну операцию (например, не более 500)

### Полезные ссылки для самостоятельного изучения
- "Python protected attributes underscore"
- "Python raise exception with message"
- "Python __str__ vs __repr__"
- "Python encapsulation"

---

### Файл автотестов: `test_bank_account.py`

```python
"""
Автотесты для задачи 3: Банковский счёт
Запуск: python -m pytest test_bank_account.py -v
"""

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """Тесты для класса BankAccount"""
    
    def test_create_account_with_balance(self):
        """Создание счёта с начальным балансом"""
        acc = BankAccount("Alice", 100)
        self.assertEqual(acc.owner, "Alice")
        self.assertEqual(acc.get_balance(), 100)
    
    def test_create_account_default_balance(self):
        """Создание счёта без указания баланса (по умолчанию 0)"""
        acc = BankAccount("Bob")
        self.assertEqual(acc.get_balance(), 0)
    
    def test_deposit(self):
        """Пополнение счёта"""
        acc = BankAccount("Alice", 100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)
        
        acc.deposit(25.5)
        self.assertEqual(acc.get_balance(), 175.5)
    
    def test_deposit_negative_raises_error(self):
        """Пополнение на отрицательную сумму вызывает ValueError"""
        acc = BankAccount("Alice", 100)
        with self.assertRaises(ValueError):
            acc.deposit(-10)
    
    def test_deposit_zero_raises_error(self):
        """Пополнение на ноль вызывает ValueError"""
        acc = BankAccount("Alice", 100)
        with self.assertRaises(ValueError):
            acc.deposit(0)
    
    def test_withdraw(self):
        """Снятие денег со счёта"""
        acc = BankAccount("Alice", 100)
        acc.withdraw(30)
        self.assertEqual(acc.get_balance(), 70)
        
        acc.withdraw(70)
        self.assertEqual(acc.get_balance(), 0)
    
    def test_withdraw_insufficient_funds(self):
        """Снятие больше, чем есть на счёте, вызывает ValueError"""
        acc = BankAccount("Alice", 50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)
    
    def test_withdraw_negative_raises_error(self):
        """Снятие отрицательной суммы вызывает ValueError"""
        acc = BankAccount("Alice", 100)
        with self.assertRaises(ValueError):
            acc.withdraw(-10)
    
    def test_transfer(self):
        """Перевод денег между счетами"""
        acc1 = BankAccount("Alice", 100)
        acc2 = BankAccount("Bob", 50)
        
        acc1.transfer(acc2, 30)
        
        self.assertEqual(acc1.get_balance(), 70)
        self.assertEqual(acc2.get_balance(), 80)
    
    def test_transfer_insufficient_funds(self):
        """Перевод больше, чем есть на счёте"""
        acc1 = BankAccount("Alice", 30)
        acc2 = BankAccount("Bob", 50)
        
        with self.assertRaises(ValueError):
            acc1.transfer(acc2, 100)
        
        # Балансы не должны измениться
        self.assertEqual(acc1.get_balance(), 30)
        self.assertEqual(acc2.get_balance(), 50)
    
    def test_str_method(self):
        """Строковое представление счёта"""
        acc = BankAccount("Alice", 100)
        result = str(acc)
        self.assertIn("Alice", result)
        self.assertIn("100", result)
        self.assertIn("USD", result)
    
    def test_protected_balance_attribute(self):
        """Баланс хранится в защищённом атрибуте _balance"""
        acc = BankAccount("Alice", 100)
        self.assertTrue(hasattr(acc, '_balance'))
        self.assertEqual(acc._balance, 100)


class TestBankAccountAdvanced(unittest.TestCase):
    """Дополнительные тесты"""
    
    def test_transaction_history(self):
        """Дополнительно: история транзакций"""
        acc = BankAccount("Alice", 100)
        if hasattr(acc, 'get_history'):
            acc.deposit(50)
            acc.withdraw(30)
            history = acc.get_history()
            self.assertIsInstance(history, list)
            self.assertGreater(len(history), 0)
        else:
            self.skipTest("Метод get_history не реализован")
    
    def test_bank_name_class_attribute(self):
        """Дополнительно: атрибут класса bank_name"""
        if hasattr(BankAccount, 'bank_name'):
            self.assertIsNotNone(BankAccount.bank_name)
        else:
            self.skipTest("Атрибут bank_name не реализован")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 4: Книга и Библиотека

### Уровень сложности: 4/10

### Изучаемые концепции
- Взаимодействие нескольких классов
- Композиция (объекты как атрибуты других объектов)
- Работа со списками объектов
- Поиск и фильтрация объектов

### Подробное условие

Создайте два класса: `Book` и `Library`.

**Класс `Book`:**
1. Атрибуты: `title` (название), `author` (автор), `year` (год издания), `is_available` (доступна ли, по умолчанию `True`)
2. Метод `__str__` возвращает `"{title} by {author} ({year})"`
3. Метод `borrow()` делает книгу недоступной (если уже недоступна — `ValueError`)
4. Метод `return_book()` делает книгу доступной

**Класс `Library`:**
1. Атрибут `name` (название библиотеки)
2. Атрибут `books` — список книг (изначально пустой)
3. Метод `add_book(book)` добавляет книгу в библиотеку
4. Метод `find_by_title(title)` возвращает книгу по названию или `None`
5. Метод `find_by_author(author)` возвращает список всех книг автора
6. Метод `get_available_books()` возвращает список доступных книг
7. Метод `borrow_book(title)` находит книгу и делает её недоступной

**Файлы для решения:** `book.py` и `library.py`

### Примеры использования

```python
# Пример 1: Создание книг
b1 = Book("1984", "George Orwell", 1949)
b2 = Book("Animal Farm", "George Orwell", 1945)
b3 = Book("Brave New World", "Aldous Huxley", 1932)

print(b1)  # "1984 by George Orwell (1949)"

# Пример 2: Работа с библиотекой
lib = Library("City Library")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

orwell_books = lib.find_by_author("George Orwell")
print(len(orwell_books))  # 2

# Пример 3: Выдача книг
print(len(lib.get_available_books()))  # 3
lib.borrow_book("1984")
print(len(lib.get_available_books()))  # 2
print(b1.is_available)  # False

# Попытка взять уже выданную книгу
try:
    lib.borrow_book("1984")
except ValueError:
    print("Книга уже выдана!")
```

### Дополнительные задания
1. Добавьте метод `find_by_year_range(start, end)` для поиска книг по диапазону годов
2. Реализуйте метод `remove_book(title)` с проверкой, что книга не выдана
3. Добавьте метод `__len__` для `Library`, возвращающий количество книг

### Полезные ссылки для самостоятельного изучения
- "Python composition vs inheritance"
- "Python list of objects"
- "Python filter list by attribute"
- "Python find object in list"

---

### Файл автотестов: `test_book_library.py`

```python
"""
Автотесты для задачи 4: Книга и Библиотека
Запуск: python -m pytest test_book_library.py -v
"""

import unittest
from book import Book
from library import Library


class TestBook(unittest.TestCase):
    """Тесты для класса Book"""
    
    def test_create_book(self):
        """Создание книги с атрибутами"""
        book = Book("1984", "George Orwell", 1949)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.year, 1949)
        self.assertTrue(book.is_available)
    
    def test_book_str(self):
        """Строковое представление книги"""
        book = Book("1984", "George Orwell", 1949)
        result = str(book)
        self.assertIn("1984", result)
        self.assertIn("George Orwell", result)
        self.assertIn("1949", result)
    
    def test_borrow_book(self):
        """Выдача книги"""
        book = Book("1984", "George Orwell", 1949)
        book.borrow()
        self.assertFalse(book.is_available)
    
    def test_borrow_unavailable_book_raises_error(self):
        """Попытка выдать уже выданную книгу"""
        book = Book("1984", "George Orwell", 1949)
        book.borrow()
        with self.assertRaises(ValueError):
            book.borrow()
    
    def test_return_book(self):
        """Возврат книги"""
        book = Book("1984", "George Orwell", 1949)
        book.borrow()
        book.return_book()
        self.assertTrue(book.is_available)


class TestLibrary(unittest.TestCase):
    """Тесты для класса Library"""
    
    def setUp(self):
        """Подготовка данных для каждого теста"""
        self.lib = Library("Test Library")
        self.b1 = Book("1984", "George Orwell", 1949)
        self.b2 = Book("Animal Farm", "George Orwell", 1945)
        self.b3 = Book("Brave New World", "Aldous Huxley", 1932)
    
    def test_create_library(self):
        """Создание библиотеки"""
        lib = Library("City Library")
        self.assertEqual(lib.name, "City Library")
        self.assertEqual(lib.books, [])
    
    def test_add_book(self):
        """Добавление книги в библиотеку"""
        self.lib.add_book(self.b1)
        self.assertEqual(len(self.lib.books), 1)
        self.assertIn(self.b1, self.lib.books)
    
    def test_find_by_title_found(self):
        """Поиск книги по названию — найдена"""
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        
        result = self.lib.find_by_title("1984")
        self.assertEqual(result, self.b1)
    
    def test_find_by_title_not_found(self):
        """Поиск книги по названию — не найдена"""
        self.lib.add_book(self.b1)
        
        result = self.lib.find_by_title("Unknown Book")
        self.assertIsNone(result)
    
    def test_find_by_author(self):
        """Поиск всех книг автора"""
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        self.lib.add_book(self.b3)
        
        orwell_books = self.lib.find_by_author("George Orwell")
        self.assertEqual(len(orwell_books), 2)
        self.assertIn(self.b1, orwell_books)
        self.assertIn(self.b2, orwell_books)
    
    def test_find_by_author_not_found(self):
        """Поиск книг несуществующего автора"""
        self.lib.add_book(self.b1)
        
        result = self.lib.find_by_author("Unknown Author")
        self.assertEqual(result, [])
    
    def test_get_available_books(self):
        """Получение списка доступных книг"""
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        self.lib.add_book(self.b3)
        
        available = self.lib.get_available_books()
        self.assertEqual(len(available), 3)
        
        self.b1.borrow()
        available = self.lib.get_available_books()
        self.assertEqual(len(available), 2)
        self.assertNotIn(self.b1, available)
    
    def test_borrow_book(self):
        """Выдача книги через библиотеку"""
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        
        self.lib.borrow_book("1984")
        self.assertFalse(self.b1.is_available)
        self.assertTrue(self.b2.is_available)
    
    def test_borrow_book_not_found(self):
        """Попытка выдать несуществующую книгу"""
        self.lib.add_book(self.b1)
        
        # Должно либо вернуть None, либо выбросить исключение
        try:
            result = self.lib.borrow_book("Unknown")
            # Если не выбросило исключение, проверяем что вернулось
        except (ValueError, KeyError):
            pass  # Допустимое поведение


class TestLibraryAdvanced(unittest.TestCase):
    """Дополнительные тесты"""
    
    def setUp(self):
        self.lib = Library("Test Library")
        self.b1 = Book("1984", "George Orwell", 1949)
        self.b2 = Book("Animal Farm", "George Orwell", 1945)
        self.b3 = Book("Brave New World", "Aldous Huxley", 1932)
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        self.lib.add_book(self.b3)
    
    def test_find_by_year_range(self):
        """Дополнительно: поиск по диапазону годов"""
        if hasattr(self.lib, 'find_by_year_range'):
            result = self.lib.find_by_year_range(1940, 1950)
            self.assertEqual(len(result), 2)
        else:
            self.skipTest("Метод find_by_year_range не реализован")
    
    def test_len_method(self):
        """Дополнительно: метод __len__"""
        try:
            length = len(self.lib)
            self.assertEqual(length, 3)
        except TypeError:
            self.skipTest("Метод __len__ не реализован")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 5: Наследование — Транспортные средства

### Уровень сложности: 5/10

### Изучаемые концепции
- Наследование классов
- Вызов конструктора родительского класса (`super()`)
- Переопределение методов
- Расширение функциональности родительского класса

### Подробное условие

Создайте иерархию классов для транспортных средств.

**Базовый класс `Vehicle`:**
1. Атрибуты в `__init__`: `brand` (марка), `model` (модель), `year` (год выпуска)
2. Атрибут `is_running` (заведён ли двигатель, по умолчанию `False`)
3. Метод `start()` — запускает двигатель (меняет `is_running` на `True`)
4. Метод `stop()` — останавливает двигатель
5. Метод `get_info()` — возвращает `"{brand} {model} ({year})"`

**Класс `Car(Vehicle)`:**
1. Дополнительный атрибут `num_doors` (количество дверей)
2. Переопределённый `get_info()` добавляет информацию о дверях
3. Метод `honk()` — возвращает `"Beep beep!"`

**Класс `Motorcycle(Vehicle)`:**
1. Дополнительный атрибут `has_sidecar` (есть ли коляска, по умолчанию `False`)
2. Переопределённый `get_info()` добавляет информацию о коляске
3. Метод `wheelie()` — возвращает `"Doing a wheelie!"` (но только если двигатель запущен, иначе `ValueError`)

**Класс `ElectricCar(Car)`:**
1. Дополнительный атрибут `battery_capacity` (ёмкость батареи в kWh)
2. Атрибут `charge_level` (уровень заряда, по умолчанию 100)
3. Метод `charge(amount)` — увеличивает заряд (максимум 100)
4. Переопределённый `start()` — нельзя завести при заряде 0

**Файлы для решения:** `vehicle.py`, `car.py`, `motorcycle.py`, `electric_car.py`

### Примеры использования

```python
# Пример 1: Базовый Vehicle
v = Vehicle("Generic", "Model", 2020)
print(v.get_info())  # "Generic Model (2020)"
v.start()
print(v.is_running)  # True

# Пример 2: Car
car = Car("Toyota", "Camry", 2022, num_doors=4)
print(car.get_info())  # "Toyota Camry (2022), 4 doors"
print(car.honk())      # "Beep beep!"

# Пример 3: Motorcycle
moto = Motorcycle("Harley", "Sportster", 2021, has_sidecar=True)
print(moto.get_info())  # "Harley Sportster (2021), with sidecar"

moto.start()
print(moto.wheelie())  # "Doing a wheelie!"

# Пример 4: ElectricCar
ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
ev.charge_level = 0
try:
    ev.start()  # ValueError: Battery is empty
except ValueError:
    ev.charge(50)
    ev.start()  # Теперь работает
```

### Дополнительные задания
1. Добавьте класс `Truck(Vehicle)` с атрибутом `cargo_capacity` и методом `load_cargo(weight)`
2. Реализуйте метод `__repr__` для всех классов для отладки
3. Добавьте абстрактный метод `fuel_type()` в базовый класс (вернуть тип топлива)

### Полезные ссылки для самостоятельного изучения
- "Python inheritance tutorial"
- "Python super() function"
- "Python method overriding"
- "Python multiple inheritance MRO"

---

### Файл автотестов: `test_vehicles.py`

```python
"""
Автотесты для задачи 5: Транспортные средства
Запуск: python -m pytest test_vehicles.py -v
"""

import unittest
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from electric_car import ElectricCar


class TestVehicle(unittest.TestCase):
    """Тесты для базового класса Vehicle"""
    
    def test_create_vehicle(self):
        """Создание транспортного средства"""
        v = Vehicle("Generic", "Model", 2020)
        self.assertEqual(v.brand, "Generic")
        self.assertEqual(v.model, "Model")
        self.assertEqual(v.year, 2020)
        self.assertFalse(v.is_running)
    
    def test_start_stop(self):
        """Запуск и остановка двигателя"""
        v = Vehicle("Generic", "Model", 2020)
        
        v.start()
        self.assertTrue(v.is_running)
        
        v.stop()
        self.assertFalse(v.is_running)
    
    def test_get_info(self):
        """Информация о транспортном средстве"""
        v = Vehicle("Generic", "Model", 2020)
        info = v.get_info()
        self.assertIn("Generic", info)
        self.assertIn("Model", info)
        self.assertIn("2020", info)


class TestCar(unittest.TestCase):
    """Тесты для класса Car"""
    
    def test_create_car(self):
        """Создание автомобиля"""
        car = Car("Toyota", "Camry", 2022, num_doors=4)
        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.num_doors, 4)
    
    def test_car_inherits_vehicle(self):
        """Car наследует от Vehicle"""
        car = Car("Toyota", "Camry", 2022, num_doors=4)
        self.assertIsInstance(car, Vehicle)
    
    def test_car_start_stop(self):
        """Унаследованные методы работают"""
        car = Car("Toyota", "Camry", 2022, num_doors=4)
        car.start()
        self.assertTrue(car.is_running)
    
    def test_car_get_info(self):
        """Переопределённый get_info включает двери"""
        car = Car("Toyota", "Camry", 2022, num_doors=4)
        info = car.get_info()
        self.assertIn("Toyota", info)
        self.assertIn("4", info)
        self.assertIn("door", info.lower())
    
    def test_honk(self):
        """Метод honk"""
        car = Car("Toyota", "Camry", 2022, num_doors=4)
        self.assertEqual(car.honk(), "Beep beep!")


class TestMotorcycle(unittest.TestCase):
    """Тесты для класса Motorcycle"""
    
    def test_create_motorcycle(self):
        """Создание мотоцикла"""
        moto = Motorcycle("Harley", "Sportster", 2021)
        self.assertEqual(moto.brand, "Harley")
        self.assertFalse(moto.has_sidecar)
    
    def test_motorcycle_with_sidecar(self):
        """Мотоцикл с коляской"""
        moto = Motorcycle("Ural", "Gear Up", 2020, has_sidecar=True)
        self.assertTrue(moto.has_sidecar)
    
    def test_motorcycle_inherits_vehicle(self):
        """Motorcycle наследует от Vehicle"""
        moto = Motorcycle("Harley", "Sportster", 2021)
        self.assertIsInstance(moto, Vehicle)
    
    def test_motorcycle_get_info(self):
        """get_info отображает информацию о коляске"""
        moto = Motorcycle("Ural", "Gear Up", 2020, has_sidecar=True)
        info = moto.get_info()
        self.assertIn("sidecar", info.lower())
    
    def test_wheelie_when_running(self):
        """wheelie работает при запущенном двигателе"""
        moto = Motorcycle("Harley", "Sportster", 2021)
        moto.start()
        result = moto.wheelie()
        self.assertIn("wheelie", result.lower())
    
    def test_wheelie_when_not_running(self):
        """wheelie вызывает ошибку при выключенном двигателе"""
        moto = Motorcycle("Harley", "Sportster", 2021)
        with self.assertRaises(ValueError):
            moto.wheelie()


class TestElectricCar(unittest.TestCase):
    """Тесты для класса ElectricCar"""
    
    def test_create_electric_car(self):
        """Создание электромобиля"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        self.assertEqual(ev.brand, "Tesla")
        self.assertEqual(ev.battery_capacity, 75)
        self.assertEqual(ev.charge_level, 100)
    
    def test_electric_car_inherits_car(self):
        """ElectricCar наследует от Car"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        self.assertIsInstance(ev, Car)
        self.assertIsInstance(ev, Vehicle)
    
    def test_electric_car_has_honk(self):
        """Унаследованный метод honk"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        self.assertEqual(ev.honk(), "Beep beep!")
    
    def test_charge(self):
        """Зарядка батареи"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        ev.charge_level = 50
        ev.charge(30)
        self.assertEqual(ev.charge_level, 80)
    
    def test_charge_max_100(self):
        """Заряд не превышает 100"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        ev.charge_level = 90
        ev.charge(50)
        self.assertEqual(ev.charge_level, 100)
    
    def test_start_with_empty_battery(self):
        """Нельзя завести с пустой батареей"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        ev.charge_level = 0
        with self.assertRaises(ValueError):
            ev.start()
    
    def test_start_with_charge(self):
        """Можно завести при наличии заряда"""
        ev = ElectricCar("Tesla", "Model 3", 2023, num_doors=4, battery_capacity=75)
        ev.charge_level = 10
        ev.start()
        self.assertTrue(ev.is_running)


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 6: Полиморфизм — Зоопарк

### Уровень сложности: 6/10

### Изучаемые концепции
- Полиморфизм
- Единый интерфейс для разных типов объектов
- Обработка коллекций разнородных объектов
- Duck typing в Python

### Подробное условие

Создайте систему классов для зоопарка, демонстрирующую полиморфизм.

**Базовый класс `Animal`:**
1. Атрибуты: `name`, `age`
2. Метод `speak()` — возвращает строку со звуком животного (в базовом классе — `"Some sound"`)
3. Метод `info()` — возвращает `"{name}, {age} years old"`
4. Метод `eat(food)` — возвращает `"{name} is eating {food}"`

**Классы-потомки:**
- `Lion`: `speak()` → `"Roar!"`, дополнительный метод `hunt()` → `"{name} is hunting"`
- `Elephant`: `speak()` → `"Trumpet!"`, атрибут `trunk_length`, метод `spray_water()` → `"{name} sprays water"`
- `Parrot`: `speak()` → `"Squawk! {phrase}"` где `phrase` — атрибут с фразой попугая, метод `learn_phrase(phrase)` — меняет фразу
- `Snake`: `speak()` → `"Hiss..."`, атрибут `is_venomous`, метод `shed_skin()` → `"{name} is shedding skin"`

**Класс `Zoo`:**
1. Атрибут `animals` — список животных
2. Метод `add_animal(animal)` — добавляет животное
3. Метод `all_speak()` — возвращает список результатов `speak()` всех животных
4. Метод `feed_all(food)` — возвращает список результатов кормления всех
5. Метод `get_by_type(animal_type)` — возвращает всех животных указанного типа

**Файлы для решения:** `animal.py`, `lion.py`, `elephant.py`, `parrot.py`, `snake.py`, `zoo.py`

### Примеры использования

```python
# Пример 1: Полиморфизм в действии
lion = Lion("Simba", 5)
elephant = Elephant("Dumbo", 10, trunk_length=2.5)
parrot = Parrot("Polly", 3, phrase="Hello!")
snake = Snake("Kaa", 8, is_venomous=False)

animals = [lion, elephant, parrot, snake]
for animal in animals:
    print(animal.speak())
# "Roar!"
# "Trumpet!"
# "Squawk! Hello!"
# "Hiss..."

# Пример 2: Зоопарк
zoo = Zoo()
zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(parrot)

sounds = zoo.all_speak()
print(sounds)  # ["Roar!", "Trumpet!", "Squawk! Hello!"]

# Пример 3: Кормление
meals = zoo.feed_all("meat")
print(meals)
# ["Simba is eating meat", "Dumbo is eating meat", "Polly is eating meat"]

# Пример 4: Уникальные методы
parrot.learn_phrase("Polly wants a cracker!")
print(parrot.speak())  # "Squawk! Polly wants a cracker!"

print(lion.hunt())  # "Simba is hunting"
```

### Дополнительные задания
1. Добавьте метод `Zoo.oldest_animal()`, возвращающий самое старое животное
2. Реализуйте метод `Zoo.total_age()` через встроенную функцию `sum()`
3. Добавьте класс `Penguin` с методом `swim()` и `slide()`

### Полезные ссылки для самостоятельного изучения
- "Python polymorphism examples"
- "Python duck typing"
- "Python isinstance vs type"
- "Python list comprehension with methods"

---

### Файл автотестов: `test_zoo.py`

```python
"""
Автотесты для задачи 6: Зоопарк
Запуск: python -m pytest test_zoo.py -v
"""

import unittest
from animal import Animal
from lion import Lion
from elephant import Elephant
from parrot import Parrot
from snake import Snake
from zoo import Zoo


class TestAnimal(unittest.TestCase):
    """Тесты для базового класса Animal"""
    
    def test_create_animal(self):
        """Создание животного"""
        a = Animal("Generic", 5)
        self.assertEqual(a.name, "Generic")
        self.assertEqual(a.age, 5)
    
    def test_speak(self):
        """Базовый метод speak"""
        a = Animal("Generic", 5)
        result = a.speak()
        self.assertIsInstance(result, str)
    
    def test_info(self):
        """Метод info"""
        a = Animal("Generic", 5)
        info = a.info()
        self.assertIn("Generic", info)
        self.assertIn("5", info)
    
    def test_eat(self):
        """Метод eat"""
        a = Animal("Generic", 5)
        result = a.eat("food")
        self.assertIn("Generic", result)
        self.assertIn("food", result)


class TestLion(unittest.TestCase):
    """Тесты для класса Lion"""
    
    def test_create_lion(self):
        """Создание льва"""
        lion = Lion("Simba", 5)
        self.assertEqual(lion.name, "Simba")
        self.assertIsInstance(lion, Animal)
    
    def test_speak(self):
        """Лев рычит"""
        lion = Lion("Simba", 5)
        self.assertEqual(lion.speak(), "Roar!")
    
    def test_hunt(self):
        """Метод hunt"""
        lion = Lion("Simba", 5)
        result = lion.hunt()
        self.assertIn("Simba", result)
        self.assertIn("hunting", result.lower())


class TestElephant(unittest.TestCase):
    """Тесты для класса Elephant"""
    
    def test_create_elephant(self):
        """Создание слона"""
        elephant = Elephant("Dumbo", 10, trunk_length=2.5)
        self.assertEqual(elephant.name, "Dumbo")
        self.assertEqual(elephant.trunk_length, 2.5)
    
    def test_speak(self):
        """Слон трубит"""
        elephant = Elephant("Dumbo", 10, trunk_length=2.5)
        self.assertEqual(elephant.speak(), "Trumpet!")
    
    def test_spray_water(self):
        """Метод spray_water"""
        elephant = Elephant("Dumbo", 10, trunk_length=2.5)
        result = elephant.spray_water()
        self.assertIn("Dumbo", result)
        self.assertIn("water", result.lower())


class TestParrot(unittest.TestCase):
    """Тесты для класса Parrot"""
    
    def test_create_parrot(self):
        """Создание попугая"""
        parrot = Parrot("Polly", 3, phrase="Hello!")
        self.assertEqual(parrot.name, "Polly")
        self.assertEqual(parrot.phrase, "Hello!")
    
    def test_speak(self):
        """Попугай говорит фразу"""
        parrot = Parrot("Polly", 3, phrase="Hello!")
        result = parrot.speak()
        self.assertIn("Hello!", result)
        self.assertIn("Squawk", result)
    
    def test_learn_phrase(self):
        """Попугай учит новую фразу"""
        parrot = Parrot("Polly", 3, phrase="Hello!")
        parrot.learn_phrase("Goodbye!")
        result = parrot.speak()
        self.assertIn("Goodbye!", result)
        self.assertNotIn("Hello!", result)


class TestSnake(unittest.TestCase):
    """Тесты для класса Snake"""
    
    def test_create_snake(self):
        """Создание змеи"""
        snake = Snake("Kaa", 8, is_venomous=False)
        self.assertEqual(snake.name, "Kaa")
        self.assertFalse(snake.is_venomous)
    
    def test_create_venomous_snake(self):
        """Создание ядовитой змеи"""
        snake = Snake("Viper", 5, is_venomous=True)
        self.assertTrue(snake.is_venomous)
    
    def test_speak(self):
        """Змея шипит"""
        snake = Snake("Kaa", 8, is_venomous=False)
        result = snake.speak()
        self.assertIn("Hiss", result)
    
    def test_shed_skin(self):
        """Метод shed_skin"""
        snake = Snake("Kaa", 8, is_venomous=False)
        result = snake.shed_skin()
        self.assertIn("Kaa", result)
        self.assertIn("shed", result.lower())


class TestZoo(unittest.TestCase):
    """Тесты для класса Zoo"""
    
    def setUp(self):
        """Подготовка данных"""
        self.zoo = Zoo()
        self.lion = Lion("Simba", 5)
        self.elephant = Elephant("Dumbo", 10, trunk_length=2.5)
        self.parrot = Parrot("Polly", 3, phrase="Hello!")
    
    def test_create_zoo(self):
        """Создание зоопарка"""
        zoo = Zoo()
        self.assertEqual(zoo.animals, [])
    
    def test_add_animal(self):
        """Добавление животного"""
        self.zoo.add_animal(self.lion)
        self.assertEqual(len(self.zoo.animals), 1)
    
    def test_all_speak(self):
        """Все животные говорят"""
        self.zoo.add_animal(self.lion)
        self.zoo.add_animal(self.elephant)
        self.zoo.add_animal(self.parrot)
        
        sounds = self.zoo.all_speak()
        
        self.assertEqual(len(sounds), 3)
        self.assertIn("Roar!", sounds)
        self.assertIn("Trumpet!", sounds)
    
    def test_feed_all(self):
        """Кормление всех животных"""
        self.zoo.add_animal(self.lion)
        self.zoo.add_animal(self.elephant)
        
        meals = self.zoo.feed_all("meat")
        
        self.assertEqual(len(meals), 2)
        self.assertTrue(all("meat" in m for m in meals))
    
    def test_get_by_type(self):
        """Получение животных по типу"""
        lion2 = Lion("Mufasa", 15)
        self.zoo.add_animal(self.lion)
        self.zoo.add_animal(lion2)
        self.zoo.add_animal(self.elephant)
        
        lions = self.zoo.get_by_type(Lion)
        
        self.assertEqual(len(lions), 2)
        self.assertIn(self.lion, lions)
        self.assertIn(lion2, lions)


class TestZooAdvanced(unittest.TestCase):
    """Дополнительные тесты"""
    
    def setUp(self):
        self.zoo = Zoo()
        self.lion = Lion("Simba", 5)
        self.elephant = Elephant("Dumbo", 10, trunk_length=2.5)
        self.parrot = Parrot("Polly", 3, phrase="Hello!")
        self.zoo.add_animal(self.lion)
        self.zoo.add_animal(self.elephant)
        self.zoo.add_animal(self.parrot)
    
    def test_oldest_animal(self):
        """Дополнительно: самое старое животное"""
        if hasattr(self.zoo, 'oldest_animal'):
            oldest = self.zoo.oldest_animal()
            self.assertEqual(oldest, self.elephant)
        else:
            self.skipTest("Метод oldest_animal не реализован")
    
    def test_total_age(self):
        """Дополнительно: суммарный возраст"""
        if hasattr(self.zoo, 'total_age'):
            total = self.zoo.total_age()
            self.assertEqual(total, 18)  # 5 + 10 + 3
        else:
            self.skipTest("Метод total_age не реализован")


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## Задача 7: Свойства (Properties) — Термостат

### Уровень сложности: 7/10

### Изучаемые концепции
- Декоратор `@property`
- Геттеры и сеттеры
- Валидация при присваивании
- Вычисляемые свойства
- Приватные атрибуты (`__`)

### Подробное условие

Создайте класс `Thermostat`, представляющий умный термостат.

**Технические требования:**

1. **Приватный атрибут** `__temperature` для хранения температуры в Цельсиях

2. **Свойство `celsius`:**
   - Геттер возвращает температуру в Цельсиях
   - Сеттер устанавливает температуру с валидацией: допустимый диапазон от -50 до 50 градусов (иначе `ValueError`)

3. **Свойство `fahrenheit`:**
   - Геттер возвращает температуру в Фаренгейтах (формула: `C * 9/5 + 32`)
   - Сеттер принимает температуру в Фаренгейтах и конвертирует в Цельсии (формула: `(F - 32) * 5/9`)

4. **Свойство `kelvin`:**
   - Только для чтения (только геттер)
   - Формула: `C + 273.15`

5. **Метод `is_comfortable()`:**
   - Возвращает `True`, если температура в диапазоне 18-25°C

6. **Метод `adjust(delta)`:**
   - Изменяет температуру на `delta` градусов с проверкой диапазона

**Файл для решения:** `thermostat.py`

### Примеры использования

```python
# Пример 1: Базовая работа со свойствами
t = Thermostat(20)
print(t.celsius)      # 20
print(t.fahrenheit)   # 68.0
