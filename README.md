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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from counter import Counter


class TestCounterBasic(unittest.TestCase):
    """Тесты базовой функциональности счётчика."""
    
    def test_default_initialization(self):
        """Счётчик создаётся со значением 0 по умолчанию."""
        counter = Counter()
        self.assertEqual(counter.get_value(), 0)
    
    def test_value_attribute_exists(self):
        """Атрибут value существует и доступен."""
        counter = Counter()
        self.assertEqual(counter.value, 0)
    
    def test_custom_initialization(self):
        """Счётчик создаётся с заданным начальным значением."""
        counter = Counter(10)
        self.assertEqual(counter.get_value(), 10)
    
    def test_negative_initialization(self):
        """Счётчик может начинаться с отрицательного значения."""
        counter = Counter(-5)
        self.assertEqual(counter.get_value(), -5)
    
    def test_increment_once(self):
        """increment() увеличивает счётчик на 1."""
        counter = Counter(0)
        counter.increment()
        self.assertEqual(counter.get_value(), 1)
    
    def test_increment_multiple(self):
        """Несколько вызовов increment() работают корректно."""
        counter = Counter(0)
        counter.increment()
        counter.increment()
        counter.increment()
        self.assertEqual(counter.get_value(), 3)
    
    def test_decrement_once(self):
        """decrement() уменьшает счётчик на 1."""
        counter = Counter(10)
        counter.decrement()
        self.assertEqual(counter.get_value(), 9)
    
    def test_decrement_multiple(self):
        """Несколько вызовов decrement() работают корректно."""
        counter = Counter(10)
        counter.decrement()
        counter.decrement()
        counter.decrement()
        self.assertEqual(counter.get_value(), 7)
    
    def test_decrement_below_zero(self):
        """Счётчик может уходить в отрицательные значения."""
        counter = Counter(1)
        counter.decrement()
        counter.decrement()
        self.assertEqual(counter.get_value(), -1)
    
    def test_reset_to_default(self):
        """reset() сбрасывает к значению 0 (по умолчанию)."""
        counter = Counter()
        counter.increment()
        counter.increment()
        counter.reset()
        self.assertEqual(counter.get_value(), 0)
    
    def test_reset_to_custom_start(self):
        """reset() сбрасывает к заданному начальному значению."""
        counter = Counter(5)
        counter.increment()
        counter.increment()
        counter.increment()
        self.assertEqual(counter.get_value(), 8)
        counter.reset()
        self.assertEqual(counter.get_value(), 5)
    
    def test_combined_operations(self):
        """Комбинация операций работает корректно."""
        counter = Counter(100)
        counter.increment()   # 101
        counter.increment()   # 102
        counter.decrement()   # 101
        counter.increment()   # 102
        counter.decrement()   # 101
        counter.decrement()   # 100
        counter.decrement()   # 99
        self.assertEqual(counter.get_value(), 99)
    
    def test_reset_after_operations(self):
        """reset() работает после серии операций."""
        counter = Counter(50)
        for _ in range(10):
            counter.increment()
        for _ in range(5):
            counter.decrement()
        counter.reset()
        self.assertEqual(counter.get_value(), 50)


class TestCounterStep(unittest.TestCase):
    """Тесты дополнительного задания: шаг изменения."""
    
    def test_custom_step_initialization(self):
        """Счётчик принимает параметр step."""
        counter = Counter(0, step=5)
        self.assertEqual(counter.get_value(), 0)
    
    def test_increment_with_custom_step(self):
        """increment() увеличивает на заданный шаг."""
        counter = Counter(0, step=5)
        counter.increment()
        self.assertEqual(counter.get_value(), 5)
        counter.increment()
        self.assertEqual(counter.get_value(), 10)
    
    def test_decrement_with_custom_step(self):
        """decrement() уменьшает на заданный шаг."""
        counter = Counter(100, step=10)
        counter.decrement()
        self.assertEqual(counter.get_value(), 90)
        counter.decrement()
        self.assertEqual(counter.get_value(), 80)
    
    def test_step_with_reset(self):
        """reset() работает корректно при использовании step."""
        counter = Counter(50, step=7)
        counter.increment()
        counter.increment()
        self.assertEqual(counter.get_value(), 64)
        counter.reset()
        self.assertEqual(counter.get_value(), 50)
    
    def test_default_step_is_one(self):
        """По умолчанию шаг равен 1."""
        counter = Counter(0)
        counter.increment()
        self.assertEqual(counter.get_value(), 1)


class TestCounterLimits(unittest.TestCase):
    """Тесты дополнительного задания: ограничения."""
    
    def test_max_value_limit(self):
        """Счётчик не превышает max_value."""
        counter = Counter(8, max_value=10)
        counter.increment()  # 9
        counter.increment()  # 10
        counter.increment()  # должно остаться 10
        self.assertEqual(counter.get_value(), 10)
    
    def test_min_value_limit(self):
        """Счётчик не опускается ниже min_value."""
        counter = Counter(2, min_value=0)
        counter.decrement()  # 1
        counter.decrement()  # 0
        counter.decrement()  # должно остаться 0
        self.assertEqual(counter.get_value(), 0)
    
    def test_both_limits(self):
        """Оба ограничения работают одновременно."""
        counter = Counter(5, min_value=0, max_value=10)
        
        for _ in range(10):
            counter.increment()
        self.assertEqual(counter.get_value(), 10)
        
        for _ in range(20):
            counter.decrement()
        self.assertEqual(counter.get_value(), 0)
    
    def test_no_limits_by_default(self):
        """По умолчанию ограничений нет."""
        counter = Counter(0)
        for _ in range(1000):
            counter.increment()
        self.assertEqual(counter.get_value(), 1000)
        
        for _ in range(2000):
            counter.decrement()
        self.assertEqual(counter.get_value(), -1000)


class TestCounterHistory(unittest.TestCase):
    """Тесты дополнительного задания: история."""
    
    def test_initial_history(self):
        """История содержит начальное значение."""
        counter = Counter(5)
        history = counter.get_history()
        self.assertEqual(history, [5])
    
    def test_history_after_increment(self):
        """История обновляется после increment()."""
        counter = Counter(0)
        counter.increment()
        counter.increment()
        history = counter.get_history()
        self.assertEqual(history, [0, 1, 2])
    
    def test_history_after_decrement(self):
        """История обновляется после decrement()."""
        counter = Counter(5)
        counter.decrement()
        counter.decrement()
        history = counter.get_history()
        self.assertEqual(history, [5, 4, 3])
    
    def test_history_after_reset(self):
        """История обновляется после reset()."""
        counter = Counter(10)
        counter.increment()
        counter.reset()
        history = counter.get_history()
        self.assertEqual(history, [10, 11, 10])
    
    def test_history_is_copy(self):
        """get_history() возвращает копию списка."""
        counter = Counter(0)
        history = counter.get_history()
        history.append(999)
        self.assertEqual(counter.get_history(), [0])
    
    def test_history_combined_operations(self):
        """История корректна после комбинации операций."""
        counter = Counter(0)
        counter.increment()   # 1
        counter.increment()   # 2
        counter.decrement()   # 1
        counter.reset()       # 0
        history = counter.get_history()
        self.assertEqual(history, [0, 1, 2, 1, 0])


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestCounterBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestCounterStep))
    suite.addTests(loader.loadTestsFromTestCase(TestCounterLimits))
    suite.addTests(loader.loadTestsFromTestCase(TestCounterHistory))
    
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
```

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

```python
import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rectangle import Rectangle


