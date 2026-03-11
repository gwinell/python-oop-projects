import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.employees import Employee, Manager, Developer, Intern, Company


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