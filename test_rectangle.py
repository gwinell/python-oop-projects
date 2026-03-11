import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.rectangle import Rectangle


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
        expected = math.sqrt(1.5 ** 2 + 2 ** 2)
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