class TestRectangleBasic(unittest.TestCase):
    """Тесты базовой функциональности."""
    
    def test_creation_integers(self):
        """Прямоугольник создаётся с целыми числами."""
        rect = Rectangle(5, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
    
    def test_creation_floats(self):
        """Прямоугольник создаётся с дробными числами."""
        rect = Rectangle(5.5, 3.5)
        self.assertEqual(rect.width, 5.5)
        self.assertEqual(rect.height, 3.5)
    
    def test_area_integers(self):
        """area() корректно вычисляет площадь для целых чисел."""
        rect = Rectangle(5, 3)
        self.assertEqual(rect.area(), 15)
    
    def test_area_floats(self):
        """area() корректно вычисляет площадь для дробных чисел."""
        rect = Rectangle(2.5, 4)
        self.assertEqual(rect.area(), 10)
    
    def test_area_square(self):
        """area() корректно вычисляет площадь квадрата."""
        rect = Rectangle(4, 4)
        self.assertEqual(rect.area(), 16)
    
    def test_perimeter_integers(self):
        """perimeter() корректно вычисляет периметр."""
        rect = Rectangle(5, 3)
        self.assertEqual(rect.perimeter(), 16)
    
    def test_perimeter_square(self):
        """perimeter() корректно вычисляет периметр квадрата."""
        rect = Rectangle(4, 4)
        self.assertEqual(rect.perimeter(), 16)
    
    def test_perimeter_floats(self):
        """perimeter() работает с дробными числами."""
        rect = Rectangle(2.5, 1.5)
        self.assertEqual(rect.perimeter(), 8)
    
    def test_is_square_true(self):
        """is_square() возвращает True для квадрата."""
        rect = Rectangle(4, 4)
        self.assertTrue(rect.is_square())
    
    def test_is_square_true_floats(self):
        """is_square() работает с дробными числами."""
        rect = Rectangle(3.5, 3.5)
        self.assertTrue(rect.is_square())
    
    def test_is_square_false(self):
        """is_square() возвращает False для не-квадрата."""
        rect = Rectangle(5, 3)
        self.assertFalse(rect.is_square())
    
    def test_str_format(self):
        """__str__() возвращает правильный формат."""
        rect = Rectangle(10, 5)
        self.assertEqual(str(rect), "Rectangle(width=10, height=5)")
    
    def test_str_format_square(self):
        """__str__() для квадрата."""
        rect = Rectangle(4, 4)
        self.assertEqual(str(rect), "Rectangle(width=4, height=4)")
    
    def test_str_format_floats(self):
        """__str__() с дробными числами."""
        rect = Rectangle(3.5, 2.5)
        self.assertEqual(str(rect), "Rectangle(width=3.5, height=2.5)")


class TestRectangleValidation(unittest.TestCase):
    """Тесты валидации входных данных."""
    
    def test_negative_width_raises(self):
        """Отрицательная ширина вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-5, 3)
    
    def test_negative_height_raises(self):
        """Отрицательная высота вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, -3)
    
    def test_both_negative_raises(self):
        """Обе отрицательные величины вызывают ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-5, -3)
    
    def test_zero_width_raises(self):
        """Нулевая ширина вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 3)
    
    def test_zero_height_raises(self):
        """Нулевая высота вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
    
    def test_string_width_raises(self):
        """Строка вместо ширины вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle("5", 3)
    
    def test_string_height_raises(self):
        """Строка вместо высоты вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, "3")
    
    def test_none_width_raises(self):
        """None вместо ширины вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(None, 3)
    
    def test_none_height_raises(self):
        """None вместо высоты вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(5, None)


class TestRectangleScale(unittest.TestCase):
    """Тесты дополнительного задания: масштабирование."""
    
    def test_scale_up_integer(self):
        """scale() увеличивает размеры на целый коэффициент."""
        rect = Rectangle(5, 3)
        rect.scale(2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 6)
    
    def test_scale_down(self):
        """scale() уменьшает размеры."""
        rect = Rectangle(10, 6)
        rect.scale(0.5)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
    
    def test_scale_affects_area(self):
        """scale() влияет на площадь."""
        rect = Rectangle(5, 3)
        rect.scale(2)
        self.assertEqual(rect.area(), 60)
    
    def test_scale_negative_raises(self):
        """Отрицательный коэффициент вызывает ValueError."""
        rect = Rectangle(5, 3)
        with self.assertRaises(ValueError):
            rect.scale(-1)
    
    def test_scale_zero_raises(self):
        """Нулевой коэффициент вызывает ValueError."""
        rect = Rectangle(5, 3)
        with self.assertRaises(ValueError):
            rect.scale(0)
    
    def test_scale_string_raises(self):
        """Строка вместо коэффициента вызывает ValueError."""
        rect = Rectangle(5, 3)
        with self.assertRaises(ValueError):
            rect.scale("2")


class TestRectangleContain(unittest.TestCase):
    """Тесты дополнительного задания: вмещение."""
    
    def test_can_contain_smaller(self):
        """Большой прямоугольник вмещает меньший."""
        big = Rectangle(10, 10)
        small = Rectangle(5, 5)
        self.assertTrue(big.can_contain(small))
    
    def test_cannot_contain_larger(self):
        """Маленький прямоугольник не вмещает большой."""
        small = Rectangle(5, 5)
        big = Rectangle(10, 10)
        self.assertFalse(small.can_contain(big))
    
    def test_can_contain_with_rotation(self):
        """Вмещение с учётом поворота."""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(4, 8)  # 4x8 поместится в 10x5 если повернуть на 8x4
        self.assertTrue(rect1.can_contain(rect2))
    
    def test_can_contain_same_size(self):
        """Равные прямоугольники вмещают друг друга."""
        rect1 = Rectangle(5, 5)
        rect2 = Rectangle(5, 5)
        self.assertTrue(rect1.can_contain(rect2))
    
    def test_can_contain_exact_fit(self):
        """Точное вмещение."""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(10, 5)
        self.assertTrue(rect1.can_contain(rect2))
    
    def test_cannot_contain_slightly_larger(self):
        """Чуть больший прямоугольник не вмещается."""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(10.1, 5)
        self.assertFalse(rect1.can_contain(rect2))
    
    def test_can_contain_invalid_type_raises(self):
        """Неверный тип аргумента вызывает TypeError."""
        rect = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            rect.can_contain("not a rectangle")


class TestRectangleDiagonal(unittest.TestCase):
    """Тесты дополнительного задания: диагональ."""
    
    def test_diagonal_3_4_5(self):
        """Диагональ для классического треугольника 3-4-5."""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.diagonal(), 5)
    
    def test_diagonal_square(self):
        """Диагональ единичного квадрата."""
        rect = Rectangle(1, 1)
        self.assertAlmostEqual(rect.diagonal(), math.sqrt(2), places=10)
    
    def test_diagonal_5_12_13(self):
        """Диагональ для треугольника 5-12-13."""
        rect = Rectangle(5, 12)
        self.assertEqual(rect.diagonal(), 13)
    
    def test_diagonal_floats(self):
        """Диагональ для дробных размеров."""
        rect = Rectangle(1.5, 2)
        expected = math.sqrt(1.5**2 + 2**2)
        self.assertAlmostEqual(rect.diagonal(), expected, places=10)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleScale))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleContain))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleDiagonal))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bank_account import BankAccount


class TestBankAccountBasic(unittest.TestCase):
    """Тесты базовой функциональности."""
    
    def test_creation_default_balance(self):
        """Счёт создаётся с нулевым балансом по умолчанию."""
        account = BankAccount("Иван")
        self.assertEqual(account.get_balance(), 0)
    
    def test_creation_with_balance(self):
        """Счёт создаётся с заданным балансом."""
        account = BankAccount("Мария", 1000)
        self.assertEqual(account.get_balance(), 1000)
    
    def test_owner_attribute(self):
        """Атрибут owner доступен."""
        account = BankAccount("Пётр", 500)
        self.assertEqual(account.owner, "Пётр")
    
    def test_deposit_increases_balance(self):
        """deposit() увеличивает баланс."""
        account = BankAccount("Тест")
        account.deposit(500)
        self.assertEqual(account.get_balance(), 500)
    
    def test_deposit_multiple(self):
        """Несколько пополнений суммируются."""
        account = BankAccount("Тест")
        account.deposit(500)
        account.deposit(300)
        self.assertEqual(account.get_balance(), 800)
    
    def test_withdraw_decreases_balance(self):
        """withdraw() уменьшает баланс."""
        account = BankAccount("Тест", 1000)
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 700)
    
    def test_withdraw_all(self):
        """Можно снять весь баланс."""
        account = BankAccount("Тест", 500)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 0)
    
    def test_str_format(self):
        """__str__() возвращает правильный формат."""
        account = BankAccount("Ольга", 1500)
        self.assertEqual(str(account), "BankAccount(owner='Ольга', balance=1500)")
    
    def test_str_zero_balance(self):
        """__str__() с нулевым балансом."""
        account = BankAccount("Тест")
        self.assertEqual(str(account), "BankAccount(owner='Тест', balance=0)")
    
    def test_combined_operations(self):
        """Комбинация операций работает корректно."""
        account = BankAccount("Тест", 1000)
        account.deposit(500)   # 1500
        account.withdraw(200)  # 1300
        account.deposit(100)   # 1400
        account.withdraw(400)  # 1000
        self.assertEqual(account.get_balance(), 1000)


class TestBankAccountValidation(unittest.TestCase):
    """Тесты валидации."""
    
    def test_negative_initial_balance_raises(self):
        """Отрицательный начальный баланс вызывает ValueError."""
        with self.assertRaises(ValueError):
            BankAccount("Тест", -100)
    
    def test_empty_owner_raises(self):
        """Пустое имя владельца вызывает ValueError."""
        with self.assertRaises(ValueError):
            BankAccount("")
    
    def test_whitespace_owner_raises(self):
        """Имя из пробелов вызывает ValueError."""
        with self.assertRaises(ValueError):
            BankAccount("   ")
    
    def test_deposit_negative_raises(self):
        """Отрицательная сумма пополнения вызывает ValueError."""
        account = BankAccount("Тест")
        with self.assertRaises(ValueError):
            account.deposit(-100)
    
    def test_deposit_zero_raises(self):
        """Нулевая сумма пополнения вызывает ValueError."""
        account = BankAccount("Тест")
        with self.assertRaises(ValueError):
            account.deposit(0)
    
    def test_withdraw_insufficient_funds(self):
        """Снятие больше баланса вызывает ValueError."""
        account = BankAccount("Тест", 100)
        with self.assertRaises(ValueError) as context:
            account.withdraw(500)
        self.assertIn("Недостаточно средств", str(context.exception))
    
    def test_withdraw_negative_raises(self):
        """Отрицательная сумма снятия вызывает ValueError."""
        account = BankAccount("Тест", 1000)
        with self.assertRaises(ValueError):
            account.withdraw(-100)
    
    def test_withdraw_zero_raises(self):
        """Нулевая сумма снятия вызывает ValueError."""
        account = BankAccount("Тест", 1000)
        with self.assertRaises(ValueError):
            account.withdraw(0)


class TestBankAccountEncapsulation(unittest.TestCase):
    """Тесты инкапсуляции."""
    
    def test_balance_is_protected(self):
        """Баланс хранится в защищённом атрибуте _balance."""
        account = BankAccount("Тест", 1000)
        self.assertTrue(hasattr(account, '_balance'))
        self.assertEqual(account._balance, 1000)
    
    def test_balance_not_public(self):
        """Публичного атрибута balance нет (или это property)."""
        account = BankAccount("Тест", 1000)
        # Если balance существует, он должен совпадать с _balance
        if hasattr(account, 'balance'):
            self.assertEqual(account.balance, account._balance)


class TestBankAccountHistory(unittest.TestCase):
    """Тесты дополнительного задания: история транзакций."""
    
    def test_history_exists(self):
        """Метод get_transaction_history() существует."""
        account = BankAccount("Тест", 1000)
        self.assertTrue(hasattr(account, 'get_transaction_history'))
    
    def test_history_initial_deposit(self):
        """История содержит начальный депозит."""
        account = BankAccount("Тест", 1000)
        history = account.get_transaction_history()
        self.assertIsInstance(history, list)
        self.assertGreater(len(history), 0)
    
    def test_history_after_deposit(self):
        """История обновляется после пополнения."""
        account = BankAccount("Тест")
        account.deposit(500)
        history = account.get_transaction_history()
        deposit_records = [h for h in history if h.get('type') == 'deposit']
        self.assertGreater(len(deposit_records), 0)
    
    def test_history_after_withdraw(self):
        """История обновляется после снятия."""
        account = BankAccount("Тест", 1000)
        account.withdraw(300)
        history = account.get_transaction_history()
        withdraw_records = [h for h in history if h.get('type') == 'withdraw']
        self.assertGreater(len(withdraw_records), 0)
    
    def test_history_contains_amount(self):
        """Запись в истории содержит сумму."""
        account = BankAccount("Тест")
        account.deposit(500)
        history = account.get_transaction_history()
        last_record = history[-1]
        self.assertIn('amount', last_record)
        self.assertEqual(last_record['amount'], 500)


class TestBankAccountTransfer(unittest.TestCase):
    """Тесты дополнительного задания: переводы."""
    
    def test_transfer_success(self):
        """Успешный перевод между счетами."""
        account1 = BankAccount("Отправитель", 1000)
        account2 = BankAccount("Получатель", 500)
        account1.transfer(account2, 300)
        self.assertEqual(account1.get_balance(), 700)
        self.assertEqual(account2.get_balance(), 800)
    
    def test_transfer_insufficient_funds(self):
        """Перевод при недостаточных средствах вызывает ValueError."""
        account1 = BankAccount("Отправитель", 100)
        account2 = BankAccount("Получатель", 500)
        with self.assertRaises(ValueError):
            account1.transfer(account2, 500)
    
    def test_transfer_to_self_raises(self):
        """Перевод самому себе вызывает ValueError."""
        account = BankAccount("Тест", 1000)
        with self.assertRaises(ValueError):
            account.transfer(account, 100)
    
    def test_transfer_invalid_recipient_raises(self):
        """Перевод не на BankAccount вызывает TypeError."""
        account = BankAccount("Тест", 1000)
        with self.assertRaises(TypeError):
            account.transfer("не счёт", 100)
    
    def test_transfer_negative_amount_raises(self):
        """Отрицательная сумма перевода вызывает ValueError."""
        account1 = BankAccount("Отправитель", 1000)
        account2 = BankAccount("Получатель", 500)
        with self.assertRaises(ValueError):
            account1.transfer(account2, -100)


class TestBankAccountInterest(unittest.TestCase):
    """Тесты дополнительного задания: проценты."""
    
    def test_apply_interest(self):
        """apply_interest() начисляет проценты."""
        account = BankAccount("Тест", 1000)
        account.apply_interest(0.1)  # 10%
        self.assertEqual(account.get_balance(), 1100)
    
    def test_apply_interest_5_percent(self):
        """Начисление 5%."""
        account = BankAccount("Тест", 1000)
        account.apply_interest(0.05)
        self.assertEqual(account.get_balance(), 1050)
    
    def test_apply_interest_zero_balance(self):
        """Начисление процентов на нулевой баланс."""
        account = BankAccount("Тест", 0)
        account.apply_interest(0.1)
        self.assertEqual(account.get_balance(), 0)
    
    def test_apply_interest_negative_rate_raises(self):
        """Отрицательная ставка вызывает ValueError."""
        account = BankAccount("Тест", 1000)
        with self.assertRaises(ValueError):
            account.apply_interest(-0.05)
    
    def test_apply_interest_zero_rate(self):
        """Нулевая ставка не меняет баланс."""
        account = BankAccount("Тест", 1000)
        account.apply_interest(0)
        self.assertEqual(account.get_balance(), 1000)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountEncapsulation))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountHistory))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountTransfer))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountInterest))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from library import Book, Library


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


class TestLibrarySorting(unittest.TestCase):
    """Тесты дополнительного задания: сортировка."""
    
    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("Яблоко", "Иванов", 2002, "isbn-1"))
        self.library.add_book(Book("Апельсин", "Петров", 2000, "isbn-2"))
        self.library.add_book(Book("Банан", "Андреев", 2)


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

```python
import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shapes import Shape, Circle, Rectangle, Triangle


class TestShape(unittest.TestCase):
    """Тесты базового класса Shape."""
    
    def test_creation(self):
        """Shape создаётся с именем."""
        shape = Shape("Фигура")
        self.assertEqual(shape.name, "Фигура")
    
    def test_default_area(self):
        """area() возвращает 0 по умолчанию."""
        shape = Shape("Тест")
        self.assertEqual(shape.area(), 0)
    
    def test_default_perimeter(self):
        """perimeter() возвращает 0 по умолчанию."""
        shape = Shape("Тест")
        self.assertEqual(shape.perimeter(), 0)
    
    def test_describe_format(self):
        """describe() возвращает правильный формат."""
        shape = Shape("Тест")
        description = shape.describe()
        self.assertIn("Тест", description)
        self.assertIn("площадь", description.lower())
        self.assertIn("периметр", description.lower())


class TestCircle(unittest.TestCase):
    """Тесты класса Circle."""
    
    def test_inheritance(self):
        """Circle наследуется от Shape."""
        circle = Circle(5)
        self.assertIsInstance(circle, Shape)
    
    def test_name(self):
        """Circle имеет правильное имя."""
        circle = Circle(5)
        self.assertEqual(circle.name, "Circle")
    
    def test_radius_attribute(self):
        """Атрибут radius доступен."""
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)
    
    def test_area(self):
        """area() вычисляет площадь круга."""
        circle = Circle(5)
        expected = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected, places=10)
    
    def test_area_unit_circle(self):
        """Площадь единичного круга."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi, places=10)
    
    def test_perimeter(self):
        """perimeter() вычисляет длину окружности."""
        circle = Circle(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(circle.perimeter(), expected, places=10)
    
    def test_perimeter_unit_circle(self):
        """Периметр единичного круга."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi, places=10)
    
    def test_negative_radius_raises(self):
        """Отрицательный радиус вызывает ValueError."""
        with self.assertRaises(ValueError):
            Circle(-5)
    
    def test_zero_radius_raises(self):
        """Нулевой радиус вызывает ValueError."""
        with self.assertRaises(ValueError):
            Circle(0)
    
    def test_describe(self):
        """describe() работает для Circle."""
        circle = Circle(5)
        description = circle.describe()
        self.assertIn("Circle", description)


class TestRectangleShape(unittest.TestCase):
    """Тесты класса Rectangle (в иерархии Shape)."""
    
    def test_inheritance(self):
        """Rectangle наследуется от Shape."""
        rect = Rectangle(4, 6)
        self.assertIsInstance(rect, Shape)
    
    def test_name(self):
        """Rectangle имеет правильное имя."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.name, "Rectangle")
    
    def test_dimensions(self):
        """Атрибуты width и height доступны."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
    
    def test_area(self):
        """area() вычисляет площадь."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)
    
    def test_perimeter(self):
        """perimeter() вычисляет периметр."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.perimeter(), 20)
    
    def test_is_square_true(self):
        """is_square() возвращает True для квадрата."""
        square = Rectangle(5, 5)
        self.assertTrue(square.is_square())
    
    def test_is_square_false(self):
        """is_square() возвращает False для не-квадрата."""
        rect = Rectangle(4, 6)
        self.assertFalse(rect.is_square())
    
    def test_negative_width_raises(self):
        """Отрицательная ширина вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-4, 6)
    
    def test_negative_height_raises(self):
        """Отрицательная высота вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(4, -6)
    
    def test_zero_dimensions_raises(self):
        """Нулевые размеры вызывают ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 6)


