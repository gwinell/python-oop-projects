# python-oop-projects
Проекты по Python сгенерированные нейросетью Claude 4.5 Opus для изучения в формате "learning by doing"
# Серия практических задач по ООП в Python

---

## Задача 1: Счётчик

### Уровень сложности: 1/10

### Изучаемые концепции
- Создание класса с помощью `class`
- Метод `__init__` (конструктор)
- Атрибуты экземпляра
- Методы экземпляра
- Ключевое слово `self`

### Условие

Создайте класс `Counter`, который представляет простой счётчик.

**Технические требования:**

1. Метод `__init__` должен принимать необязательный параметр `start` (начальное значение счётчика, по умолчанию 0)
2. Атрибут `value` хранит текущее значение счётчика
3. Метод `increment()` увеличивает счётчик на 1
4. Метод `decrement()` уменьшает счётчик на 1
5. Метод `reset()` сбрасывает счётчик к начальному значению (которое было передано в `__init__`)
6. Метод `get_value()` возвращает текущее значение

**Файл для сдачи:** `counter.py`

### Примеры использования

```python
# Пример 1: Создание счётчика с начальным значением по умолчанию
counter = Counter()
print(counter.get_value())  # Вывод: 0

# Пример 2: Увеличение и уменьшение
counter = Counter(10)
counter.increment()
counter.increment()
print(counter.get_value())  # Вывод: 12
counter.decrement()
print(counter.get_value())  # Вывод: 11

# Пример 3: Сброс к начальному значению
counter = Counter(5)
counter.increment()
counter.increment()
counter.increment()
print(counter.get_value())  # Вывод: 8
counter.reset()
print(counter.get_value())  # Вывод: 5
```

### Дополнительные задания

1. **Шаг изменения**: Добавьте параметр `step` в `__init__`, чтобы `increment()` и `decrement()` изменяли значение на указанный шаг (по умолчанию 1)
2. **Ограничения**: Добавьте параметры `min_value` и `max_value` (по умолчанию `None`), чтобы счётчик не выходил за границы
3. **История**: Добавьте метод `get_history()`, возвращающий список всех значений счётчика (включая начальное)

### Полезные ссылки для изучения
- "Python class __init__ method"
- "Python self keyword explained"
- "Python instance attributes vs class attributes"
- "Python default parameter values"

---

### Файл тестов: `test_counter.py`

---

## Задача 2: Прямоугольник

### Уровень сложности: 2/10

### Изучаемые концепции
- Атрибуты экземпляра
- Методы, возвращающие вычисленные значения
- Валидация данных в конструкторе
- Магический метод `__str__`
- Выброс исключений

### Условие

Создайте класс `Rectangle`, представляющий прямоугольник.

**Технические требования:**

1. Метод `__init__` принимает два параметра: `width` (ширина) и `height` (высота)
2. Ширина и высота должны быть положительными числами (int или float). При передаче недопустимых значений выбросить `ValueError` с понятным сообщением
3. Метод `area()` возвращает площадь прямоугольника
4. Метод `perimeter()` возвращает периметр прямоугольника
5. Метод `is_square()` возвращает `True`, если прямоугольник является квадратом, иначе `False`
6. Метод `__str__` возвращает строку в формате `"Rectangle(width=X, height=Y)"`

**Файл для сдачи:** `rectangle.py`

### Примеры использования

```python
# Пример 1: Создание и вычисление площади
rect = Rectangle(5, 3)
print(rect.area())  # Вывод: 15

# Пример 2: Периметр и проверка на квадрат
rect = Rectangle(4, 4)
print(rect.perimeter())  # Вывод: 16
print(rect.is_square())  # Вывод: True

# Пример 3: Строковое представление
rect = Rectangle(10, 5)
print(rect)  # Вывод: Rectangle(width=10, height=5)
print(rect.is_square())  # Вывод: False

# Пример 4: Ошибка валидации
try:
    rect = Rectangle(-5, 3)
except ValueError as e:
    print(e)  # Сообщение об ошибке
```

### Дополнительные задания

