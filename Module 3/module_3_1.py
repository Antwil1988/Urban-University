calls = 0
def count_calls():
    global calls
    calls +=  1

def string_info(string):
    count_calls()
    tuple_def = (len(string), string.lower(), string.upper())
    print(tuple_def)
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            True_False = "True"
            break
        else:
            True_False = "False"
    print(True_False)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print ("Количество вызовов:", calls)