class TestTriangle(unittest.TestCase):
    """Тесты класса Triangle."""
    
    def test_inheritance(self):
        """Triangle наследуется от Shape."""
        triangle = Triangle(3, 4, 5)
        self.assertIsInstance(triangle, Shape)
    
    def test_name(self):
        """Triangle имеет правильное имя."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.name, "Triangle")
    
    def test_sides(self):
        """Атрибуты сторон доступны."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.a, 3)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 5)
    
    def test_perimeter(self):
        """perimeter() вычисляет периметр."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)
    
    def test_area_right_triangle(self):
        """area() для прямоугольного треугольника 3-4-5."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=10)
    
    def test_area_equilateral(self):
        """area() для равностороннего треугольника."""
        triangle = Triangle(6, 6, 6)
        expected = (math.sqrt(3) / 4) * 36  # ≈ 15.59
        self.assertAlmostEqual(triangle.area(), expected, places=10)
    
    def test_invalid_triangle_raises(self):
        """Невозможный треугольник вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)  # 1 + 2 < 10
    
    def test_invalid_triangle_equality(self):
        """Вырожденный треугольник вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # 1 + 2 = 3
    
    def test_negative_side_raises(self):
        """Отрицательная сторона вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)
    
    def test_zero_side_raises(self):
        """Нулевая сторона вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)


class TestSquare(unittest.TestCase):
    """Тесты дополнительного задания: Square."""
    
    def test_square_inheritance(self):
        """Square наследуется от Rectangle."""
        from shapes import Square
        square = Square(5)
        self.assertIsInstance(square, Rectangle)
    
    def test_square_creation(self):
        """Square создаётся с одной стороной."""
        from shapes import Square
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
    
    def test_square_area(self):
        """area() для Square."""
        from shapes import Square
        square = Square(5)
        self.assertEqual(square.area(), 25)
    
    def test_square_is_square(self):
        """is_square() для Square возвращает True."""
        from shapes import Square
        square = Square(5)
        self.assertTrue(square.is_square())


class TestShapeComparison(unittest.TestCase):
    """Тесты дополнительного задания: сравнение фигур."""
    
    def test_equality_same_area(self):
        """Фигуры с одинаковой площадью равны."""
        circle = Circle(1)  # площадь ≈ 3.14
        # Подберём прямоугольник с такой же площадью
        rect = Rectangle(math.pi, 1)  # площадь = π
        self.assertEqual(circle, rect)
    
    def test_equality_different_area(self):
        """Фигуры с разной площадью не равны."""
        circle = Circle(5)
        rect = Rectangle(2, 3)
        self.assertNotEqual(circle, rect)
    
    def test_less_than(self):
        """Сравнение меньше по площади."""
        small = Rectangle(2, 2)  # площадь = 4
        big = Rectangle(3, 3)    # площадь = 9
        self.assertTrue(small < big)
        self.assertFalse(big < small)
    
    def test_greater_than(self):
        """Сравнение больше по площади."""
        small = Rectangle(2, 2)
        big = Rectangle(3, 3)
        self.assertTrue(big > small)
        self.assertFalse(small > big)
    
    def test_sorting(self):
        """Фигуры можно сортировать по площади."""
        shapes = [
            Rectangle(3, 3),  # 9
            Circle(1),        # ≈ 3.14
            Rectangle(2, 2),  # 4
        ]
        sorted_shapes = sorted(shapes)
        areas = [s.area() for s in sorted_shapes]
        self.assertEqual(areas, sorted(areas))


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestShape))
    suite.addTests(loader.loadTestsFromTestCase(TestCircle))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleShape))
    suite.addTests(loader.loadTestsFromTestCase(TestTriangle))
    
    # Дополнительные тесты (могут падать, если не реализованы)
    try:
        from shapes import Square
        suite.addTests(loader.loadTestsFromTestCase(TestSquare))
    except ImportError:
        print("Square не реализован, тесты пропущены")
    
    suite.addTests(loader.loadTestsFromTestCase(TestShapeComparison))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from employees import Employee, Manager, Developer, Intern, Company


class TestEmployee(unittest.TestCase):
    """Тесты базового класса Employee."""
    
    def test_creation(self):
        """Employee создаётся с правильными атрибутами."""
        emp = Employee("Иван", "E001", 50000)
        self.assertEqual(emp.name, "Иван")
        self.assertEqual(emp.employee_id, "E001")
        self.assertEqual(emp.base_salary, 50000)
    
    def test_calculate_salary_base(self):
        """calculate_salary() возвращает базовую зарплату."""
        emp = Employee("Иван", "E001", 50000)
        self.assertEqual(emp.calculate_salary(), 50000)
    
    def test_get_info(self):
        """get_info() возвращает информацию о сотруднике."""
        emp = Employee("Иван", "E001", 50000)
        info = emp.get_info()
        self.assertIn("Иван", info)
        self.assertIn("E001", info)
    
    def test_str(self):
        """__str__() возвращает строку."""
        emp = Employee("Иван", "E001", 50000)
        self.assertIsInstance(str(emp), str)
        self.assertIn("Иван", str(emp))


class TestManager(unittest.TestCase):
    """Тесты класса Manager."""
    
    def test_inheritance(self):
        """Manager наследуется от Employee."""
        manager = Manager("Иван", "M001", 100000)
        self.assertIsInstance(manager, Employee)
    
    def test_default_bonus(self):
        """Бонус по умолчанию равен 0."""
        manager = Manager("Иван", "M001", 100000)
        self.assertEqual(manager.bonus, 0)
    
    def test_salary_without_bonus(self):
        """Зарплата без бонуса равна базовой."""
        manager = Manager("Иван", "M001", 100000)
        self.assertEqual(manager.calculate_salary(), 100000)
    
    def test_set_bonus(self):
        """set_bonus() устанавливает бонус."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(20000)
        self.assertEqual(manager.bonus, 20000)
    
    def test_salary_with_bonus(self):
        """Зарплата включает бонус."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(20000)
        self.assertEqual(manager.calculate_salary(), 120000)
    
    def test_change_bonus(self):
        """Бонус можно изменить."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(10000)
        manager.set_bonus(30000)
        self.assertEqual(manager.calculate_salary(), 130000)


class TestDeveloper(unittest.TestCase):
    """Тесты класса Developer."""
    
    def test_inheritance(self):
        """Developer наследуется от Employee."""
        dev = Developer("Мария", "D001", 80000)
        self.assertIsInstance(dev, Employee)
    
    def test_default_languages(self):
        """Список языков по умолчанию пуст."""
        dev = Developer("Мария", "D001", 80000)
        self.assertEqual(dev.programming_languages, [])
    
    def test_salary_no_languages(self):
        """Зарплата без языков равна базовой."""
        dev = Developer("Мария", "D001", 80000)
        self.assertEqual(dev.calculate_salary(), 80000)
    
    def test_add_language(self):
        """add_language() добавляет язык."""
        dev = Developer("Мария", "D001", 80000)
        dev.add_language("Python")
        self.assertIn("Python", dev.programming_languages)
    
    def test_salary_with_languages(self):
        """Зарплата увеличивается за языки."""
        dev = Developer("Мария", "D001", 80000)
        dev.add_language("Python")
        dev.add_language("JavaScript")
        self.assertEqual(dev.calculate_salary(), 82000)
    
    def test_salary_many_languages(self):
        """Зарплата за много языков."""
        dev = Developer("Мария", "D001", 80000)
        for lang in ["Python", "JavaScript", "Go", "Rust", "C++"]:
            dev.add_language(lang)
        self.assertEqual(dev.calculate_salary(), 85000)


class TestIntern(unittest.TestCase):
    """Тесты класса Intern."""
    
    def test_inheritance(self):
        """Intern наследуется от Employee."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertIsInstance(intern, Employee)
    
    def test_duration_attribute(self):
        """Атрибут duration_months доступен."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertEqual(intern.duration_months, 3)
    
    def test_salary_half(self):
        """Зарплата стажёра — половина базовой."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertEqual(intern.calculate_salary(), 20000)
    
    def test_salary_different_base(self):
        """Зарплата стажёра с другой базой."""
        intern = Intern("Борис", "I002", 60000, 6)
        self.assertEqual(intern.calculate_salary(), 30000)


class TestCompany(unittest.TestCase):
    """Тесты класса Company."""
    
    def setUp(self):
        """Создание тестовых данных."""
        self.company = Company("TechCorp")
        self.manager = Manager("Иван", "M001", 100000)
        self.dev = Developer("Мария", "D001", 80000)
        self.intern = Intern("Алексей", "I001", 40000, 3)
    
    def test_creation(self):
        """Company создаётся с именем."""
        self.assertEqual(self.company.name, "TechCorp")
    
    def test_add_employee(self):
        """add_employee() добавляет сотрудника."""
        self.company.add_employee(self.manager)
        employees = self.company.get_employees_by_type(Manager)
        self.assertIn(self.manager, employees)
    
    def test_add_multiple_employees(self):
        """Добавление нескольких сотрудников."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.add_employee(self.intern)
        # Проверяем общее количество
        all_employees = (
            self.company.get_employees_by_type(Manager) +
            self.company.get_employees_by_type(Developer) +
            self.company.get_employees_by_type(Intern)
        )
        self.assertEqual(len(all_employees), 3)
    
    def test_get_total_salaries(self):
        """get_total_salaries() считает сумму зарплат."""
        self.manager.set_bonus(20000)  # 120000
        self.dev.add_language("Python")  # 81000
        # intern: 20000
        
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.add_employee(self.intern)
        
        self.assertEqual(self.company.get_total_salaries(), 221000)
    
    def test_get_employees_by_type_manager(self):
        """Фильтрация по типу Manager."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        managers = self.company.get_employees_by_type(Manager)
        self.assertEqual(len(managers), 1)
        self.assertIsInstance(managers[0], Manager)
    
    def test_get_employees_by_type_developer(self):
        """Фильтрация по типу Developer."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        devs = self.company.get_employees_by_type(Developer)
        self.assertEqual(len(devs), 1)
        self.assertIsInstance(devs[0], Developer)
    
    def test_fire_employee(self):
        """fire_employee() удаляет сотрудника."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.fire_employee("M001")
        managers = self.company.get_employees_by_type(Manager)
        self.assertEqual(len(managers), 0)
    
    def test_fire_nonexistent_raises(self):
        """Увольнение несуществующего вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.company.fire_employee("X999")


class TestSalesPerson(unittest.TestCase):
    """Тесты дополнительного задания: SalesPerson."""
    
    def test_creation(self):
        """SalesPerson создаётся."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=100000)
        self.assertEqual(sales.sales_amount, 100000)
    
    def test_salary_with_commission(self):
        """Зарплата включает 5% комиссии."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=100000)
        # 50000 + 100000 * 0.05 = 55000
        self.assertEqual(sales.calculate_salary(), 55000)
    
    def test_inheritance(self):
        """SalesPerson наследуется от Employee."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=0)
        self.assertIsInstance(sales, Employee)


class TestCompanyReport(unittest.TestCase):
    """Тесты дополнительного задания: отчёт."""
    
    def test_generate_report_exists(self):
        """Метод generate_report() существует."""
        company = Company("Test")
        self.assertTrue(hasattr(company, 'generate_report'))
    
    def test_generate_report_returns_string(self):
        """generate_report() возвращает строку."""
        company = Company("Test")
        company.add_employee(Manager("Тест", "T001", 100000))
        report = company.generate_report()
        self.assertIsInstance(report, str)


class TestCompanyRaise(unittest.TestCase):
    """Тесты дополнительного задания: повышение зарплаты."""
    
    def test_give_raise(self):
        """give_raise() увеличивает базовую зарплату."""
        company = Company("Test")
        emp = Employee("Тест", "E001", 50000)
        company.add_employee(emp)
        company.give_raise("E001", 10000)
        self.assertEqual(emp.base_salary, 60000)
    
    def test_give_raise_nonexistent_raises(self):
        """Повышение несуществующего вызывает KeyError."""
        company = Company("Test")
        with self.assertRaises(KeyError):
            company.give_raise("X999", 10000)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestEmployee))
    suite.addTests(loader.loadTestsFromTestCase(TestManager))
    suite.addTests(loader.loadTestsFromTestCase(TestDeveloper))
    suite.addTests(loader.loadTestsFromTestCase(TestIntern))
    suite.addTests(loader.loadTestsFromTestCase(TestCompany))
    
    # Дополнительные тесты
    try:
        from employees import SalesPerson
        suite.addTests(loader.loadTestsFromTestCase(TestSalesPerson))
    except ImportError:
        print("SalesPerson не реализован")
    
    suite.addTests(loader.loadTestsFromTestCase(TestCompanyReport))
    suite.addTests(loader.loadTestsFromTestCase(TestCompanyRaise))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures import Stack, Queue


