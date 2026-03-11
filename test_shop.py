import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solutions.shop import Product, CartItem, ShoppingCart, Order, Store


class TestProduct(unittest.TestCase):
    """Тесты класса Product."""

    def test_creation(self):
        """Product создаётся с правильными атрибутами."""
        product = Product("P001", "Ноутбук", 50000, 10)
        self.assertEqual(product.product_id, "P001")
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.quantity, 10)

    def test_negative_price_raises(self):
        """Отрицательная цена вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", -100, 10)

    def test_zero_price_raises(self):
        """Нулевая цена вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", 0, 10)

    def test_negative_quantity_raises(self):
        """Отрицательное количество вызывает ValueError."""
        with self.assertRaises(ValueError):
            Product("P001", "Товар", 100, -5)

    def test_is_available_true(self):
        """is_available() возвращает True когда товар есть."""
        product = Product("P001", "Товар", 100, 10)
        self.assertTrue(product.is_available())
        self.assertTrue(product.is_available(5))
        self.assertTrue(product.is_available(10))

    def test_is_available_false(self):
        """is_available() возвращает False когда товара недостаточно."""
        product = Product("P001", "Товар", 100, 5)
        self.assertFalse(product.is_available(10))

    def test_is_available_zero_stock(self):
        """is_available() для товара с нулевым остатком."""
        product = Product("P001", "Товар", 100, 0)
        self.assertFalse(product.is_available())

    def test_reduce_stock(self):
        """reduce_stock() уменьшает количество."""
        product = Product("P001", "Товар", 100, 10)
        product.reduce_stock(3)
        self.assertEqual(product.quantity, 7)

    def test_reduce_stock_insufficient_raises(self):
        """reduce_stock() с недостаточным количеством вызывает ValueError."""
        product = Product("P001", "Товар", 100, 5)
        with self.assertRaises(ValueError):
            product.reduce_stock(10)

    def test_restock(self):
        """restock() увеличивает количество."""
        product = Product("P001", "Товар", 100, 10)
        product.restock(5)
        self.assertEqual(product.quantity, 15)

    def test_str(self):
        """__str__() возвращает информацию о товаре."""
        product = Product("P001", "Ноутбук", 50000, 10)
        s = str(product)
        self.assertIn("Ноутбук", s)
        self.assertIn("50000", s)


class TestCartItem(unittest.TestCase):
    """Тесты класса CartItem."""

    def setUp(self):
        self.product = Product("P001", "Товар", 1000, 10)

    def test_creation(self):
        """CartItem создаётся с product и quantity."""
        item = CartItem(self.product, 3)
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 3)

    def test_get_total(self):
        """get_total() возвращает стоимость."""
        item = CartItem(self.product, 3)
        self.assertEqual(item.get_total(), 3000)

    def test_update_quantity(self):
        """update_quantity() изменяет количество."""
        item = CartItem(self.product, 3)
        item.update_quantity(5)
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.get_total(), 5000)

    def test_update_quantity_zero_raises(self):
        """update_quantity(0) вызывает ValueError."""
        item = CartItem(self.product, 3)
        with self.assertRaises(ValueError):
            item.update_quantity(0)

    def test_update_quantity_negative_raises(self):
        """Отрицательное количество вызывает ValueError."""
        item = CartItem(self.product, 3)
        with self.assertRaises(ValueError):
            item.update_quantity(-1)


