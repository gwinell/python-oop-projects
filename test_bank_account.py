import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.bank_account import BankAccount


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
        account.deposit(500)  # 1500
        account.withdraw(200)  # 1300
        account.deposit(100)  # 1400
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