class TestStackBasic(unittest.TestCase):
    """Базовые тесты Stack."""
    
    def test_create_empty(self):
        """Создание пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
    
    def test_create_from_iterable(self):
        """Создание стека из iterable."""
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)
    
    def test_push(self):
        """push() добавляет элемент."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)
    
    def test_push_multiple(self):
        """Несколько push()."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)
    
    def test_pop(self):
        """pop() возвращает и удаляет верхний элемент."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.pop()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 1)
    
    def test_pop_order_lifo(self):
        """pop() соблюдает LIFO."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
    
    def test_pop_empty_raises(self):
        """pop() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertIn("empty", str(context.exception).lower())
    
    def test_peek(self):
        """peek() возвращает верхний элемент без удаления."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.peek()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 2)  # Длина не изменилась
    
    def test_peek_empty_raises(self):
        """peek() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
    
    def test_is_empty_true(self):
        """is_empty() возвращает True для пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
    
    def test_is_empty_false(self):
        """is_empty() возвращает False для непустого стека."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())


class TestStackMagicMethods(unittest.TestCase):
    """Тесты магических методов Stack."""
    
    def test_len_empty(self):
        """len() для пустого стека."""
        stack = Stack()
        self.assertEqual(len(stack), 0)
    
    def test_len_with_items(self):
        """len() для непустого стека."""
        stack = Stack([1, 2, 3, 4, 5])
        self.assertEqual(len(stack), 5)
    
    def test_bool_empty(self):
        """bool() для пустого стека — False."""
        stack = Stack()
        self.assertFalse(bool(stack))
    
    def test_bool_not_empty(self):
        """bool() для непустого стека — True."""
        stack = Stack([1])
        self.assertTrue(bool(stack))
    
    def test_if_statement(self):
        """Стек работает в if."""
        stack = Stack()
        if stack:
            self.fail("Пустой стек не должен быть truthy")
        
        stack.push(1)
        if not stack:
            self.fail("Непустой стек должен быть truthy")
    
    def test_iter(self):
        """Итерация по стеку (от вершины к основанию)."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        items = list(stack)
        self.assertEqual(items, [3, 2, 1])
    
    def test_iter_for_loop(self):
        """Стек работает в for."""
        stack = Stack([1, 2, 3])
        result = []
        for item in stack:
            result.append(item)
        self.assertEqual(len(result), 3)


class TestQueueBasic(unittest.TestCase):
    """Базовые тесты Queue."""
    
    def test_create_empty(self):
        """Создание пустой очереди."""
        queue = Queue()
        self.assertTrue(queue.is_empty())
    
    def test_create_from_iterable(self):
        """Создание очереди из iterable."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)
    
    def test_enqueue(self):
        """enqueue() добавляет элемент."""
        queue = Queue()
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
    
    def test_dequeue(self):
        """dequeue() возвращает и удаляет первый элемент."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        result = queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 1)
    
    def test_dequeue_order_fifo(self):
        """dequeue() соблюдает FIFO."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
    
    def test_dequeue_empty_raises(self):
        """dequeue() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError) as context:
            queue.dequeue()
        self.assertIn("empty", str(context.exception).lower())
    
    def test_front(self):
        """front() возвращает первый элемент без удаления."""
        queue = Queue([1, 2, 3])
        result = queue.front()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 3)
    
    def test_front_empty_raises(self):
        """front() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.front()


class TestQueueMagicMethods(unittest.TestCase):
    """Тесты магических методов Queue."""
    
    def test_len(self):
        """len() для очереди."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)
    
    def test_bool_empty(self):
        """bool() для пустой очереди."""
        queue = Queue()
        self.assertFalse(bool(queue))
    
    def test_bool_not_empty(self):
        """bool() для непустой очереди."""
        queue = Queue([1])
        self.assertTrue(bool(queue))
    
    def test_iter(self):
        """Итерация по очереди (от начала к концу)."""
        queue = Queue([1, 2, 3])
        items = list(queue)
        self.assertEqual(items, [1, 2, 3])


class TestStackAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Stack."""
    
    def test_clear(self):
        """clear() очищает стек."""
        stack = Stack([1, 2, 3])
        stack.clear()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)
    
    def test_contains(self):
        """contains() проверяет наличие элемента."""
        stack = Stack([1, 2, 3])
        self.assertTrue(stack.contains(2))
        self.assertFalse(stack.contains(5))
    
    def test_in_operator(self):
        """Оператор in работает."""
        stack = Stack([1, 2, 3])
        self.assertIn(2, stack)
        self.assertNotIn(5, stack)
    
    def test_maxsize(self):
        """Ограничение размера стека."""
        stack = Stack(maxsize=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(OverflowError):
            stack.push(4)


class TestQueueAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Queue."""
    
    def test_clear(self):
        """clear() очищает очередь."""
        queue = Queue([1, 2, 3])
        queue.clear()
        self.assertTrue(queue.is_empty())
    
    def test_contains(self):
        """contains() проверяет наличие элемента."""
        queue = Queue([1, 2, 3])
        self.assertTrue(queue.contains(2))
        self.assertFalse(queue.contains(5))
    
    def test_in_operator(self):
        """Оператор in работает."""
        queue = Queue([1, 2, 3])
        self.assertIn(2, queue)
        self.assertNotIn(5, queue)
    
    def test_maxsize(self):
        """Ограничение размера очереди."""
        queue = Queue(maxsize=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        with self.assertRaises(OverflowError):
            queue.enqueue(4)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestStackBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestStackMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestStackAdditional))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueAdditional))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from logger import Logger, log_calls


class TestLoggerSingleton(unittest.TestCase):
    """Тесты паттерна Singleton."""
    
    def setUp(self):
        """Сброс singleton перед каждым тестом."""
        Logger._instance = None
    
    def test_singleton_same_instance(self):
        """Два вызова возвращают один экземпляр."""
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)
    
    def test_singleton_id(self):
        """id() одинаков для всех экземпляров."""
        logger1 = Logger()
        logger2 = Logger()
        self.assertEqual(id(logger1), id(logger2))


class TestLoggerLevels(unittest.TestCase):
    """Тесты уровней логирования."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
    
    def test_level_constants_exist(self):
        """Константы уровней существуют."""
        self.assertTrue(hasattr(Logger, 'DEBUG'))
        self.assertTrue(hasattr(Logger, 'INFO'))
        self.assertTrue(hasattr(Logger, 'WARNING'))
        self.assertTrue(hasattr(Logger, 'ERROR'))
        self.assertTrue(hasattr(Logger, 'CRITICAL'))
    
    def test_level_order(self):
        """Уровни упорядочены по важности."""
        self.assertLess(Logger.DEBUG, Logger.INFO)
        self.assertLess(Logger.INFO, Logger.WARNING)
        self.assertLess(Logger.WARNING, Logger.ERROR)
        self.assertLess(Logger.ERROR, Logger.CRITICAL)
    
    def test_set_level(self):
        """set_level() устанавливает уровень."""
        self.logger.set_level(Logger.WARNING)
        # Не должно падать
    
    def test_filter_by_level(self):
        """Сообщения ниже уровня не логируются."""
        self.logger.set_level(Logger.WARNING)
        self.logger.debug("Debug")
        self.logger.info("Info")
        self.logger.warning("Warning")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertIn("Warning", logs[0])


class TestLoggerMethods(unittest.TestCase):
    """Тесты методов логирования."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_debug(self):
        """debug() создаёт запись."""
        self.logger.debug("Test debug")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertIn("DEBUG", logs[0])
        self.assertIn("Test debug", logs[0])
    
    def test_info(self):
        """info() создаёт запись."""
        self.logger.info("Test info")
        logs = self.logger.get_logs()
        self.assertIn("INFO", logs[0])
    
    def test_warning(self):
        """warning() создаёт запись."""
        self.logger.warning("Test warning")
        logs = self.logger.get_logs()
        self.assertIn("WARNING", logs[0])
    
    def test_error(self):
        """error() создаёт запись."""
        self.logger.error("Test error")
        logs = self.logger.get_logs()
        self.assertIn("ERROR", logs[0])
    
    def test_critical(self):
        """critical() создаёт запись."""
        self.logger.critical("Test critical")
        logs = self.logger.get_logs()
        self.assertIn("CRITICAL", logs[0])
    
    def test_log_format_contains_timestamp(self):
        """Запись содержит временную метку."""
        self.logger.info("Test")
        logs = self.logger.get_logs()
        # Проверяем наличие формата даты
        import re
        pattern = r'\d{4}-\d{2}-\d{2}'
        self.assertTrue(re.search(pattern, logs[0]))
    
    def test_log_format_contains_time(self):
        """Запись содержит время."""
        self.logger.info("Test")
        logs = self.logger.get_logs()
        import re
        pattern = r'\d{2}:\d{2}:\d{2}'
        self.assertTrue(re.search(pattern, logs[0]))


class TestLoggerGetLogs(unittest.TestCase):
    """Тесты получения логов."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_get_logs_empty(self):
        """get_logs() возвращает пустой список."""
        logs = self.logger.get_logs()
        self.assertEqual(logs, [])
    
    def test_get_logs_multiple(self):
        """get_logs() возвращает все записи."""
        self.logger.info("First")
        self.logger.warning("Second")
        self.logger.error("Third")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 3)
    
    def test_get_logs_by_level(self):
        """get_logs_by_level() фильтрует записи."""
        self.logger.info("Info message")
        self.logger.warning("Warning message")
        self.logger.error("Error message")
        
        errors = self.logger.get_logs_by_level(Logger.ERROR)
        self.assertEqual(len(errors), 1)
        self.assertIn("Error message", errors[0])
    
    def test_get_logs_by_level_multiple(self):
        """get_logs_by_level() для нескольких записей одного уровня."""
        self.logger.warning("Warning 1")
        self.logger.info("Info")
        self.logger.warning("Warning 2")
        
        warnings = self.logger.get_logs_by_level(Logger.WARNING)
        self.assertEqual(len(warnings), 2)


class TestLogCallsDecorator(unittest.TestCase):
    """Тесты декоратора log_calls."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_decorator_logs_call(self):
        """Декоратор логирует вызов функции."""
        @log_calls
        def sample_function(x, y):
            return x + y
        
        result = sample_function(2, 3)
        logs = self.logger.get_logs()
        
        self.assertGreater(len(logs), 0)
    
    def test_decorator_logs_function_name(self):
        """Декоратор логирует имя функции."""
        @log_calls
        def my_special_function():
            return 42
        
        my_special_function()
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("my_special_function", log_text)
    
    def test_decorator_preserves_return_value(self):
        """Декоратор не изменяет возвращаемое значение."""
        @log_calls
        def add(a, b):
            return a + b
        
        result = add(10, 20)
        self.assertEqual(result, 30)
    
    def test_decorator_logs_arguments(self):
        """Декоратор логирует аргументы."""
        @log_calls
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"
        
        greet("Alice")
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("Alice", log_text)
    
    def test_decorator_logs_result(self):
        """Декоратор логирует результат."""
        @log_calls
        def multiply(a, b):
            return a * b
        
        multiply(7, 6)
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("42", log_text)


class TestLoggerFile(unittest.TestCase):
    """Тесты дополнительного задания: запись в файл."""
    
    def setUp(self):
        Logger._instance = None
        self.test_file = "test_log.txt"
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_file_logging(self):
        """Логирование в файл."""
        logger = Logger(filename=self)

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

```python
import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shapes import Shape, Circle, Rectangle, Triangle


class TestShape(unittest.TestCase):
    """Тесты базового класса Shape."""
    
    def test_creation(self):
        """Shape создаётся с именем."""
        shape = Shape("Фигура")
        self.assertEqual(shape.name, "Фигура")
    
    def test_default_area(self):
        """area() возвращает 0 по умолчанию."""
        shape = Shape("Тест")
        self.assertEqual(shape.area(), 0)
    
    def test_default_perimeter(self):
        """perimeter() возвращает 0 по умолчанию."""
        shape = Shape("Тест")
        self.assertEqual(shape.perimeter(), 0)
    
    def test_describe_format(self):
        """describe() возвращает правильный формат."""
        shape = Shape("Тест")
        description = shape.describe()
        self.assertIn("Тест", description)
        self.assertIn("площадь", description.lower())
        self.assertIn("периметр", description.lower())


class TestCircle(unittest.TestCase):
    """Тесты класса Circle."""
    
    def test_inheritance(self):
        """Circle наследуется от Shape."""
        circle = Circle(5)
        self.assertIsInstance(circle, Shape)
    
    def test_name(self):
        """Circle имеет правильное имя."""
        circle = Circle(5)
        self.assertEqual(circle.name, "Circle")
    
    def test_radius_attribute(self):
        """Атрибут radius доступен."""
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)
    
    def test_area(self):
        """area() вычисляет площадь круга."""
        circle = Circle(5)
        expected = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected, places=10)
    
    def test_area_unit_circle(self):
        """Площадь единичного круга."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi, places=10)
    
    def test_perimeter(self):
        """perimeter() вычисляет длину окружности."""
        circle = Circle(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(circle.perimeter(), expected, places=10)
    
    def test_perimeter_unit_circle(self):
        """Периметр единичного круга."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi, places=10)
    
    def test_negative_radius_raises(self):
        """Отрицательный радиус вызывает ValueError."""
        with self.assertRaises(ValueError):
            Circle(-5)
    
    def test_zero_radius_raises(self):
        """Нулевой радиус вызывает ValueError."""
        with self.assertRaises(ValueError):
            Circle(0)
    
    def test_describe(self):
        """describe() работает для Circle."""
        circle = Circle(5)
        description = circle.describe()
        self.assertIn("Circle", description)


class TestRectangleShape(unittest.TestCase):
    """Тесты класса Rectangle (в иерархии Shape)."""
    
    def test_inheritance(self):
        """Rectangle наследуется от Shape."""
        rect = Rectangle(4, 6)
        self.assertIsInstance(rect, Shape)
    
    def test_name(self):
        """Rectangle имеет правильное имя."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.name, "Rectangle")
    
    def test_dimensions(self):
        """Атрибуты width и height доступны."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
    
    def test_area(self):
        """area() вычисляет площадь."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)
    
    def test_perimeter(self):
        """perimeter() вычисляет периметр."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.perimeter(), 20)
    
    def test_is_square_true(self):
        """is_square() возвращает True для квадрата."""
        square = Rectangle(5, 5)
        self.assertTrue(square.is_square())
    
    def test_is_square_false(self):
        """is_square() возвращает False для не-квадрата."""
        rect = Rectangle(4, 6)
        self.assertFalse(rect.is_square())
    
    def test_negative_width_raises(self):
        """Отрицательная ширина вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-4, 6)
    
    def test_negative_height_raises(self):
        """Отрицательная высота вызывает ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(4, -6)
    
    def test_zero_dimensions_raises(self):
        """Нулевые размеры вызывают ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 6)


