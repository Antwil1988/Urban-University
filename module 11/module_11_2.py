import pprint
import sys


def introspection_info(obj):

    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')],
        'module': sys.modules.get(getattr(obj, '__module__', '__main__'), '__main__'),
    }

    # Дополнительная информация для некоторых типов объектов
    if isinstance(obj, type):
        info['bases'] = [base.__name__ for base in obj.__bases__]
    elif hasattr(obj, '__dict__'):
        info['instance_variables'] = list(obj.__dict__.keys())

    return info

# Создание собственного класса для демонстрации


class MyClass:
    def __init__(self, value):
        self.value = value


    def my_method(self):
        pass


# Создание экземпляра класса
obj = MyClass(42)

# Вызов функции introspection_info
info = introspection_info(obj)

# Вывод информации о объекте
pprint.pprint(info)