1. **Масштабирование**: Добавьте метод `scale(factor)`, который умножает размеры на коэффициент (положительное число). При неверном factor выбросить `ValueError`
2. **Вмещение**: Добавьте метод `can_contain(other)`, принимающий другой Rectangle и возвращающий `True`, если текущий прямоугольник может вместить другой (с учётом возможного поворота)
3. **Диагональ**: Добавьте метод `diagonal()`, возвращающий длину диагонали

### Полезные ссылки для изучения
- "Python __str__ method"
- "Python raise ValueError"
- "Python isinstance check type"
- "Python math module sqrt"

---

### Файл тестов: `test_rectangle.py`

---

## Задача 3: Банковский счёт

### Уровень сложности: 3/10

### Изучаемые концепции
- Инкапсуляция (защищённые атрибуты с `_`)
- Управление состоянием объекта
- Методы с валидацией и побочными эффектами
- Работа с историей операций

### Условие

Создайте класс `BankAccount`, представляющий банковский счёт.

**Технические требования:**

1. Метод `__init__` принимает `owner` (имя владельца, непустая строка) и необязательный `balance` (начальный баланс, по умолчанию 0, не может быть отрицательным)
2. Баланс должен храниться в защищённом атрибуте `_balance`
3. Атрибут `owner` хранит имя владельца
4. Метод `deposit(amount)` пополняет счёт на указанную сумму (положительное число)
5. Метод `withdraw(amount)` снимает деньги со счёта. Если денег недостаточно, выбросить `ValueError` с сообщением "Недостаточно средств"
6. Метод `get_balance()` возвращает текущий баланс
7. Метод `__str__` возвращает строку в формате `"BankAccount(owner='Имя', balance=X)"`

**Файл для сдачи:** `bank_account.py`

### Примеры использования

```python
# Пример 1: Создание счёта и пополнение
account = BankAccount("Иван Петров")
account.deposit(1000)
print(account.get_balance())  # Вывод: 1000

# Пример 2: Снятие денег
account = BankAccount("Мария Сидорова", 5000)
account.withdraw(2000)
print(account.get_balance())  # Вывод: 3000

# Пример 3: Недостаточно средств
account = BankAccount("Алексей", 100)
try:
    account.withdraw(500)
except ValueError as e:
    print(e)  # Вывод: Недостаточно средств

# Пример 4: Строковое представление
account = BankAccount("Ольга", 1500)
print(account)  # Вывод: BankAccount(owner='Ольга', balance=1500)
```

### Дополнительные задания

1. **История транзакций**: Добавьте метод `get_transaction_history()`, возвращающий список словарей с информацией о транзакциях (тип: 'deposit'/'withdraw'/'initial', сумма, баланс после)
2. **Перевод**: Добавьте метод `transfer(other_account, amount)` для перевода денег на другой счёт (BankAccount). Должен выбрасывать TypeError если other_account не BankAccount
3. **Начисление процентов**: Добавьте метод `apply_interest(rate)`, который начисляет процент на остаток (rate — дробное число, например 0.05 для 5%)

### Полезные ссылки для изучения
- "Python private and protected attributes"
- "Python encapsulation"
- "Python naming conventions underscore"
- "Python property decorator"

---

### Файл тестов: `test_bank_account.py`


---

## Задача 4: Книга и Библиотека

### Уровень сложности: 4/10

### Изучаемые концепции
- Композиция (объект содержит другие объекты)
- Работа с коллекциями объектов
- Поиск и фильтрация
- Взаимодействие между классами

### Условие

Создайте два класса: `Book` (книга) и `Library` (библиотека).

**Класс Book:**
1. Метод `__init__` принимает: `title` (название), `author` (автор), `year` (год издания), `isbn` (уникальный идентификатор)
2. Атрибут `is_available` (по умолчанию `True`)
3. Метод `__str__` возвращает информацию о книге