class TestTriangle(unittest.TestCase):
    """Тесты класса Triangle."""
    
    def test_inheritance(self):
        """Triangle наследуется от Shape."""
        triangle = Triangle(3, 4, 5)
        self.assertIsInstance(triangle, Shape)
    
    def test_name(self):
        """Triangle имеет правильное имя."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.name, "Triangle")
    
    def test_sides(self):
        """Атрибуты сторон доступны."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.a, 3)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 5)
    
    def test_perimeter(self):
        """perimeter() вычисляет периметр."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)
    
    def test_area_right_triangle(self):
        """area() для прямоугольного треугольника 3-4-5."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=10)
    
    def test_area_equilateral(self):
        """area() для равностороннего треугольника."""
        triangle = Triangle(6, 6, 6)
        expected = (math.sqrt(3) / 4) * 36  # ≈ 15.59
        self.assertAlmostEqual(triangle.area(), expected, places=10)
    
    def test_invalid_triangle_raises(self):
        """Невозможный треугольник вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)  # 1 + 2 < 10
    
    def test_invalid_triangle_equality(self):
        """Вырожденный треугольник вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # 1 + 2 = 3
    
    def test_negative_side_raises(self):
        """Отрицательная сторона вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)
    
    def test_zero_side_raises(self):
        """Нулевая сторона вызывает ValueError."""
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)


class TestSquare(unittest.TestCase):
    """Тесты дополнительного задания: Square."""
    
    def test_square_inheritance(self):
        """Square наследуется от Rectangle."""
        from shapes import Square
        square = Square(5)
        self.assertIsInstance(square, Rectangle)
    
    def test_square_creation(self):
        """Square создаётся с одной стороной."""
        from shapes import Square
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
    
    def test_square_area(self):
        """area() для Square."""
        from shapes import Square
        square = Square(5)
        self.assertEqual(square.area(), 25)
    
    def test_square_is_square(self):
        """is_square() для Square возвращает True."""
        from shapes import Square
        square = Square(5)
        self.assertTrue(square.is_square())


class TestShapeComparison(unittest.TestCase):
    """Тесты дополнительного задания: сравнение фигур."""
    
    def test_equality_same_area(self):
        """Фигуры с одинаковой площадью равны."""
        circle = Circle(1)  # площадь ≈ 3.14
        # Подберём прямоугольник с такой же площадью
        rect = Rectangle(math.pi, 1)  # площадь = π
        self.assertEqual(circle, rect)
    
    def test_equality_different_area(self):
        """Фигуры с разной площадью не равны."""
        circle = Circle(5)
        rect = Rectangle(2, 3)
        self.assertNotEqual(circle, rect)
    
    def test_less_than(self):
        """Сравнение меньше по площади."""
        small = Rectangle(2, 2)  # площадь = 4
        big = Rectangle(3, 3)    # площадь = 9
        self.assertTrue(small < big)
        self.assertFalse(big < small)
    
    def test_greater_than(self):
        """Сравнение больше по площади."""
        small = Rectangle(2, 2)
        big = Rectangle(3, 3)
        self.assertTrue(big > small)
        self.assertFalse(small > big)
    
    def test_sorting(self):
        """Фигуры можно сортировать по площади."""
        shapes = [
            Rectangle(3, 3),  # 9
            Circle(1),        # ≈ 3.14
            Rectangle(2, 2),  # 4
        ]
        sorted_shapes = sorted(shapes)
        areas = [s.area() for s in sorted_shapes]
        self.assertEqual(areas, sorted(areas))


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestShape))
    suite.addTests(loader.loadTestsFromTestCase(TestCircle))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleShape))
    suite.addTests(loader.loadTestsFromTestCase(TestTriangle))
    
    # Дополнительные тесты (могут падать, если не реализованы)
    try:
        from shapes import Square
        suite.addTests(loader.loadTestsFromTestCase(TestSquare))
    except ImportError:
        print("Square не реализован, тесты пропущены")
    
    suite.addTests(loader.loadTestsFromTestCase(TestShapeComparison))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from employees import Employee, Manager, Developer, Intern, Company


class TestEmployee(unittest.TestCase):
    """Тесты базового класса Employee."""
    
    def test_creation(self):
        """Employee создаётся с правильными атрибутами."""
        emp = Employee("Иван", "E001", 50000)
        self.assertEqual(emp.name, "Иван")
        self.assertEqual(emp.employee_id, "E001")
        self.assertEqual(emp.base_salary, 50000)
    
    def test_calculate_salary_base(self):
        """calculate_salary() возвращает базовую зарплату."""
        emp = Employee("Иван", "E001", 50000)
        self.assertEqual(emp.calculate_salary(), 50000)
    
    def test_get_info(self):
        """get_info() возвращает информацию о сотруднике."""
        emp = Employee("Иван", "E001", 50000)
        info = emp.get_info()
        self.assertIn("Иван", info)
        self.assertIn("E001", info)
    
    def test_str(self):
        """__str__() возвращает строку."""
        emp = Employee("Иван", "E001", 50000)
        self.assertIsInstance(str(emp), str)
        self.assertIn("Иван", str(emp))


class TestManager(unittest.TestCase):
    """Тесты класса Manager."""
    
    def test_inheritance(self):
        """Manager наследуется от Employee."""
        manager = Manager("Иван", "M001", 100000)
        self.assertIsInstance(manager, Employee)
    
    def test_default_bonus(self):
        """Бонус по умолчанию равен 0."""
        manager = Manager("Иван", "M001", 100000)
        self.assertEqual(manager.bonus, 0)
    
    def test_salary_without_bonus(self):
        """Зарплата без бонуса равна базовой."""
        manager = Manager("Иван", "M001", 100000)
        self.assertEqual(manager.calculate_salary(), 100000)
    
    def test_set_bonus(self):
        """set_bonus() устанавливает бонус."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(20000)
        self.assertEqual(manager.bonus, 20000)
    
    def test_salary_with_bonus(self):
        """Зарплата включает бонус."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(20000)
        self.assertEqual(manager.calculate_salary(), 120000)
    
    def test_change_bonus(self):
        """Бонус можно изменить."""
        manager = Manager("Иван", "M001", 100000)
        manager.set_bonus(10000)
        manager.set_bonus(30000)
        self.assertEqual(manager.calculate_salary(), 130000)


class TestDeveloper(unittest.TestCase):
    """Тесты класса Developer."""
    
    def test_inheritance(self):
        """Developer наследуется от Employee."""
        dev = Developer("Мария", "D001", 80000)
        self.assertIsInstance(dev, Employee)
    
    def test_default_languages(self):
        """Список языков по умолчанию пуст."""
        dev = Developer("Мария", "D001", 80000)
        self.assertEqual(dev.programming_languages, [])
    
    def test_salary_no_languages(self):
        """Зарплата без языков равна базовой."""
        dev = Developer("Мария", "D001", 80000)
        self.assertEqual(dev.calculate_salary(), 80000)
    
    def test_add_language(self):
        """add_language() добавляет язык."""
        dev = Developer("Мария", "D001", 80000)
        dev.add_language("Python")
        self.assertIn("Python", dev.programming_languages)
    
    def test_salary_with_languages(self):
        """Зарплата увеличивается за языки."""
        dev = Developer("Мария", "D001", 80000)
        dev.add_language("Python")
        dev.add_language("JavaScript")
        self.assertEqual(dev.calculate_salary(), 82000)
    
    def test_salary_many_languages(self):
        """Зарплата за много языков."""
        dev = Developer("Мария", "D001", 80000)
        for lang in ["Python", "JavaScript", "Go", "Rust", "C++"]:
            dev.add_language(lang)
        self.assertEqual(dev.calculate_salary(), 85000)


class TestIntern(unittest.TestCase):
    """Тесты класса Intern."""
    
    def test_inheritance(self):
        """Intern наследуется от Employee."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertIsInstance(intern, Employee)
    
    def test_duration_attribute(self):
        """Атрибут duration_months доступен."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertEqual(intern.duration_months, 3)
    
    def test_salary_half(self):
        """Зарплата стажёра — половина базовой."""
        intern = Intern("Алексей", "I001", 40000, 3)
        self.assertEqual(intern.calculate_salary(), 20000)
    
    def test_salary_different_base(self):
        """Зарплата стажёра с другой базой."""
        intern = Intern("Борис", "I002", 60000, 6)
        self.assertEqual(intern.calculate_salary(), 30000)


class TestCompany(unittest.TestCase):
    """Тесты класса Company."""
    
    def setUp(self):
        """Создание тестовых данных."""
        self.company = Company("TechCorp")
        self.manager = Manager("Иван", "M001", 100000)
        self.dev = Developer("Мария", "D001", 80000)
        self.intern = Intern("Алексей", "I001", 40000, 3)
    
    def test_creation(self):
        """Company создаётся с именем."""
        self.assertEqual(self.company.name, "TechCorp")
    
    def test_add_employee(self):
        """add_employee() добавляет сотрудника."""
        self.company.add_employee(self.manager)
        employees = self.company.get_employees_by_type(Manager)
        self.assertIn(self.manager, employees)
    
    def test_add_multiple_employees(self):
        """Добавление нескольких сотрудников."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.add_employee(self.intern)
        # Проверяем общее количество
        all_employees = (
            self.company.get_employees_by_type(Manager) +
            self.company.get_employees_by_type(Developer) +
            self.company.get_employees_by_type(Intern)
        )
        self.assertEqual(len(all_employees), 3)
    
    def test_get_total_salaries(self):
        """get_total_salaries() считает сумму зарплат."""
        self.manager.set_bonus(20000)  # 120000
        self.dev.add_language("Python")  # 81000
        # intern: 20000
        
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.add_employee(self.intern)
        
        self.assertEqual(self.company.get_total_salaries(), 221000)
    
    def test_get_employees_by_type_manager(self):
        """Фильтрация по типу Manager."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        managers = self.company.get_employees_by_type(Manager)
        self.assertEqual(len(managers), 1)
        self.assertIsInstance(managers[0], Manager)
    
    def test_get_employees_by_type_developer(self):
        """Фильтрация по типу Developer."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        devs = self.company.get_employees_by_type(Developer)
        self.assertEqual(len(devs), 1)
        self.assertIsInstance(devs[0], Developer)
    
    def test_fire_employee(self):
        """fire_employee() удаляет сотрудника."""
        self.company.add_employee(self.manager)
        self.company.add_employee(self.dev)
        self.company.fire_employee("M001")
        managers = self.company.get_employees_by_type(Manager)
        self.assertEqual(len(managers), 0)
    
    def test_fire_nonexistent_raises(self):
        """Увольнение несуществующего вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.company.fire_employee("X999")


class TestSalesPerson(unittest.TestCase):
    """Тесты дополнительного задания: SalesPerson."""
    
    def test_creation(self):
        """SalesPerson создаётся."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=100000)
        self.assertEqual(sales.sales_amount, 100000)
    
    def test_salary_with_commission(self):
        """Зарплата включает 5% комиссии."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=100000)
        # 50000 + 100000 * 0.05 = 55000
        self.assertEqual(sales.calculate_salary(), 55000)
    
    def test_inheritance(self):
        """SalesPerson наследуется от Employee."""
        from employees import SalesPerson
        sales = SalesPerson("Продавец", "S001", 50000, sales_amount=0)
        self.assertIsInstance(sales, Employee)


class TestCompanyReport(unittest.TestCase):
    """Тесты дополнительного задания: отчёт."""
    
    def test_generate_report_exists(self):
        """Метод generate_report() существует."""
        company = Company("Test")
        self.assertTrue(hasattr(company, 'generate_report'))
    
    def test_generate_report_returns_string(self):
        """generate_report() возвращает строку."""
        company = Company("Test")
        company.add_employee(Manager("Тест", "T001", 100000))
        report = company.generate_report()
        self.assertIsInstance(report, str)


class TestCompanyRaise(unittest.TestCase):
    """Тесты дополнительного задания: повышение зарплаты."""
    
    def test_give_raise(self):
        """give_raise() увеличивает базовую зарплату."""
        company = Company("Test")
        emp = Employee("Тест", "E001", 50000)
        company.add_employee(emp)
        company.give_raise("E001", 10000)
        self.assertEqual(emp.base_salary, 60000)
    
    def test_give_raise_nonexistent_raises(self):
        """Повышение несуществующего вызывает KeyError."""
        company = Company("Test")
        with self.assertRaises(KeyError):
            company.give_raise("X999", 10000)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestEmployee))
    suite.addTests(loader.loadTestsFromTestCase(TestManager))
    suite.addTests(loader.loadTestsFromTestCase(TestDeveloper))
    suite.addTests(loader.loadTestsFromTestCase(TestIntern))
    suite.addTests(loader.loadTestsFromTestCase(TestCompany))
    
    # Дополнительные тесты
    try:
        from employees import SalesPerson
        suite.addTests(loader.loadTestsFromTestCase(TestSalesPerson))
    except ImportError:
        print("SalesPerson не реализован")
    
    suite.addTests(loader.loadTestsFromTestCase(TestCompanyReport))
    suite.addTests(loader.loadTestsFromTestCase(TestCompanyRaise))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures import Stack, Queue


class TestStackBasic(unittest.TestCase):
    """Базовые тесты Stack."""
    
    def test_create_empty(self):
        """Создание пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
    
    def test_create_from_iterable(self):
        """Создание стека из iterable."""
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)
    
    def test_push(self):
        """push() добавляет элемент."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)
    
    def test_push_multiple(self):
        """Несколько push()."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)
    
    def test_pop(self):
        """pop() возвращает и удаляет верхний элемент."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.pop()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 1)
    
    def test_pop_order_lifo(self):
        """pop() соблюдает LIFO."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
    
    def test_pop_empty_raises(self):
        """pop() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertIn("empty", str(context.exception).lower())
    
    def test_peek(self):
        """peek() возвращает верхний элемент без удаления."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.peek()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 2)  # Длина не изменилась
    
    def test_peek_empty_raises(self):
        """peek() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
    
    def test_is_empty_true(self):
        """is_empty() возвращает True для пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
    
    def test_is_empty_false(self):
        """is_empty() возвращает False для непустого стека."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())


class TestStackMagicMethods(unittest.TestCase):
    """Тесты магических методов Stack."""
    
    def test_len_empty(self):
        """len() для пустого стека."""
        stack = Stack()
        self.assertEqual(len(stack), 0)
    
    def test_len_with_items(self):
        """len() для непустого стека."""
        stack = Stack([1, 2, 3, 4, 5])
        self.assertEqual(len(stack), 5)
    
    def test_bool_empty(self):
        """bool() для пустого стека — False."""
        stack = Stack()
        self.assertFalse(bool(stack))
    
    def test_bool_not_empty(self):
        """bool() для непустого стека — True."""
        stack = Stack([1])
        self.assertTrue(bool(stack))
    
    def test_if_statement(self):
        """Стек работает в if."""
        stack = Stack()
        if stack:
            self.fail("Пустой стек не должен быть truthy")
        
        stack.push(1)
        if not stack:
            self.fail("Непустой стек должен быть truthy")
    
    def test_iter(self):
        """Итерация по стеку (от вершины к основанию)."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        items = list(stack)
        self.assertEqual(items, [3, 2, 1])
    
    def test_iter_for_loop(self):
        """Стек работает в for."""
        stack = Stack([1, 2, 3])
        result = []
        for item in stack:
            result.append(item)
        self.assertEqual(len(result), 3)


