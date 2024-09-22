def test_function():
    def inner_function():
        print('Я в области видимости inner_function')

    inner_function()


test_function()
# При попытке вызвать inner_function()
# вне test_function выдает ошибку