**Класс Library:**
1. Метод `__init__` инициализирует пустую коллекцию книг
2. Метод `add_book(book)` добавляет книгу (принимает только Book)
3. Метод `remove_book(isbn)` удаляет книгу по ISBN, выбрасывает `KeyError` если не найдена
4. Метод `find_by_title(title)` — поиск по названию (частичное совпадение, без учёта регистра), возвращает список
5. Метод `find_by_author(author)` — поиск по автору (частичное совпадение, без учёта регистра), возвращает список
6. Метод `get_available_books()` — возвращает список доступных книг
7. Метод `borrow_book(isbn)` — выдаёт книгу (меняет `is_available` на `False`). Выбрасывает `KeyError` если книга не найдена, `ValueError` если уже выдана
8. Метод `return_book(isbn)` — возвращает книгу. Выбрасывает `KeyError` если не найдена, `ValueError` если не была выдана

**Файлы для сдачи:** `book.py` и `library.py` (или один файл `library.py` с обоими классами)

### Примеры использования

```python
# Создание книг
book1 = Book("Война и мир", "Лев Толстой", 1869, "978-5-17-090000-1")
book2 = Book("Анна Каренина", "Лев Толстой", 1877, "978-5-17-090000-2")
book3 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "978-5-17-090000-3")

# Создание библиотеки
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Поиск
tolstoy_books = library.find_by_author("Толстой")  # [book1, book2]
war_books = library.find_by_title("война")          # [book1]

# Выдача и возврат
library.borrow_book("978-5-17-090000-1")
available = library.get_available_books()           # [book2, book3]
library.return_book("978-5-17-090000-1")
```

### Дополнительные задания

1. **Статистика**: Метод `get_statistics()` возвращает словарь: `{'total': N, 'available': M, 'borrowed': K, 'by_author': {'Автор1': X, ...}}`
2. **Сортировка**: Метод `get_books_sorted_by(field)` где field — 'title', 'author' или 'year'. Выбрасывает `ValueError` для неверного поля
3. **Экспорт**: Метод `to_dict()` для Book, метод `export_to_json(filename=None)` для Library (если filename=None, возвращает JSON-строку)

### Полезные ссылки для изучения
- "Python composition vs inheritance"
- "Python list comprehension filter"
- "Python string lower() method"
- "Python json module"

---

### Файл тестов: `test_library.py`

## Задача 5: Геометрические фигуры (Наследование)

### Уровень сложности: 5/10

### Изучаемые концепции
- Наследование классов
- Базовый класс и подклассы
- Переопределение методов (override)
- Вызов методов родителя через `super()`
- Абстрактная логика в базовом классе

### Условие

Создайте иерархию классов для геометрических фигур.

**Базовый класс Shape:**
1. Метод `__init__` принимает `name` (название фигуры)
2. Метод `area()` возвращает 0 (будет переопределён в подклассах)
3. Метод `perimeter()` возвращает 0 (будет переопределён в подклассах)
4. Метод `describe()` возвращает строку: `"{name}: площадь = {area}, периметр = {perimeter}"`

**Класс Circle (наследуется от Shape):**
1. Метод `__init__` принимает `radius` (радиус, положительное число)
2. Переопределяет `area()` — возвращает площадь круга (π * r²)
3. Переопределяет `perimeter()` — возвращает длину окружности (2 * π * r)

**Класс Rectangle (наследуется от Shape):**
1. Метод `__init__` принимает `width` и `height` (положительные числа)
2. Переопределяет `area()` и `perimeter()`
3. Метод `is_square()` возвращает `True`, если это квадрат

**Класс Triangle (наследуется от Shape):**
1. Метод `__init__` принимает три стороны `a`, `b`, `c` (положительные числа)
2. Валидация: стороны должны образовывать треугольник (сумма любых двух сторон > третьей), иначе `ValueError`
3. Переопределяет `area()` (формула Герона) и `perimeter()`

**Файл для сдачи:** `shapes.py`

### Примеры использования

```python
import math

circle = Circle(5)
print(circle.area())       # ≈ 78.54
print(circle.perimeter())  # ≈ 31.42
print(circle.describe())   # "Circle: площадь = 78.54..., периметр = 31.42..."

rect = Rectangle(4, 6)
print(rect.area())         # 24
print(rect.is_square())    # False

square = Rectangle(5, 5)
print(square.is_square())  # True

triangle = Triangle(3, 4, 5)
print(triangle.area())     # 6.0
print(triangle.perimeter()) # 12
```