class TestQueueBasic(unittest.TestCase):
    """Базовые тесты Queue."""
    
    def test_create_empty(self):
        """Создание пустой очереди."""
        queue = Queue()
        self.assertTrue(queue.is_empty())
    
    def test_create_from_iterable(self):
        """Создание очереди из iterable."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)
    
    def test_enqueue(self):
        """enqueue() добавляет элемент."""
        queue = Queue()
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
    
    def test_dequeue(self):
        """dequeue() возвращает и удаляет первый элемент."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        result = queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 1)
    
    def test_dequeue_order_fifo(self):
        """dequeue() соблюдает FIFO."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
    
    def test_dequeue_empty_raises(self):
        """dequeue() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError) as context:
            queue.dequeue()
        self.assertIn("empty", str(context.exception).lower())
    
    def test_front(self):
        """front() возвращает первый элемент без удаления."""
        queue = Queue([1, 2, 3])
        result = queue.front()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 3)
    
    def test_front_empty_raises(self):
        """front() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.front()


class TestQueueMagicMethods(unittest.TestCase):
    """Тесты магических методов Queue."""
    
    def test_len(self):
        """len() для очереди."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)
    
    def test_bool_empty(self):
        """bool() для пустой очереди."""
        queue = Queue()
        self.assertFalse(bool(queue))
    
    def test_bool_not_empty(self):
        """bool() для непустой очереди."""
        queue = Queue([1])
        self.assertTrue(bool(queue))
    
    def test_iter(self):
        """Итерация по очереди (от начала к концу)."""
        queue = Queue([1, 2, 3])
        items = list(queue)
        self.assertEqual(items, [1, 2, 3])


class TestStackAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Stack."""
    
    def test_clear(self):
        """clear() очищает стек."""
        stack = Stack([1, 2, 3])
        stack.clear()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)
    
    def test_contains(self):
        """contains() проверяет наличие элемента."""
        stack = Stack([1, 2, 3])
        self.assertTrue(stack.contains(2))
        self.assertFalse(stack.contains(5))
    
    def test_in_operator(self):
        """Оператор in работает."""
        stack = Stack([1, 2, 3])
        self.assertIn(2, stack)
        self.assertNotIn(5, stack)
    
    def test_maxsize(self):
        """Ограничение размера стека."""
        stack = Stack(maxsize=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(OverflowError):
            stack.push(4)


class TestQueueAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Queue."""
    
    def test_clear(self):
        """clear() очищает очередь."""
        queue = Queue([1, 2, 3])
        queue.clear()
        self.assertTrue(queue.is_empty())
    
    def test_contains(self):
        """contains() проверяет наличие элемента."""
        queue = Queue([1, 2, 3])
        self.assertTrue(queue.contains(2))
        self.assertFalse(queue.contains(5))
    
    def test_in_operator(self):
        """Оператор in работает."""
        queue = Queue([1, 2, 3])
        self.assertIn(2, queue)
        self.assertNotIn(5, queue)
    
    def test_maxsize(self):
        """Ограничение размера очереди."""
        queue = Queue(maxsize=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        with self.assertRaises(OverflowError):
            queue.enqueue(4)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestStackBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestStackMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestStackAdditional))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueAdditional))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from logger import Logger, log_calls


class TestLoggerSingleton(unittest.TestCase):
    """Тесты паттерна Singleton."""
    
    def setUp(self):
        """Сброс singleton перед каждым тестом."""
        Logger._instance = None
    
    def test_singleton_same_instance(self):
        """Два вызова возвращают один экземпляр."""
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)
    
    def test_singleton_id(self):
        """id() одинаков для всех экземпляров."""
        logger1 = Logger()
        logger2 = Logger()
        self.assertEqual(id(logger1), id(logger2))


class TestLoggerLevels(unittest.TestCase):
    """Тесты уровней логирования."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
    
    def test_level_constants_exist(self):
        """Константы уровней существуют."""
        self.assertTrue(hasattr(Logger, 'DEBUG'))
        self.assertTrue(hasattr(Logger, 'INFO'))
        self.assertTrue(hasattr(Logger, 'WARNING'))
        self.assertTrue(hasattr(Logger, 'ERROR'))
        self.assertTrue(hasattr(Logger, 'CRITICAL'))
    
    def test_level_order(self):
        """Уровни упорядочены по важности."""
        self.assertLess(Logger.DEBUG, Logger.INFO)
        self.assertLess(Logger.INFO, Logger.WARNING)
        self.assertLess(Logger.WARNING, Logger.ERROR)
        self.assertLess(Logger.ERROR, Logger.CRITICAL)
    
    def test_set_level(self):
        """set_level() устанавливает уровень."""
        self.logger.set_level(Logger.WARNING)
        # Не должно падать
    
    def test_filter_by_level(self):
        """Сообщения ниже уровня не логируются."""
        self.logger.set_level(Logger.WARNING)
        self.logger.debug("Debug")
        self.logger.info("Info")
        self.logger.warning("Warning")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertIn("Warning", logs[0])


class TestLoggerMethods(unittest.TestCase):
    """Тесты методов логирования."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_debug(self):
        """debug() создаёт запись."""
        self.logger.debug("Test debug")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertIn("DEBUG", logs[0])
        self.assertIn("Test debug", logs[0])
    
    def test_info(self):
        """info() создаёт запись."""
        self.logger.info("Test info")
        logs = self.logger.get_logs()
        self.assertIn("INFO", logs[0])
    
    def test_warning(self):
        """warning() создаёт запись."""
        self.logger.warning("Test warning")
        logs = self.logger.get_logs()
        self.assertIn("WARNING", logs[0])
    
    def test_error(self):
        """error() создаёт запись."""
        self.logger.error("Test error")
        logs = self.logger.get_logs()
        self.assertIn("ERROR", logs[0])
    
    def test_critical(self):
        """critical() создаёт запись."""
        self.logger.critical("Test critical")
        logs = self.logger.get_logs()
        self.assertIn("CRITICAL", logs[0])
    
    def test_log_format_contains_timestamp(self):
        """Запись содержит временную метку."""
        self.logger.info("Test")
        logs = self.logger.get_logs()
        # Проверяем наличие формата даты
        import re
        pattern = r'\d{4}-\d{2}-\d{2}'
        self.assertTrue(re.search(pattern, logs[0]))
    
    def test_log_format_contains_time(self):
        """Запись содержит время."""
        self.logger.info("Test")
        logs = self.logger.get_logs()
        import re
        pattern = r'\d{2}:\d{2}:\d{2}'
        self.assertTrue(re.search(pattern, logs[0]))


class TestLoggerGetLogs(unittest.TestCase):
    """Тесты получения логов."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_get_logs_empty(self):
        """get_logs() возвращает пустой список."""
        logs = self.logger.get_logs()
        self.assertEqual(logs, [])
    
    def test_get_logs_multiple(self):
        """get_logs() возвращает все записи."""
        self.logger.info("First")
        self.logger.warning("Second")
        self.logger.error("Third")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 3)
    
    def test_get_logs_by_level(self):
        """get_logs_by_level() фильтрует записи."""
        self.logger.info("Info message")
        self.logger.warning("Warning message")
        self.logger.error("Error message")
        
        errors = self.logger.get_logs_by_level(Logger.ERROR)
        self.assertEqual(len(errors), 1)
        self.assertIn("Error message", errors[0])
    
    def test_get_logs_by_level_multiple(self):
        """get_logs_by_level() для нескольких записей одного уровня."""
        self.logger.warning("Warning 1")
        self.logger.info("Info")
        self.logger.warning("Warning 2")
        
        warnings = self.logger.get_logs_by_level(Logger.WARNING)
        self.assertEqual(len(warnings), 2)


class TestLogCallsDecorator(unittest.TestCase):
    """Тесты декоратора log_calls."""
    
    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)
    
    def test_decorator_logs_call(self):
        """Декоратор логирует вызов функции."""
        @log_calls
        def sample_function(x, y):
            return x + y
        
        result = sample_function(2, 3)
        logs = self.logger.get_logs()
        
        self.assertGreater(len(logs), 0)
    
    def test_decorator_logs_function_name(self):
        """Декоратор логирует имя функции."""
        @log_calls
        def my_special_function():
            return 42
        
        my_special_function()
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("my_special_function", log_text)
    
    def test_decorator_preserves_return_value(self):
        """Декоратор не изменяет возвращаемое значение."""
        @log_calls
        def add(a, b):
            return a + b
        
        result = add(10, 20)
        self.assertEqual(result, 30)
    
    def test_decorator_logs_arguments(self):
        """Декоратор логирует аргументы."""
        @log_calls
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"
        
        greet("Alice")
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("Alice", log_text)
    
    def test_decorator_logs_result(self):
        """Декоратор логирует результат."""
        @log_calls
        def multiply(a, b):
            return a * b
        
        multiply(7, 6)
        logs = self.logger.get_logs()
        
        log_text = ' '.join(logs)
        self.assertIn("42", log_text)


class TestLoggerFile(unittest.TestCase):
    """Тесты дополнительного задания: запись в файл."""
    
    def setUp(self):
        Logger._instance = None
        self.test_file = "test_log.txt"
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_file_logging(self):
        """Логирование в файл."""
        logger = Logger(filename=self)

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

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shop import Product, CartItem, ShoppingCart, Order, Store


class TestProduct(unittest.TestCase):
    """Тесты класса Product."""
    
    def test_creation(self):
        """Product создаётся с правильными атрибутами."""
        product = Product("P001", "Ноутбук", 50000, 10)
        self.assertEqual(product.product_id, "P001")
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.quantity, 10)
    
    def test_negative_price_raises(self):
        """Отрицательная цена вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", -100, 10)
    
    def test_zero_price_raises(self):
        """Нулевая цена вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", 0, 10)
    
    def test_negative_quantity_raises(self):
        """Отрицательное количество вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", 100, -5)
    
    def test_is_available_true(self):
        """is_available() возвращает True когда товар есть."""
        product = Product("P001", "Товар", 100, 10)
        self.assertTrue(product.is_available())
        self.assertTrue(product.is_available(5))
        self.assertTrue(product.is_available(10))
    
    def test_is_available_false(self):
        """is_available() возвращает False когда товара недостаточно."""
        product = Product("P001", "Товар", 100, 5)
        self.assertFalse(product.is_available(10))
    
    def test_is_available_zero_stock(self):
        """is_available() для товара с нулевым остатком."""
        product = Product("P001", "Товар", 100, 0)
        self.assertFalse(product.is_available())
    
    def test_reduce_stock(self):
        """reduce_stock() уменьшает количество."""
        product = Product("P001", "Товар", 100, 10)
        product.reduce_stock(3)
        self.assertEqual(product.quantity, 7)
    
    def test_reduce_stock_insufficient_raises(self):
        """reduce_stock() с недостаточным количеством вызывает ValueError."""
        product = Product("P001", "Товар", 100, 5)
        with self.assertRaises(ValueError):
            product.reduce_stock(10)
    
    def test_restock(self):
        """restock() увеличивает количество."""
        product = Product("P001", "Товар", 100, 10)
        product.restock(5)
        self.assertEqual(product.quantity, 15)
    
    def test_str(self):
        """__str__() возвращает информацию о товаре."""
        product = Product("P001", "Ноутбук", 50000, 10)
        s = str(product)
        self.assertIn("Ноутбук", s)
        self.assertIn("50000", s)


