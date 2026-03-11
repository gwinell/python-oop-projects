import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.counter import Counter


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
        counter.increment()  # 101
        counter.increment()  # 102
        counter.decrement()  # 101
        counter.increment()  # 102
        counter.decrement()  # 101
        counter.decrement()  # 100
        counter.decrement()  # 99
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
        counter.increment()  # 1
        counter.increment()  # 2
        counter.decrement()  # 1
        counter.reset()  # 0
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