"""
Автотесты для задачи 1: Счётчик
Запуск: python -m pytest test_counter.py -v
Или без pytest: python test_counter.py
"""

import unittest
from solutions.counter import Counter


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