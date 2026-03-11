import unittest
import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.orm import (
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