### Дополнительные задания

1. **Класс Square**: Создайте класс `Square`, наследующийся от `Rectangle`, принимающий только одну сторону
2. **Сравнение**: Добавьте метод `__eq__` в Shape для сравнения фигур по площади
3. **Сравнение больше/меньше**: Добавьте методы `__lt__`, `__gt__` для сравнения фигур по площади

### Полезные ссылки для изучения
- "Python class inheritance"
- "Python super() function"
- "Python method overriding"
- "Python math.pi"
- "Heron's formula"

---

### Файл тестов: `test_shapes.py`

---

## Задача 6: Система сотрудников

### Уровень сложности: 6/10

### Изучаемые концепции
- Полиморфизм
- Наследование с разным поведением
- Абстрактные методы (концептуально)
- Работа с коллекциями разнотипных объектов

### Условие

Создайте систему для управления сотрудниками компании.

**Базовый класс Employee:**
1. Метод `__init__` принимает: `name` (имя), `employee_id` (ID сотрудника), `base_salary` (базовая зарплата)
2. Метод `calculate_salary()` возвращает базовую зарплату (будет переопределён)
3. Метод `get_info()` возвращает строку с информацией о сотруднике
4. Метод `__str__` возвращает краткую информацию

**Класс Manager (наследуется от Employee):**
1. Дополнительный атрибут `bonus` (бонус, по умолчанию 0)
2. Метод `calculate_salary()` возвращает `base_salary + bonus`
3. Метод `set_bonus(amount)` устанавливает бонус

**Класс Developer (наследуется от Employee):**
1. Дополнительный атрибут `programming_languages` (список языков, по умолчанию пустой)
2. Метод `calculate_salary()` возвращает `base_salary + 1000 * количество_языков`
3. Метод `add_language(language)` добавляет язык в список

**Класс Intern (наследуется от Employee):**
1. Дополнительный атрибут `duration_months` (срок стажировки в месяцах)
2. Метод `calculate_salary()` возвращает `base_salary * 0.5` (стажёры получают половину)

**Класс Company:**
1. Метод `__init__` принимает `name` (название компании)
2. Метод `add_employee(employee)` добавляет сотрудника
3. Метод `get_total_salaries()` возвращает сумму зарплат всех сотрудников
4. Метод `get_employees_by_type(employee_type)` возвращает список сотрудников указанного типа
5. Метод `fire_employee(employee_id)` удаляет сотрудника по ID

**Файл для сдачи:** `employees.py`

### Примеры использования

```python
# Создание сотрудников
manager = Manager("Иван", "M001", 100000)
manager.set_bonus(20000)

dev = Developer("Мария", "D001", 80000)
dev.add_language("Python")
dev.add_language("JavaScript")

intern = Intern("Алексей", "I001", 40000, duration_months=3)

# Компания
company = Company("TechCorp")
company.add_employee(manager)
company.add_employee(dev)
company.add_employee(intern)

print(manager.calculate_salary())  # 120000
print(dev.calculate_salary())      # 82000
print(intern.calculate_salary())   # 20000

print(company.get_total_salaries())  # 222000
```

### Дополнительные задания

1. **SalesPerson**: Класс с атрибутом `sales_amount` и комиссией 5% от продаж
2. **Отчёт**: Метод `generate_report()` в Company, возвращающий детальный отчёт
3. **Повышение**: Метод `give_raise(employee_id, amount)` в Company

### Полезные ссылки для изучения
- "Python polymorphism"
- "Python isinstance vs type"
- "Python abstract base class"

---

### Файл тестов: `test_employees.py`


---

## Задача 7: Стек и Очередь

### Уровень сложности: 6/10

### Изучаемые концепции
- Реализация структур данных
- Магические методы `__len__`, `__bool__`, `__iter__`
- Исключения для особых ситуаций
- Итераторы

### Условие

Реализуйте два класса: `Stack` (стек, LIFO) и `Queue` (очередь, FIFO).