class TestShoppingCart(unittest.TestCase):
    """Тесты класса ShoppingCart."""

    def setUp(self):
        self.cart = ShoppingCart()
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)

    def test_empty_cart(self):
        """Новая корзина пуста."""
        self.assertEqual(len(self.cart), 0)
        self.assertEqual(self.cart.get_total(), 0)

    def test_add_item(self):
        """add_item() добавляет товар."""
        self.cart.add_item(self.laptop, 2)
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart.get_total(), 100000)

    def test_add_item_multiple_products(self):
        """Добавление нескольких товаров."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.assertEqual(len(self.cart), 2)
        self.assertEqual(self.cart.get_total(), 104500)

    def test_add_item_same_product_increases_quantity(self):
        """Повторное добавление увеличивает количество."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.laptop, 3)
        self.assertEqual(len(self.cart), 1)
        items = self.cart.get_items()
        self.assertEqual(items[0].quantity, 5)

    def test_remove_item(self):
        """remove_item() удаляет товар."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.cart.remove_item("P001")
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart.get_total(), 4500)

    def test_remove_nonexistent_raises(self):
        """remove_item() для несуществующего товара вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.cart.remove_item("NONEXISTENT")

    def test_update_item_quantity(self):
        """update_item_quantity() изменяет количество."""
        self.cart.add_item(self.laptop, 2)
        self.cart.update_item_quantity("P001", 5)
        self.assertEqual(self.cart.get_total(), 250000)

    def test_get_items(self):
        """get_items() возвращает список CartItem."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        items = self.cart.get_items()
        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], CartItem)

    def test_clear(self):
        """clear() очищает корзину."""
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)
        self.cart.clear()
        self.assertEqual(len(self.cart), 0)
        self.assertEqual(self.cart.get_total(), 0)


class TestOrder(unittest.TestCase):
    """Тесты класса Order."""

    def setUp(self):
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)
        self.cart = ShoppingCart()
        self.cart.add_item(self.laptop, 2)
        self.cart.add_item(self.mouse, 3)

    def test_creation(self):
        """Order создаётся с правильными атрибутами."""
        order = Order("O001", self.cart, "Иван Петров")
        self.assertEqual(order.order_id, "O001")
        self.assertEqual(order.customer_name, "Иван Петров")

    def test_initial_status_pending(self):
        """Начальный статус — PENDING."""
        order = Order("O001", self.cart, "Иван")
        self.assertEqual(order.status, Order.PENDING)

    def test_get_total(self):
        """get_total() возвращает сумму заказа."""
        order = Order("O001", self.cart, "Иван")
        self.assertEqual(order.get_total(), 104500)

    def test_confirm(self):
        """confirm() подтверждает заказ и списывает товары."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        self.assertEqual(order.status, Order.CONFIRMED)
        self.assertEqual(self.laptop.quantity, 8)  # 10 - 2
        self.assertEqual(self.mouse.quantity, 47)  # 50 - 3

    def test_confirm_insufficient_stock_raises(self):
        """confirm() при недостатке товара вызывает ValueError."""
        self.laptop.quantity = 1  # Меньше чем в корзине (2)
        order = Order("O001", self.cart, "Иван")
        with self.assertRaises(ValueError):
            order.confirm()

    def test_ship(self):
        """ship() отправляет подтверждённый заказ."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        self.assertEqual(order.status, Order.SHIPPED)

    def test_ship_pending_raises(self):
        """ship() для неподтверждённого заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        with self.assertRaises(ValueError):
            order.ship()

    def test_deliver(self):
        """deliver() доставляет отправленный заказ."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        order.deliver()
        self.assertEqual(order.status, Order.DELIVERED)

    def test_deliver_not_shipped_raises(self):
        """deliver() для неотправленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        with self.assertRaises(ValueError):
            order.deliver()

    def test_cancel_pending(self):
        """cancel() отменяет неподтверждённый заказ."""
        order = Order("O001", self.cart, "Иван")
        order.cancel()
        self.assertEqual(order.status, Order.CANCELLED)

    def test_cancel_confirmed_returns_stock(self):
        """cancel() возвращает товары на склад."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        self.assertEqual(self.laptop.quantity, 8)
        order.cancel()
        self.assertEqual(order.status, Order.CANCELLED)
        self.assertEqual(self.laptop.quantity, 10)  # Возвращены

    def test_cancel_shipped_raises(self):
        """cancel() для отправленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        with self.assertRaises(ValueError):
            order.cancel()

    def test_cancel_delivered_raises(self):
        """cancel() для доставленного заказа вызывает ValueError."""
        order = Order("O001", self.cart, "Иван")
        order.confirm()
        order.ship()
        order.deliver()
        with self.assertRaises(ValueError):
            order.cancel()


