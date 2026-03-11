import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.shapes import Shape, Circle, Rectangle, Triangle


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
        big = Rectangle(3, 3)  # площадь = 9
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
            Circle(1),  # ≈ 3.14
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