**Класс Stack (Last In, First Out):**
1. Метод `__init__` создаёт пустой стек (можно передать iterable для начальной инициализации)
2. Метод `push(item)` добавляет элемент на вершину стека
3. Метод `pop()` удаляет и возвращает элемент с вершины. Если стек пуст — выбросить `IndexError` с сообщением "Stack is empty"
4. Метод `peek()` возвращает элемент с вершины без удаления. Если пуст — `IndexError`
5. Метод `is_empty()` возвращает `True`, если стек пуст
6. `__len__` возвращает количество элементов
7. `__bool__` возвращает `True`, если стек не пуст
8. `__iter__` позволяет итерироваться по стеку (от вершины к основанию)

**Класс Queue (First In, First Out):**
1. Метод `__init__` создаёт пустую очередь (можно передать iterable)
2. Метод `enqueue(item)` добавляет элемент в конец очереди
3. Метод `dequeue()` удаляет и возвращает элемент из начала. Если пуста — `IndexError` с сообщением "Queue is empty"
4. Метод `front()` возвращает первый элемент без удаления
5. Метод `is_empty()` возвращает `True`, если очередь пуста
6. `__len__`, `__bool__`, `__iter__` аналогично Stack

**Файл для сдачи:** `data_structures.py`

### Примеры использования

```python
# Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3
print(stack.peek())  # 2
print(len(stack))    # 2

for item in stack:
    print(item)  # 2, 1

# Queue
queue = Queue([1, 2, 3])
print(queue.dequeue())  # 1
queue.enqueue(4)
print(queue.front())    # 2

if queue:
    print("Очередь не пуста")
```

### Дополнительные задания

1. **Метод clear()**: Очищает структуру данных
2. **Метод contains(item)**: Проверяет наличие элемента (также реализовать `__contains__` для оператора `in`)
3. **Ограничение размера**: Параметр `maxsize` в `__init__`. При превышении — `OverflowError`

### Полезные ссылки для изучения
- "Python __len__ __bool__ magic methods"
- "Python __iter__ iterator protocol"
- "Stack data structure"
- "Queue data structure FIFO"

---

### Файл тестов: `test_data_structures.py`



---

## Задача 8: Система логирования (Декораторы классов)

### Уровень сложности: 7/10

### Изучаемые концепции
- Декораторы
- Работа с датой и временем
- Паттерн Singleton
- Уровни логирования

### Условие

Создайте систему логирования с классом `Logger`.

**Класс Logger (Singleton):**
1. Реализует паттерн Singleton — только один экземпляр класса
2. Метод `__init__` принимает необязательный `filename` (если указан — логи пишутся в файл)
3. Уровни логирования: DEBUG, INFO, WARNING, ERROR, CRITICAL (в виде констант класса или Enum)
4. Метод `set_level(level)` устанавливает минимальный уровень логирования
5. Методы `debug(message)`, `info(message)`, `warning(message)`, `error(message)`, `critical(message)`
6. Формат записи: `"[УРОВЕНЬ] YYYY-MM-DD HH:MM:SS - сообщение"`
7. Метод `get_logs()` возвращает список всех записей
8. Метод `get_logs_by_level(level)` фильтрует записи по уровню

**Декоратор @log_calls:**
1. Создайте декоратор `log_calls`, который логирует вызовы функций/методов
2. Логирует: имя функции, аргументы, результат, время выполнения

**Файл для сдачи:** `logger.py`

### Примеры использования

```python
# Singleton
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True

# Логирование
logger = Logger()
logger.set_level(Logger.INFO)
logger.debug("Это не выведется")  # уровень ниже INFO
logger.info("Информация")
logger.warning("Предупреждение")
logger.error("Ошибка")

for log in logger.get_logs():
    print(log)

# Декоратор
@log_calls
def add(a, b):
    return a + b

result = add(2, 3)  # Логирует вызов
```

### Дополнительные задания

1. **Запись в файл**: Полная реализация записи в файл
2. **Форматтер**: Метод `set_format(format_string)` для настройки формата вывода
3. **Контекстный менеджер**: Реализовать `__enter__`/`__exit__` для временного изменения уровня

