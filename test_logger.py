import unittest
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.logger import Logger, log_calls


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

    def test_file_logging(self):
        """Логирование в файл."""
        logger = Logger(filename=self.test_file)
        logger.set_level(Logger.INFO)
        logger.info("Test message")
        logger.warning("Warning message")

        # Проверяем, что файл создан
        self.assertTrue(os.path.exists(self.test_file))

        # Проверяем содержимое файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("Test message", content)
            self.assertIn("Warning message", content)

    def test_file_append_mode(self):
        """Логирование в файл в режиме добавления."""
        # Первая запись
        logger1 = Logger(filename=self.test_file)
        logger1.set_level(Logger.INFO)
        logger1.info("First message")

        # Вторая запись (должна добавиться, а не перезаписать)
        logger2 = Logger(filename=self.test_file)
        logger2.set_level(Logger.INFO)
        logger2.info("Second message")

        with open(self.test_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)

    def test_file_without_filename(self):
        """Без filename логирование идёт только в память."""
        logger = Logger()  # Без filename
        logger.set_level(Logger.INFO)
        logger.info("Memory only")

        # Файл не должен создаваться
        self.assertFalse(os.path.exists("test_log.txt"))


class TestLoggerAdvancedFormatting(unittest.TestCase):
    """Тесты дополнительного задания: форматтер."""

    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)

    def test_custom_format(self):
        """Установка пользовательского формата."""
        custom_format = "{level} | {time} | {message}"
        self.logger.set_format(custom_format)
        self.logger.info("Custom format test")

        logs = self.logger.get_logs()
        self.assertIn("INFO |", logs[0])
        self.assertIn("| Custom format test", logs[0])

    def test_format_without_time(self):
        """Формат без временной метки."""
        self.logger.set_format("{level} - {message}")
        self.logger.info("No time")

        logs = self.logger.get_logs()
        import re
        pattern = r'\d{4}-\d{2}-\d{2}'
        self.assertFalse(re.search(pattern, logs[0]))

    def test_format_with_custom_time(self):
        """Формат с пользовательским форматом времени."""
        self.logger.set_format("{level} [{time:%Y/%m/%d %H-%M-%S}] {message}")
        self.logger.info("Custom time format")

        logs = self.logger.get_logs()
        import re
        pattern = r'\d{4}/\d{2}/\d{2} \d{2}-\d{2}-\d{2}'
        self.assertTrue(re.search(pattern, logs[0]))


class TestLoggerContextManager(unittest.TestCase):
    """Тесты дополнительного задания: контекстный менеджер."""

    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.ERROR)  # Только ошибки

    def test_context_manager_changes_level(self):
        """Внутри контекста уровень логирования меняется."""
        with self.logger as log:
            log.set_level(Logger.DEBUG)
            log.debug("Debug inside context")

        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)

    def test_context_manager_restores_level(self):
        """После выхода из контекста уровень восстанавливается."""
        original_level = self.logger.level

        with self.logger as log:
            log.set_level(Logger.DEBUG)
            self.assertNotEqual(log.level, original_level)

        self.assertEqual(self.logger.level, original_level)

    def test_context_manager_exception_restores_level(self):
        """Даже при исключении уровень восстанавливается."""
        original_level = self.logger.level

        try:
            with self.logger as log:
                log.set_level(Logger.DEBUG)
                raise ValueError("Test exception")
        except ValueError:
            pass

        self.assertEqual(self.logger.level, original_level)

    def test_context_manager_temporary_filtering(self):
        """Временное логирование низкоуровневых сообщений."""
        self.logger.set_level(Logger.ERROR)
        self.logger.info("Outside context")  # Не запишется

        with self.logger as log:
            log.set_level(Logger.DEBUG)
            log.debug("Inside context")  # Запишется
            log.info("Also inside")  # Запишется

        self.logger.warning("Outside again")  # Не запишется (уровень WARNING < ERROR)

        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 2)
        self.assertIn("Inside context", logs[0])
        self.assertIn("Also inside", logs[1])


