# функция, проверяющая соответствие произвольной строки формату json
import json


def is_correct_json(string):
    try:
        json_string = json.loads(string)
        if json_string:
            return True
    except json.decoder.JSONDecodeError:
        return False


# TEST_1:
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))

# TEST_2:
print(is_correct_json('number = 17'))

# TEST_3:
data = '''{
        "beegeek": 2018,
        "stepik": 2013
       }'''

print(is_correct_json(data))

# TEST_4:
data = '''{
        "beegeek": 2018,
        ("Timur", "Guev"): 29,
        ("Artur", "Harisov"): 20,
        "stepik": 2013
       }'''

print(is_correct_json(data))

# TEST_5:
print(is_correct_json('99999'))

# TEST_6:
data = '''{
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Artur', 'Harisov'): 20,
        'stepik': 2013
       }'''

print(is_correct_json(data))

# TEST_7:
data = '''{
        'beegeek': 2018,
        'stepik': 2013
       }'''

print(is_correct_json(data))

# TEST_8:
print(is_correct_json('"beegeek"'))

# TEST_9:
print(is_correct_json('beegeek'))

# TEST_10:
print(is_correct_json('["beegeek", 1, 2, 3]'))