### Полезные ссылки для изучения
- "Python singleton pattern"
- "Python datetime strftime"
- "Python decorator with arguments"
- "Python Enum class"

---

### Файл тестов: `test_logger.py`



## Задача 9: Интернет-магазин (Комплексная система)

### Уровень сложности: 8/10

### Изучаемые концепции
- Комплексное взаимодействие множества классов
- Агрегация и композиция
- Управление состоянием
- Бизнес-логика в методах
- Исключения для бизнес-правил

### Условие

Создайте систему интернет-магазина с несколькими взаимосвязанными классами.

**Класс Product:**
1. Метод `__init__` принимает: `product_id`, `name`, `price`, `quantity` (количество на складе)
2. Все параметры валидируются (price > 0, quantity >= 0)
3. Метод `is_available(amount=1)` проверяет, доступно ли указанное количество
4. Метод `reduce_stock(amount)` уменьшает количество на складе
5. Метод `restock(amount)` пополняет склад
6. Метод `__str__` возвращает информацию о товаре

**Класс CartItem:**
1. Связывает Product с количеством в корзине
2. Метод `__init__` принимает `product` и `quantity`
3. Метод `get_total()` возвращает стоимость (цена × количество)
4. Метод `update_quantity(new_quantity)` изменяет количество

**Класс ShoppingCart:**
1. Метод `add_item(product, quantity)` добавляет товар в корзину. Если товар уже есть — увеличивает количество
2. Метод `remove_item(product_id)` удаляет товар из корзины
3. Метод `update_item_quantity(product_id, quantity)` изменяет количество товара
4. Метод `get_total()` возвращает общую стоимость корзины
5. Метод `get_items()` возвращает список CartItem
6. Метод `clear()` очищает корзину
7. `__len__` возвращает количество уникальных товаров

**Класс Order:**
1. Метод `__init__` принимает `order_id`, `cart` (ShoppingCart), `customer_name`
2. Статусы заказа: PENDING, CONFIRMED, SHIPPED, DELIVERED, CANCELLED
3. Метод `confirm()` подтверждает заказ и списывает товары со склада
4. Метод `cancel()` отменяет заказ (если не SHIPPED/DELIVERED) и возвращает товары на склад
5. Метод `ship()` отправляет заказ (только из статуса CONFIRMED)
6. Метод `deliver()` доставляет заказ (только из статуса SHIPPED)
7. Метод `get_total()` возвращает сумму заказа

**Класс Store:**
1. Управляет товарами и заказами
2. Метод `add_product(product)` добавляет товар в каталог
3. Метод `get_product(product_id)` возвращает товар по ID
4. Метод `create_order(cart, customer_name)` создаёт заказ
5. Метод `get_order(order_id)` возвращает заказ
6. Метод `get_available_products()` возвращает товары в наличии

**Файл для сдачи:** `shop.py`

### Примеры использования

```python
# Создание магазина и товаров
store = Store("TechShop")
laptop = Product("P001", "Ноутбук", 50000, 10)
mouse = Product("P002", "Мышь", 1500, 50)
store.add_product(laptop)
store.add_product(mouse)

# Корзина покупателя
cart = ShoppingCart()
cart.add_item(laptop, 2)
cart.add_item(mouse, 3)
print(cart.get_total())  # 104500

# Оформление заказа
order = store.create_order(cart, "Иван Петров")
order.confirm()  # Списывает товары со склада
print(laptop.quantity)  # 8

order.ship()
order.deliver()
print(order.status)  # DELIVERED
```

### Дополнительные задания

1. **Скидки**: Класс `Discount` с методами применения скидки (процент или фиксированная сумма). Метод `apply_discount(discount)` в Cart
2. **История заказов**: Метод `get_order_history(customer_name)` в Store
3. **Уведомления**: Метод `subscribe(callback)` в Order, вызывающий callback при смене статуса

### Полезные ссылки для изучения
- "Python enum for status"
- "Python aggregation vs composition"
- "State pattern Python"
- "Python callback functions"

---

### Файл тестов: `test_shop.py`

---

## Задача 10: ORM-подобная система (Дескрипторы и метаклассы)