class TestLoggerEdgeCases(unittest.TestCase):
    """Тесты граничных случаев."""

    def setUp(self):
        Logger._instance = None
        self.logger = Logger()

    def test_empty_message(self):
        """Логирование пустого сообщения."""
        self.logger.set_level(Logger.INFO)
        self.logger.info("")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)

    def test_very_long_message(self):
        """Логирование очень длинного сообщения."""
        long_msg = "A" * 10000
        self.logger.set_level(Logger.INFO)
        self.logger.info(long_msg)
        logs = self.logger.get_logs()
        self.assertIn(long_msg, logs[0])

    def test_special_characters(self):
        """Логирование сообщений со спецсимволами."""
        special_msg = "Line1\nLine2\tTab\rReturn"
        self.logger.set_level(Logger.INFO)
        self.logger.info(special_msg)
        logs = self.logger.get_logs()
        # Спецсимволы должны сохраниться как есть или быть экранированы
        self.assertIn("Line1", logs[0])
        self.assertIn("Line2", logs[0])

    def test_unicode_characters(self):
        """Логирование сообщений с Unicode."""
        unicode_msg = "Привет, мир! 🐍 Python"
        self.logger.set_level(Logger.INFO)
        self.logger.info(unicode_msg)
        logs = self.logger.get_logs()
        self.assertIn(unicode_msg, logs[0])

    def test_set_level_invalid(self):
        """Установка несуществующего уровня."""
        with self.assertRaises(AttributeError):
            self.logger.set_level(999)

    def test_get_logs_by_level_nonexistent(self):
        """Запрос логов с несуществующим уровнем."""
        self.logger.set_level(Logger.DEBUG)
        self.logger.info("Test")

        with self.assertRaises(AttributeError):
            self.logger.get_logs_by_level(999)

    def test_file_permission_error(self):
        """Попытка записи в файл без прав."""
        # Этот тест может быть пропущен в некоторых окружениях
        if os.name == 'nt':  # Windows
            readonly_file = "C:\\readonly_test.txt"
            # Попытка создать файл в защищённой директории
            try:
                logger = Logger(filename=readonly_file)
                logger.info("Test")
                # Если дошли сюда - странно, но ок
            except PermissionError:
                pass  # Ожидаемое поведение
            except Exception:
                pass


class TestLogCallsDecoratorAdvanced(unittest.TestCase):
    """Дополнительные тесты декоратора log_calls."""

    def setUp(self):
        Logger._instance = None
        self.logger = Logger()
        self.logger.set_level(Logger.DEBUG)

    def test_decorator_with_methods(self):
        """Декоратор работает с методами классов."""

        class TestClass:
            @log_calls
            def method(self, x):
                return x * 2

        obj = TestClass()
        result = obj.method(5)
        self.assertEqual(result, 10)

        logs = self.logger.get_logs()
        self.assertGreater(len(logs), 0)
        log_text = ' '.join(logs)
        self.assertIn("method", log_text)

    def test_decorator_logs_execution_time(self):
        """Декоратор логирует время выполнения."""

        @log_calls
        def slow_function():
            time.sleep(0.1)
            return 42

        slow_function()
        logs = self.logger.get_logs()
        log_text = ' '.join(logs)

        # Проверяем наличие времени выполнения (в миллисекундах или секундах)
        import re
        pattern = r'\d+\.?\d*\s*(ms|ms\.|seconds?|сек)'
        self.assertTrue(re.search(pattern, log_text, re.IGNORECASE) or
                        "execution time" in log_text.lower())

    def test_decorator_with_exception(self):
        """Декоратор логирует исключения."""

        @log_calls
        def failing_function():
            raise ValueError("Test error")

        with self.assertRaises(ValueError):
            failing_function()

        logs = self.logger.get_logs()
        log_text = ' '.join(logs)
        self.assertIn("error", log_text.lower())
        self.assertIn("Test error", log_text)

    def test_decorator_multiple_calls(self):
        """Декоратор логирует несколько вызовов."""

        @log_calls
        def counter(x):
            return x + 1

        for i in range(5):
            counter(i)

        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 5)

    def test_decorator_with_kwargs(self):
        """Декоратор корректно логирует именованные аргументы."""

        @log_calls
        def func(a, b=10, **kwargs):
            return a + b

        func(5, b=20, extra="test")
        logs = self.logger.get_logs()
        log_text = ' '.join(logs)
        self.assertIn("extra='test'", log_text)


if __name__ == '__main__':
    unittest.main()