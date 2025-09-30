import re
import datetime


def add_product(collection, name, price, category, date_str):
    if not re.match("^[a-zA-Zа-яА-Я ]+$", name):
        return "Ошибка: некорректный ввод данных"

    try:
        price = float(price)
        if price <= 0:
            return "Ошибка: некорректная стоимость продукта"
    except ValueError:
        return "Ошибка: некорректная стоимость продукта"

    if not re.match("^[a-zA-Zа-яА-Я ]+$", category):
        return "Ошибка: некорректный ввод данных"

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return "Ошибка: некорректный ввод данных"

    product = {"name": name, "price": price, "category": category, "date": date}
    collection.append(product)
    return "Продукт добавлен в коллекцию!"


def all_inf(collection):
    if not collection:
        return ["В коллекции данные не найдены"]
    result = []
    for product in collection:
        formatted_date = product['date'].strftime("%Y-%m-%d")
        result.append("Название: {}, Стоимость: {}, Категория: {}, Дата: {}".format(
            product['name'], product['price'], product['category'], formatted_date))
    return result


def view_date(collection, date_str):
    result = []
    for product in collection:
        if product["date"].strftime("%Y-%m-%d") == date_str:
            formatted_date = product['date'].strftime("%Y-%m-%d")
            result.append("Название: {}, Стоимость: {}, Категория: {}, Дата: {}".format(
                product['name'], product['price'], product['category'], formatted_date))

    if not result:
        return ["Покупки на указанную дату не найдены"]
    return result


def view_category(collection, category):
    result = []
    for product in collection:
        if product["category"].lower() == category.lower():
            formatted_date = product['date'].strftime("%Y-%m-%d")
            result.append("Название: {}, Стоимость: {}, Категория: {}, Дата: {}".format(
                product['name'], product['price'], product['category'], formatted_date))

    if not result:
        return ["Покупок в указанной категории нет"]
    return result


def sort_price(collection, sort_type):
    if sort_type.lower() not in ["incr", "decr"]:
        return ["Некорректный выбор для сортировки"]

    if not collection:
        return ["Данных для сортировки нет"]

    sorted_collection = sorted(collection, key=lambda x: x["price"], reverse=sort_type == "decr")
    result = []
    for product in sorted_collection:
        formatted_date = product['date'].strftime("%Y-%m-%d")
        result.append("Название: {}, Стоимость: {}, Категория: {}, Дата: {}".format(
            product['name'], product['price'], product['category'], formatted_date))
    return result


def delete_record(collection, name):
    for product in collection:
        if product["name"].lower() == name.lower():
            collection.remove(product)
            return "Запись удалена!"
    return "Запись не найдена"


def save_inf(collection, file_name):
    if not collection:
        return "Нет данных для сохранения"

    if not re.match("^[a-zA-Zа-яА-Я]+\\.txt$", file_name):
        return "Некорректное название файла"

    try:
        with open(file_name, "w") as file:
            for product in collection:
                formatted_date = product['date'].strftime("%Y-%m-%d")
                file.write("{},{},{},{}\n".format(product['name'], product['price'], product['category'], formatted_date))
        return "Данные сохранены в файл"
    except OSError:
        return "Ошибка сохранения данных в файл"


# Отдельная CLI-оболочка
def program_interface():
    collection = []

    while True:
        print("Выберите действие:")
        print("1. Добавить продукт в коллекцию")
        print("2. Просмотреть все записи")
        print("3. Просмотреть покупки по дате")
        print("4. Просмотреть покупки по категории")
        print("5. Распределить записи по стоимости")
        print("6. Удалить запись")
        print("7. Сохранить данные в файл")
        print("8. Выход из программы")

        choice = input("Введите номер выбранного действия: ")

        if choice == "1":
            name = input("Введите название продукта: ")
            price = input("Введите стоимость продукта: ")
            category = input("Введите категорию продукта: ")
            date = input("Введите дату в формате гггг-мм-дд: ")
            result = add_product(collection, name, price, category, date)
            print(result)
        elif choice == "2":
            for line in all_inf(collection):
                print(line)
        elif choice == "3":
            date = input("Введите дату в формате гггг-мм-дд: ")
            for line in view_date(collection, date):
                print(line)
        elif choice == "4":
            category = input("Введите категорию: ")
            for line in view_category(collection, category):
                print(line)
        elif choice == "5":
            sort_type = input("Введите 'incr' для сортировки по возрастанию, 'decr' - по убыванию: ")
            for line in sort_price(collection, sort_type):
                print(line)
        elif choice == "6":
            name = input("Введите название продукта для удаления: ")
            print(delete_record(collection, name))
        elif choice == "7":
            file_name = input("Введите название файла для сохранения данных: ")
            print(save_inf(collection, file_name))
        elif choice == "8":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз")


if __name__ == "__main__":
    program_interface()
