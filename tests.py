import unittest
import coverage
import datetime
from product_list import add_product, view_date, view_category, sort_price, delete_record

cov = coverage.Coverage(source=["product_list"])
cov.start()

class Test_Products(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"name": "Хлеб", "price": 46.0, "category": "Продукты", "date": datetime.datetime(2025, 9, 30)},
            {"name": "Сыр", "price": 139.0, "category": "Продукты", "date": datetime.datetime(2025, 9, 29)},
            {"name": "Шампунь", "price": 471.0, "category": "Гигиена", "date": datetime.datetime(2025, 9, 28)},
        ]

    def test_add_success(self):
        collection = []
        result = add_product(collection, "Масло", "120", "Продукты", "2025-09-30")
        self.assertEqual(result, "Продукт добавлен в коллекцию!")
        self.assertTrue(len(collection) > 0)

    def test_add_wrong_name(self):
        collection = []
        result = add_product(collection, "123", "100", "Продукты", "2025-09-30")
        self.assertEqual(result, "Ошибка: некорректный ввод данных")
        self.assertEqual(collection, [])

    def test_view_date_found(self):
        results = view_date(self.products, "2025-09-30")
        self.assertTrue("Хлеб" in results[0])

    def test_view_category_not_found(self):
        results = view_category(self.products, "Одежда")
        self.assertEqual(results, ["Покупок в указанной категории нет"])

    def test_sort_price(self):
        results = sort_price(self.products, "decr")
        self.assertTrue("Шампунь", results[0])

    def test_sort_invalid_sort_key(self):
        results = sort_price(self.products, "xyz")
        self.assertEqual(results, ["Некорректный выбор для сортировки"])

    def test_delete_record(self):
        result = delete_record(self.products, "Хлеб")
        self.assertEqual(result, "Запись удалена!")
        self.assertTrue(len(self.products) == 2)

if __name__ == "__main__":
    unittest.main(exit=False)
    cov.stop()
    cov.save()
    print("\nПокрытие кода:")
    cov.report()
