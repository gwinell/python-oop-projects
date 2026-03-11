import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.data_structures import Stack, Queue


class TestStackBasic(unittest.TestCase):
    """Базовые тесты Stack."""

    def test_create_empty(self):
        """Создание пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_create_from_iterable(self):
        """Создание стека из iterable."""
        stack = Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)

    def test_push(self):
        """push() добавляет элемент."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)

    def test_push_multiple(self):
        """Несколько push()."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)

    def test_pop(self):
        """pop() возвращает и удаляет верхний элемент."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.pop()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 1)

    def test_pop_order_lifo(self):
        """pop() соблюдает LIFO."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_pop_empty_raises(self):
        """pop() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertIn("empty", str(context.exception).lower())

    def test_peek(self):
        """peek() возвращает верхний элемент без удаления."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        result = stack.peek()
        self.assertEqual(result, 2)
        self.assertEqual(len(stack), 2)  # Длина не изменилась

    def test_peek_empty_raises(self):
        """peek() на пустом стеке вызывает IndexError."""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_is_empty_true(self):
        """is_empty() возвращает True для пустого стека."""
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_is_empty_false(self):
        """is_empty() возвращает False для непустого стека."""
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())


class TestStackMagicMethods(unittest.TestCase):
    """Тесты магических методов Stack."""

    def test_len_empty(self):
        """len() для пустого стека."""
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def test_len_with_items(self):
        """len() для непустого стека."""
        stack = Stack([1, 2, 3, 4, 5])
        self.assertEqual(len(stack), 5)

    def test_bool_empty(self):
        """bool() для пустого стека — False."""
        stack = Stack()
        self.assertFalse(bool(stack))

    def test_bool_not_empty(self):
        """bool() для непустого стека — True."""
        stack = Stack([1])
        self.assertTrue(bool(stack))

    def test_if_statement(self):
        """Стек работает в if."""
        stack = Stack()
        if stack:
            self.fail("Пустой стек не должен быть truthy")

        stack.push(1)
        if not stack:
            self.fail("Непустой стек должен быть truthy")

    def test_iter(self):
        """Итерация по стеку (от вершины к основанию)."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        items = list(stack)
        self.assertEqual(items, [3, 2, 1])

    def test_iter_for_loop(self):
        """Стек работает в for."""
        stack = Stack([1, 2, 3])
        result = []
        for item in stack:
            result.append(item)
        self.assertEqual(len(result), 3)


class TestQueueBasic(unittest.TestCase):
    """Базовые тесты Queue."""

    def test_create_empty(self):
        """Создание пустой очереди."""
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_create_from_iterable(self):
        """Создание очереди из iterable."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)

    def test_enqueue(self):
        """enqueue() добавляет элемент."""
        queue = Queue()
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_dequeue(self):
        """dequeue() возвращает и удаляет первый элемент."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        result = queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 1)

    def test_dequeue_order_fifo(self):
        """dequeue() соблюдает FIFO."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_dequeue_empty_raises(self):
        """dequeue() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError) as context:
            queue.dequeue()
        self.assertIn("empty", str(context.exception).lower())

    def test_front(self):
        """front() возвращает первый элемент без удаления."""
        queue = Queue([1, 2, 3])
        result = queue.front()
        self.assertEqual(result, 1)
        self.assertEqual(len(queue), 3)

    def test_front_empty_raises(self):
        """front() на пустой очереди вызывает IndexError."""
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.front()


class TestQueueMagicMethods(unittest.TestCase):
    """Тесты магических методов Queue."""

    def test_len(self):
        """len() для очереди."""
        queue = Queue([1, 2, 3])
        self.assertEqual(len(queue), 3)

    def test_bool_empty(self):
        """bool() для пустой очереди."""
        queue = Queue()
        self.assertFalse(bool(queue))

    def test_bool_not_empty(self):
        """bool() для непустой очереди."""
        queue = Queue([1])
        self.assertTrue(bool(queue))

    def test_iter(self):
        """Итерация по очереди (от начала к концу)."""
        queue = Queue([1, 2, 3])
        items = list(queue)
        self.assertEqual(items, [1, 2, 3])


class TestStackAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Stack."""

    def test_clear(self):
        """clear() очищает стек."""
        stack = Stack([1, 2, 3])
        stack.clear()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

    def test_contains(self):
        """contains() проверяет наличие элемента."""
        stack = Stack([1, 2, 3])
        self.assertTrue(stack.contains(2))
        self.assertFalse(stack.contains(5))

    def test_in_operator(self):
        """Оператор in работает."""
        stack = Stack([1, 2, 3])
        self.assertIn(2, stack)
        self.assertNotIn(5, stack)

    def test_maxsize(self):
        """Ограничение размера стека."""
        stack = Stack(maxsize=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(OverflowError):
            stack.push(4)


class TestQueueAdditional(unittest.TestCase):
    """Тесты дополнительных заданий для Queue."""

    def test_clear(self):
        """clear() очищает очередь."""
        queue = Queue([1, 2, 3])
        queue.clear()
        self.assertTrue(queue.is_empty())

    def test_contains(self):
        """contains() проверяет наличие элемента."""
        queue = Queue([1, 2, 3])
        self.assertTrue(queue.contains(2))
        self.assertFalse(queue.contains(5))

    def test_in_operator(self):
        """Оператор in работает."""
        queue = Queue([1, 2, 3])
        self.assertIn(2, queue)
        self.assertNotIn(5, queue)

    def test_maxsize(self):
        """Ограничение размера очереди."""
        queue = Queue(maxsize=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        with self.assertRaises(OverflowError):
            queue.enqueue(4)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestStackBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestStackMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueMagicMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestStackAdditional))
    suite.addTests(loader.loadTestsFromTestCase(TestQueueAdditional))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)