### Уровень сложности: 10/10

### Изучаемые концепции
- Дескрипторы (`__get__`, `__set__`, `__delete__`)
- Метаклассы (опционально)
- Валидация на уровне атрибутов
- Паттерн Active Record
- Сериализация/десериализация

### Условие

Создайте упрощённую ORM-подобную систему для работы с "моделями" данных.

**Дескрипторы-валидаторы (классы полей):**

1. **Field** — базовый класс дескриптора:
   - Параметры: `required` (обязательное, по умолчанию True), `default` (значение по умолчанию)
   - Метод `validate(value)` — базовая валидация (проверка на None если required)

2. **StringField(Field)**:
   - Дополнительные параметры: `min_length`, `max_length`
   - Проверяет, что значение — строка нужной длины

3. **IntegerField(Field)**:
   - Дополнительные параметры: `min_value`, `max_value`
   - Проверяет, что значение — целое число в диапазоне

4. **EmailField(StringField)**:
   - Проверяет формат email (содержит @ и точку после @)

5. **BooleanField(Field)**:
   - Проверяет, что значение — булево

**Класс Model:**
1. Базовый класс для всех моделей
2. При создании экземпляра принимает именованные аргументы для полей
3. Метод `validate()` проверяет все поля и возвращает список ошибок (или пустой список)
4. Метод `is_valid()` возвращает True, если валидация прошла
5. Метод `to_dict()` сериализует модель в словарь
6. Класс-метод `from_dict(data)` создаёт экземпляр из словаря
7. Метод `__str__` возвращает читаемое представление
8. Метод `__eq__` сравнивает модели по значениям полей

**Файл для сдачи:** `orm.py`

### Примеры использования

```python
class User(Model):
    username = StringField(min_length=3, max_length=20)
    email = EmailField()
    age = IntegerField(min_value=0, max_value=150, required=False, default=None)
    is_active = BooleanField(default=True)


# Создание пользователя
user = User(username="john_doe", email="john@example.com", age=25)
print(user.username)  # john_doe
print(user.is_valid())  # True

# Валидация
invalid_user = User(username="ab", email="invalid-email")
print(invalid_user.is_valid())  # False
errors = invalid_user.validate()
print(errors)  # ['username: минимальная длина 3', 'email: неверный формат']

# Сериализация
data = user.to_dict()
print(data)  # {'username': 'john_doe', 'email': 'john@example.com', 'age': 25, 'is_active': True}

# Десериализация
user2 = User.from_dict(data)
print(user == user2)  # True
```

### Дополнительные задания

1. **ListField**: Поле для списка с валидацией типа элементов
2. **DateField**: Поле для даты с форматом
3. **Вложенные модели**: Возможность использовать Model как тип поля (ForeignKey-подобное поведение)

### Полезные ссылки для изучения
- "Python descriptors __get__ __set__"
- "Python descriptor protocol"
- "Python metaclass"
- "Active Record pattern"
- "Python ORM design"

---

### Файл тестов: `test_orm.py`

---

## Сводная таблица задач

| № | Название | Сложность | Основные концепции |
|---|----------|-----------|-------------------|
| 1 | Счётчик | 1/10 | Классы, `__init__`, атрибуты, методы |
| 2 | Прямоугольник | 2/10 | Валидация, `__str__`, вычисляемые свойства |
| 3 | Банковский счёт | 3/10 | Инкапсуляция, защищённые атрибуты |
| 4 | Книга и Библиотека | 4/10 | Композиция, коллекции объектов |
| 5 | Геометрические фигуры | 5/10 | Наследование, `super()`, переопределение |
| 6 | Система сотрудников | 6/10 | Полиморфизм, разное поведение подклассов |
| 7 | Стек и Очередь | 6/10 | Структуры данных, `__len__`, `__iter__` |
| 8 | Система логирования | 7/10 | Singleton, декораторы, уровни |
| 9 | Интернет-магазин | 8/10 | Комплексная система, состояния, бизнес-логика |
| 10 | ORM-система | 10/10 | Дескрипторы, метаклассы, валидация |