class TestCartItem(unittest.TestCase):
    """Тесты класса CartItem."""
    
    def setUp(self):
        self.product = Product("P001", "Товар", 1000, 10)
    
    def test_creation(self):
        """CartItem создаётся с product и quantity."""
        item = CartItem(self.product, 3)
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 3)
    
    def test_get_total(self):
        """get_total() возвращает стоимость."""
        item = CartItem(self.product, 3)
        self.assertEqual(item.get_total(), 3000)
    
    def test_update_quantity(self):
        """update_quantity() изменяет количество."""
        item = CartItem(self.product, 3)
        item.update_quantity(5)
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.get_total(), 5000)
    
    def test_update_quantity_zero_raises(self):
        """update_quantity(0) вызывает ValueError."""
        item = CartItem(self.product, 3)
        with self.assertRaises(ValueError):
            item.update_quantity(0)
    
    def test_update_quantity_negative_raises(self):
        """Отрицательное количество вызывает ValueError."""
        item = CartItem(self.product, 3)
        with self.assertRaises(ValueError):
            item.update_quantity(-1)


class TestShoppingCart(unittest.TestCase):
    """Тесты класса ShoppingCart."""
    
    def setUp(self):
        self.cart = ShoppingCart()
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)
    
    def test_empty_cart(self):
        """Новая корзина пуста."""
        self.assertEqual(len(self.cart), 0)
        self.assertEqual(self.cart.get_total(), 0)
    
    def test_add_item(self):
        """add_item() добавляет товар."""
        self.cart.add_item(self.laptop, 2)
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart.get_total(), 100000)
    
    def test_add_item_multiple_products(self):
        """Добавление нескольких товаров."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.assertEqual(len(self.cart), 2)
        self.assertEqual(self.cart.get_total(), 104500)
    
    def test_add_item_same_product_increases_quantity(self):
        """Повторное добавление увеличивает количество."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.laptop, 3)
        self.assertEqual(len(self.cart), 1)
        items = self.cart.get_items()
        self.assertEqual(items[0].quantity, 5)
    
    def test_remove_item(self):
        """remove_item() удаляет товар."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.cart.remove_item("P001")
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart.get_total(), 4500)
    
    def test_remove_nonexistent_raises(self):
        """remove_item() для несуществующего товара вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.cart.remove_item("NONEXISTENT")
    
    def test_update_item_quantity(self):
        """update_item_quantity() изменяет количество."""
        self.cart.add_item(self.laptop, 2)
        self.cart.update_item_quantity("P001", 5)
        self.assertEqual(self.cart.get_total(), 250000)
    
    def test_get_items(self):
        """get_items() возвращает список CartItem."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        items = self.cart.get_items()
        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], CartItem)
    
    def test_clear(self):
        """clear() очищает корзину."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.cart.clear()
        self.assertEqual(len(self.cart), 0)
        self.assertEqual(self.cart.get_total(), 0)


class TestOrder(unittest.TestCase):
    """Тесты класса Order."""
    
    def setUp(self):
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)
        self.cart = ShoppingCart()
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
    
    def test_creation(self):
        """Order создаётся с правильными атрибутами."""
        order = Order("O001", self.cart, "Иван Петров")
        self.assertEqual(order.order_id, "O001")
        self.assertEqual(order.customer_name, "Иван Петров")
    
    def test_initial_status_pending(self):
        """Начальный статус — PENDING."""
        order = Order("O001", self.cart, "Иван")
        self.assertEqual(order.status, Order.PENDING)
    
    def test_get_total(self):
        """get_total() возвращает сумму заказа."""
        order = Order("O001", self.cart, "Иван")
        self.assertEqual(order.get_total(), 104500)
    
    def test_confirm(self):
        """confirm() подтверждает заказ и списывает товары."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        self.assertEqual(order.status, Order.CONFIRMED)
        self.assertEqual(self.laptop.quantity, 8)  # 10 - 2
        self.assertEqual(self.mouse.quantity, 47)   # 50 - 3
    
    def test_confirm_insufficient_stock_raises(self):
        """confirm() при недостатке товара вызывает ValueError."""
        self.laptop.quantity = 1  # Меньше чем в корзине (2)
        order = Order("O001", self.cart, "Иван")
        with self.assertRaises(ValueError):
            order.confirm()
    
    def test_ship(self):
        """ship() отправляет подтверждённый заказ."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        self.assertEqual(order.status, Order.SHIPPED)
    
    def test_ship_pending_raises(self):
        """ship() для неподтверждённого заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        with self.assertRaises(ValueError):
            order.ship()
    
    def test_deliver(self):
        """deliver() доставляет отправленный заказ."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        order.deliver()
        self.assertEqual(order.status, Order.DELIVERED)
    
    def test_deliver_not_shipped_raises(self):
        """deliver() для неотправленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        with self.assertRaises(ValueError):
            order.deliver()
    
    def test_cancel_pending(self):
        """cancel() отменяет неподтверждённый заказ."""
        order = Order("O001", self.cart, "Иван")
        order.cancel()
        self.assertEqual(order.status, Order.CANCELLED)
    
    def test_cancel_confirmed_returns_stock(self):
        """cancel() возвращает товары на склад."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        self.assertEqual(self.laptop.quantity, 8)
        order.cancel()
        self.assertEqual(order.status, Order.CANCELLED)
        self.assertEqual(self.laptop.quantity, 10)  # Возвращены
    
    def test_cancel_shipped_raises(self):
        """cancel() для отправленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        with self.assertRaises(ValueError):
            order.cancel()
    
    def test_cancel_delivered_raises(self):
        """cancel() для доставленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        order.deliver()
        with self.assertRaises(ValueError):
            order.cancel()


