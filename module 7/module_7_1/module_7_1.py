


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.weight, self.category)


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()

        return products

    def add(self, *products):

        for product in products:
            if product.__str__() not in self.get_products():
                with open(self.__file_name, 'a') as f:
                    f.write(product.__str__() + '\n')

            else:
                print(f'Продукт {product.__str__()} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
