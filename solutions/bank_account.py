class BankAccount:

    def __init__(self, owner, _balance=0):
        if not isinstance(owner, (str)):
            raise TypeError("Может быть только строкой.")
        if _balance < 0:
            raise ValueError("Баланс может быть только положительным")
        if not any(c.isalpha() for c in owner):
            raise ValueError("Имя должно содержать буквы.")

        self.owner = owner
        self._balance = _balance
        self.transaction_history = [{'type': 'initial',
                                     'amount': 0,
                                     'balance': _balance}]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Пополнение только на положительную сумму")
        self._balance += amount
        self.transaction_history.append({'type': 'deposit',
                                         'amount': amount,
                                         'balance': self._balance})

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Только положительное число на снятие")
        if (self._balance - amount) < 0:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self.transaction_history.append({'type': 'withdraw',
                                         'amount': amount,
                                         'balance': self._balance})

    def transfer(self, other_account, amount):
        if 'BankAccount' not in str(type(other_account)):
            raise TypeError("Это не банковский счет")
        if amount <= 0:
            raise ValueError("Число не может быть отрицательным")
        if (self._balance - amount) < 0:
            raise ValueError("Недостаточно средств")
        if other_account == self:
            raise ValueError("Нельзя выполнить перевод самому себе.")
        other_account._balance += amount
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self.transaction_history

    def apply_interest(self, rate):
        if not isinstance(rate, (float, int)):
            raise TypeError("Неверный тип данных.")
        if rate < 0:
            raise ValueError("Процент может быть только положительным.")
        self._balance += self._balance * rate

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

