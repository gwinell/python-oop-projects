class Counter:
    start = 0
    def __init__(self, start=0):
        self.start = start
        self.value = start

    def __str__(self):
        return f"Counter: {self.value}"

    def increment(self):
        self.value += 1

    def increment_by(self, n):
        self.value += n

    def decrement(self):
        if self.value > 0:
            self.value -= 1
        else:
            self.value = 0

    def reset(self):
        self.value = self.start

    def get_value(self):
        return self.value

c = Counter(start=5)
c.increment()
c.increment()
print(c.get_value())  # 7
c.reset()
print(c.get_value())  # 5 (вернулись к начальному)

print(c)