class TestStore(unittest.TestCase):
    """Тесты класса Store."""
    
    def setUp(self):
        self.store = Store("TechShop")
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)
    
    def test_creation(self):
        """Store создаётся с именем."""
        self.assertEqual(self.store.name, "TechShop")
    
    def test_add_product(self):
        """add_product() добавляет товар."""
        self.store.add_product(self.laptop)
        product = self.store.get_product("P001")
        self.assertEqual(product, self.laptop)
    
    def test_add_duplicate_product_raises(self):
        """Добавление товара с существующим ID вызывает ValueError."""
        self.store.add_product(self.laptop)
        duplicate = Product("P001", "Другой", 100, 5)
        with self.assertRaises(ValueError):
            self.store.add_product(duplicate)
    
    def test_get_product(self):
        """get_product() возвращает товар по ID."""
        self.store.add_product(self.laptop)
        self.store.add_product(self.mouse)
        product = self.store.get_product("P002")
        self.assertEqual(product.name, "Мышь")
    
    def test_get_product_nonexistent_raises(self):
        """get_product() для несуществующего товара вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.store.get_product("NONEXISTENT")
    
    def test_get_available_products(self):
        """get_available_products() возвращает товары в наличии."""
        self.laptop.quantity = 0
        self.store.add_product(self.laptop)
        self.store.add_product(self.mouse)
        available = self.store.get_available_products()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].name, "Мышь")
    
    def test_create_order(self):
        """create_order() создаёт заказ."""
        self.store.add_product(self.laptop)
        cart = ShoppingCart()
        cart.add_item(self.laptop, 2)
        order = self.store.create_order(cart, "Иван")
        self.assertIsInstance(order, Order)
    
    def test_get_order(self):
        """get_order() возвращает заказ по ID."""
        self.store.add_product(self.laptop)
        cart = ShoppingCart()
        cart.add_item(self.laptop, 1)
        order = self.store.create_order(cart, "Иван")
        found = self.store.get_order(order.order_id)
        self.assertEqual(found, order)


class TestDiscount(unittest.TestCase):
    """Тесты дополнительного задания: скидки."""
    
    def setUp(self):
        self.cart = ShoppingCart()
        self.product = Product("P001", "Товар", 1000, 10)
        self.cart.add_item(self.product, 5)  # 5000
    
    def test_percentage_discount(self):
        """Процентная скидка."""
        from shop import Discount
        discount = Discount(percentage=10)  # 10%
        self.cart.apply_discount(discount)
        self.assertEqual(self.cart.get_total(), 4500)
    
    def test_fixed_discount(self):
        """Фиксированная скидка."""
        from shop import Discount
        discount = Discount(fixed=500)
        self.cart.apply_discount(discount)
        self.assertEqual(self.cart.get_total(), 4500)
    
    def test_discount_not_below_zero(self):
        """Скидка не делает сумму отрицательной."""
        from shop import Discount
        discount = Discount(fixed=10000)
        self.cart.apply_discount(discount)
        self.assertGreaterEqual(self.cart.get_total(), 0)


class TestOrderHistory(unittest.TestCase):
    """Тесты дополнительного задания: история заказов."""
    
    def test_get_order_history(self):
        """get_order_history() возвращает заказы клиента."""
        store = Store("Test")
        product = Product("P001", "Товар", 100, 100)
        store.add_product(product)
        
        cart1 = ShoppingCart()
        cart1.add_item(product, 1)
        order1 = store.create_order(cart1, "Иван")
        
        cart2 = ShoppingCart()
        cart2.add_item(product, 2)
        order2 = store.create_order(cart2, "Иван")
        
        cart3 = ShoppingCart()
        cart3.add_item(product, 1)
        order3 = store.create_order(cart3, "Пётр")
        
        ivan_orders = store.get_order_history("Иван")
        self.assertEqual(len(ivan_orders), 2)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestProduct))
    suite.addTests(loader.loadTestsFromTestCase(TestCartItem))
    suite.addTests(loader.loadTestsFromTestCase(TestShoppingCart))
    suite.addTests(loader.loadTestsFromTestCase(TestOrder))
    suite.addTests(loader.loadTestsFromTestCase(TestStore))
    
    # Дополнительные тесты
    try:
        from shop import Discount
        suite.addTests(loader.loadTestsFromTestCase(TestDiscount))
    except ImportError:
        print("Discount не реализован")
    
    suite.addTests(loader.loadTestsFromTestCase(TestOrderHistory))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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

```python
import unittest
import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from orm import (
    Field, StringField, IntegerField, EmailField, BooleanField, Model
)


class TestStringField(unittest.TestCase):
    """Тесты StringField."""
    
    def test_valid_string(self):
        """Валидная строка принимается."""
        class TestModel(Model):
            name = StringField()
        
        obj = TestModel(name="John")
        self.assertEqual(obj.name, "John")
        self.assertTrue(obj.is_valid())
    
    def test_min_length(self):
        """Проверка минимальной длины."""
        class TestModel(Model):
            name = StringField(min_length=3)
        
        obj = TestModel(name="ab")
        self.assertFalse(obj.is_valid())
        errors = obj.validate()
        self.assertTrue(any("min" in e.lower() or "длин" in e.lower() for e in errors))
    
    def test_max_length(self):
        """Проверка максимальной длины."""
        class TestModel(Model):
            name = StringField(max_length=5)
        
        obj = TestModel(name="toolongname")
        self.assertFalse(obj.is_valid())
    
    def test_non_string_fails(self):
        """Не-строка не проходит валидацию."""
        class TestModel(Model):
            name = StringField()
        
        obj = TestModel(name=123)
        self.assertFalse(obj.is_valid())
    
    def test_required_missing(self):
        """Обязательное поле без значения."""
        class TestModel(Model):
            name = StringField(required=True)
        
        obj = TestModel()
        self.assertFalse(obj.is_valid())
    
    def test_not_required_missing(self):
        """Необязательное поле без значения."""
        class TestModel(Model):
            name = StringField(required=False)
        
        obj = TestModel()
        self.assertTrue(obj.is_valid())
    
    def test_default_value(self):
        """Значение по умолчанию."""
        class TestModel(Model):
            name = StringField(default="Unknown")
        
        obj = TestModel()
        self.assertEqual(obj.name, "Unknown")


class TestIntegerField(unittest.TestCase):
    """Тесты IntegerField."""
    
    def test_valid_integer(self):
        """Валидное целое число."""
        class TestModel(Model):
            age = IntegerField()
        
        obj = TestModel(age=25)
        self.assertEqual(obj.age, 25)
        self.assertTrue(obj.is_valid())
    
    def test_min_value(self):
        """Проверка минимального значения."""
        class TestModel(Model):
            age = IntegerField(min_value=0)
        
        obj = TestModel(age=-5)
        self.assertFalse(obj.is_valid())
    
    def test_max_value(self):
        """Проверка максимального значения."""
        class TestModel(Model):
            age = IntegerField(max_value=150)
        
        obj = TestModel(age=200)
        self.assertFalse(obj.is_valid())
    
    def test_range(self):
        """Проверка диапазона."""
        class TestModel(Model):
            age = IntegerField(min_value=0, max_value=150)
        
        valid = TestModel(age=50)
        self.assertTrue(valid.is_valid())
        
        too_low = TestModel(age=-1)
        self.assertFalse(too_low.is_valid())
        
        too_high = TestModel(age=151)
        self.assertFalse(too_high.is_valid())
    
    def test_non_integer_fails(self):
        """Не-целое число не проходит валидацию."""
        class TestModel(Model):
            age = IntegerField()
        
        obj = TestModel(age="twenty")
        self.assertFalse(obj.is_valid())
    
    def test_float_fails(self):
        """Float не проходит валидацию."""
        class TestModel(Model):
            age = IntegerField()
        
        obj = TestModel(age=25.5)
        self.assertFalse(obj.is_valid())


class TestEmailField(unittest.TestCase):
    """Тесты EmailField."""
    
    def test_valid_email(self):
        """Валидный email."""
        class TestModel(Model):
            email = EmailField()
        
        obj = TestModel(email="user@example.com")
        self.assertTrue(obj.is_valid())
    
    def test_valid_email_subdomain(self):
        """Email с поддоменом."""
        class TestModel(Model):
            email = EmailField()
        
        obj = TestModel(email="user@mail.example.com")
        self.assertTrue(obj.is_valid())
    
    def test_invalid_email_no_at(self):
        """Email без @."""
        class TestModel(Model):
            email = EmailField()
        
        obj = TestModel(email="userexample.com")
        self.assertFalse(obj.is_valid())
    
    def test_invalid_email_no_dot(self):
        """Email без точки после @."""
        class TestModel(Model):
            email = EmailField()
        
        obj = TestModel(email="user@examplecom")
        self.assertFalse(obj.is_valid())
    
    def test_invalid_email_empty_parts(self):
        """Email с пустыми частями."""
        class TestModel(Model):
            email = EmailField()
        
        obj = TestModel(email="@example.com")
        self.assertFalse(obj.is_valid())


class TestBooleanField(unittest.TestCase):
    """Тесты BooleanField."""
    
    def test_true_value(self):
        """True значение."""
        class TestModel(Model):
            active = BooleanField()
        
        obj = TestModel(active=True)
        self.assertTrue(obj.is_valid())
        self.assertTrue(obj.active)
    
    def test_false_value(self):
        """False значение."""
        class TestModel(Model):
            active = BooleanField()
        
        obj = TestModel(active=False)
        self.assertTrue(obj.is_valid())
        self.assertFalse(obj.active)
    
    def test_non_boolean_fails(self):
        """Не-булево значение не проходит."""
        class TestModel(Model):
            active = BooleanField()
        
        obj = TestModel(active="yes")
        self.assertFalse(obj.is_valid())
    
    def test_integer_fails(self):
        """Целое число не проходит (даже 0 или 1)."""
        class TestModel(Model):
            active = BooleanField()
        
        obj = TestModel(active=1)
        self.assertFalse(obj.is_valid())
    
    def test_default_value(self):
        """Значение по умолчанию."""
        class TestModel(Model):
            active = BooleanField(default=True)
        
        obj = TestModel()
        self.assertTrue(obj.active)


class TestModel(unittest.TestCase):
    """Тесты базового класса Model."""
    
    def setUp(self):
        """Создание тестовой модели."""
        class User(Model):
            username = StringField(min_length=3, max_length=20)
            email = EmailField()
            age = IntegerField(min_value=0, max_value=150, required=False, default=None)
            is_active = BooleanField(default=True)
        
        self.User = User
    
    def test_model_creation(self):
        """Создание модели с полями."""
        user = self.User(username="john_doe", email="john@example.com")
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")
    
    def test_model_defaults(self):
        """Значения по умолчанию применяются."""
        user = self.User(username="john", email="john@example.com")
        self.assertIsNone(user.age)
        self.assertTrue(user.is_active)
    
    def test_is_valid_true(self):
        """is_valid() для валидной модели."""
        user = self.User(username="john_doe", email="john@example.com", age=25)
        self.assertTrue(user.is_valid())
    
    def test_is_valid_false(self):
        """is_valid() для невалидной модели."""
        user = self.User(username="ab", email="invalid")
        self.assertFalse(user.is_valid())
    
    def test_validate_returns_errors(self):
        """validate() возвращает список ошибок."""
        user = self.User(username="ab", email="invalid")
        errors = user.validate()
        self.assertIsInstance(errors, list)
        self.assertGreater(len(errors), 0)
    
    def test_validate_empty_for_valid(self):
        """validate() возвращает пустой список для валидной модели."""
        user = self.User(username="john_doe", email="john@example.com")
        errors = user.validate()
        self.assertEqual(errors, [])
    
    def test_to_dict(self):
        """to_dict() сериализует модель."""
        user = self.User(username="john_doe", email="john@example.com", age=25)
        data = user.to_dict()
        self.assertEqual(data['username'], "john_doe")
        self.assertEqual(data['email'], "john@example.com")
        self.assertEqual(data['age'], 25)
        self.assertTrue(data['is_active'])
    
    def test_from_dict(self):
        """from_dict() создаёт модель из словаря."""
        data = {
            'username': 'jane_doe',
            'email': 'jane@example.com',
            'age': 30,
            'is_active': False
        }
        user = self.User.from_dict(data)
        self.assertEqual(user.username, 'jane_doe')
        self.assertEqual(user.email, 'jane@example.com')
        self.assertEqual(user.age, 30)
        self.assertFalse(user.is_active)
    
    def test_equality(self):
        """Сравнение моделей по значениям полей."""
        user1 = self.User(username="john", email="john@example.com", age=25)
        user2 = self.User(username="john", email="john@example.com", age=25)
        user3 = self.User(username="jane", email="jane@example.com", age=30)
        
        self.assertEqual(user1, user2)
        self.assertNotEqual(user1, user3)
    
    def test_str(self):
        """__str__() возвращает читаемое представление."""
        user = self.User(username="john", email="john@example.com")
        s = str(user)
        self.assertIn("john", s)
        self.assertIn("User", s)
    
    def test_field_modification(self):
        """Поля можно изменять."""
        user = self.User(username="john", email="john@example.com")
        user.username = "jane"
        self.assertEqual(user.username, "jane")
    
    def test_roundtrip_serialization(self):
        """Сериализация и десериализация сохраняют данные."""
        original = self.User(username="test_user", email="test@example.com", age=42)
        data = original.to_dict()
        restored = self.User.from_dict(data)
        self.assertEqual(original, restored)


class TestModelDescriptor(unittest.TestCase):
    """Тесты работы дескрипторов."""
    
    def test_descriptor_per_instance(self):
        """Каждый экземпляр хранит свои значения."""
        class TestModel(Model):
            name = StringField()
        
        obj1 = TestModel(name="First")
        obj2 = TestModel(name="Second")
        
        self.assertEqual(obj1.name, "First")
        self.assertEqual(obj2.name, "Second")
        
        obj1.name = "Modified"
        self.assertEqual(obj1.name, "Modified")
        self.assertEqual(obj2.name, "Second")
    
    def test_field_names_discovered(self):
        """Модель знает имена своих полей."""
        class TestModel(Model):
            field1 = StringField()
            field2 = IntegerField()
        
        # Проверяем, что to_dict() содержит все поля
        obj = TestModel(field1="test", field2=123)
        data = obj.to_dict()
        self.assertIn('field1', data)
        self.assertIn('field2', data)


class TestListField(unittest.TestCase):
    """Тесты дополнительного задания: ListField."""
    
    def test_list_field_valid(self):
        """ListField принимает список."""
        from orm import ListField
        
        class TestModel(Model):
            tags = ListField(item_type=str)
        
        obj = TestModel(tags=["python", "oop"])
        self.assertTrue(obj.is_valid())
        self.assertEqual(obj.tags, ["python", "oop"])
    
    def test_list_field_item_type(self):
        """ListField проверяет тип элементов."""
        from orm import ListField
        
        class TestModel(Model):
            numbers = ListField(item_type=int)
        
        valid = TestModel(numbers=[1, 2, 3])
        self.assertTrue(valid.is_valid())
        
        invalid = TestModel(numbers=[1, "two", 3])
        self.assertFalse(invalid.is_valid())
    
    def test_list_field_non_list_fails(self):
        """ListField не принимает не-список."""
        from orm import ListField
        
        class TestModel(Model):
            items = ListField()
        
        obj = TestModel(items="not a list")
        self.assertFalse(obj.is_valid())


class TestDateField(unittest.TestCase):
    """Тесты дополнительного задания: DateField."""
    
    def test_date_field_valid(self):
        """DateField принимает дату."""
        from orm import DateField
        
        class TestModel(Model):
            birthday = DateField()
        
        obj = TestModel(birthday=date(1990, 5, 15))
        self.assertTrue(obj.is_valid())
    
    def test_date_field_from_string(self):
        """DateField парсит строку."""
        from orm import DateField
        
        class TestModel(Model):
            birthday = DateField(format="%Y-%m-%d")
        
        obj = TestModel(birthday="1990-05-15")
        self.assertTrue(obj.is_valid())
        self.assertEqual(obj.birthday, date(1990, 5, 15))
    
    def test_date_field_invalid_format(self):
        """DateField отклоняет неверный формат."""
        from orm import DateField
        
        class TestModel(Model):
            birthday = DateField(format="%Y-%m-%d")
        
        obj = TestModel(birthday="15/05/1990")
        self.assertFalse(obj.is_valid())


class TestNestedModel(unittest.TestCase):
    """Тесты дополнительного задания: вложенные модели."""
    
    def test_nested_model(self):
        """Модель как поле другой модели."""
        from orm import ModelField
        
        class Address(Model):
            city = StringField()
            street = StringField()
        
        class Person(Model):
            name = StringField()
            address = ModelField(Address)
        
        addr = Address(city="Moscow", street="Tverskaya")
        person = Person(name="Ivan", address=addr)
        
        self.assertTrue(person.is_valid())
        self.assertEqual(person.address.city, "Moscow")
    
    def test_nested_model_to_dict(self):
        """Вложенная модель сериализуется."""
        from orm import ModelField
        
        class Address(Model):
            city = StringField()
        
        class Person(Model):
            name = StringField()
            address = ModelField(Address)
        
        person = Person(name="Ivan", address=Address(city="Moscow"))
        data = person.to_dict()
        
        self.assertIn('address', data)
        self.assertEqual(data['address']['city'], "Moscow")
    
    def test_nested_model_from_dict(self):
        """Вложенная модель десериализуется."""
        from orm import ModelField
        
        class Address(Model):
            city = StringField()
        
        class Person(Model):
            name = StringField()
            address = ModelField(Address)
        
        data = {
            'name': 'Ivan',
            'address': {'city': 'Moscow'}
        }
        person = Person.from_dict(data)
        
        self.assertEqual(person.name, "Ivan")
        self.assertIsInstance(person.address, Address)
        self.assertEqual(person.address.city, "Moscow")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestStringField))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegerField))
    suite.addTests(loader.loadTestsFromTestCase(TestEmailField))
    suite.addTests(loader.loadTestsFromTestCase(TestBooleanField))
    suite.addTests(loader.loadTestsFromTestCase(TestModel))
    suite.addTests(loader.loadTestsFromTestCase(TestModelDescriptor))
    
    # Дополнительные тесты
    try:
        from orm import ListField
        suite.addTests(loader.loadTestsFromTestCase(TestListField))
    except ImportError:
        print("ListField не реализован")
    
    try:
        from orm import DateField
        suite.addTests(loader.loadTestsFromTestCase(TestDateField))
    except ImportError:
        print("DateField не реализован")
    
    try:
        from orm import ModelField
        suite.addTests(loader.loadTestsFromTestCase(TestNestedModel))
    except ImportError:
        print("ModelField не реализован")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)
```

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