class TestStore(unittest.TestCase):
    """Тесты класса Store."""

    def setUp(self):
        self.store = Store("TechShop")
        self.laptop = Product("P001", "Ноутбук", 50000, 10)
        self.mouse = Product("P002", "Мышь", 1500, 50)

    def test_creation(self):
        """Store создаётся с именем."""
        self.assertEqual(self.store.name, "TechShop")

    def test_add_product(self):
        """add_product() добавляет товар."""
        self.store.add_product(self.laptop)
        product = self.store.get_product("P001")
        self.assertEqual(product, self.laptop)

    def test_add_duplicate_product_raises(self):
        """Добавление товара с существующим ID вызывает ValueError."""
        self.store.add_product(self.laptop)
        duplicate = Product("P001", "Другой", 100, 5)
        with self.assertRaises(ValueError):
            self.store.add_product(duplicate)

    def test_get_product(self):
        """get_product() возвращает товар по ID."""
        self.store.add_product(self.laptop)
        self.store.add_product(self.mouse)
        product = self.store.get_product("P002")
        self.assertEqual(product.name, "Мышь")

    def test_get_product_nonexistent_raises(self):
        """get_product() для несуществующего товара вызывает KeyError."""
        with self.assertRaises(KeyError):
            self.store.get_product("NONEXISTENT")

    def test_get_available_products(self):
        """get_available_products() возвращает товары в наличии."""
        self.laptop.quantity = 0
        self.store.add_product(self.laptop)
        self.store.add_product(self.mouse)
        available = self.store.get_available_products()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].name, "Мышь")

    def test_create_order(self):
        """create_order() создаёт заказ."""
        self.store.add_product(self.laptop)
        cart = ShoppingCart()
        cart.add_item(self.laptop, 2)
        order = self.store.create_order(cart, "Иван")
        self.assertIsInstance(order, Order)

    def test_get_order(self):
        """get_order() возвращает заказ по ID."""
        self.store.add_product(self.laptop)
        cart = ShoppingCart()
        cart.add_item(self.laptop, 1)
        order = self.store.create_order(cart, "Иван")
        found = self.store.get_order(order.order_id)
        self.assertEqual(found, order)


class TestDiscount(unittest.TestCase):
    """Тесты дополнительного задания: скидки."""

    def setUp(self):
        self.cart = ShoppingCart()
        self.product = Product("P001", "Товар", 1000, 10)
        self.cart.add_item(self.product, 5)  # 5000

    def test_percentage_discount(self):
        """Процентная скидка."""
        from shop import Discount
        discount = Discount(percentage=10)  # 10%
        self.cart.apply_discount(discount)
        self.assertEqual(self.cart.get_total(), 4500)

    def test_fixed_discount(self):
        """Фиксированная скидка."""
        from shop import Discount
        discount = Discount(fixed=500)
        self.cart.apply_discount(discount)
        self.assertEqual(self.cart.get_total(), 4500)

    def test_discount_not_below_zero(self):
        """Скидка не делает сумму отрицательной."""
        from shop import Discount
        discount = Discount(fixed=10000)
        self.cart.apply_discount(discount)
        self.assertGreaterEqual(self.cart.get_total(), 0)


class TestOrderHistory(unittest.TestCase):
    """Тесты дополнительного задания: история заказов."""

    def test_get_order_history(self):
        """get_order_history() возвращает заказы клиента."""
        store = Store("Test")
        product = Product("P001", "Товар", 100, 100)
        store.add_product(product)

        cart1 = ShoppingCart()
        cart1.add_item(product, 1)
        order1 = store.create_order(cart1, "Иван")

        cart2 = ShoppingCart()
        cart2.add_item(product, 2)
        order2 = store.create_order(cart2, "Иван")

        cart3 = ShoppingCart()
        cart3.add_item(product, 1)
        order3 = store.create_order(cart3, "Пётр")

        ivan_orders = store.get_order_history("Иван")
        self.assertEqual(len(ivan_orders), 2)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestProduct))
    suite.addTests(loader.loadTestsFromTestCase(TestCartItem))
    suite.addTests(loader.loadTestsFromTestCase(TestShoppingCart))
    suite.addTests(loader.loadTestsFromTestCase(TestOrder))
    suite.addTests(loader.loadTestsFromTestCase(TestStore))

    # Дополнительные тесты
    try:
        from shop import Discount

        suite.addTests(loader.loadTestsFromTestCase(TestDiscount))
    except ImportError:
        print("Discount не реализован")

    suite.addTests(loader.loadTestsFromTestCase(TestOrderHistory))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print(f"ИТОГО: {result.testsRun} тестов")
    print(f"  Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Провалено: {len(result.failures)}")
    print(f"  Ошибок: {len(result.errors)}")
    print("=" * 70)