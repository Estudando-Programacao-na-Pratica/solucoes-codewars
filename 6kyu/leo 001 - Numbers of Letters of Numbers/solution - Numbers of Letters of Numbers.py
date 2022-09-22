'''
Doctests:
>>> convert_to_english(60)
'sixzero'
>>> convert_to_english(12)
'onetwo'
>>> convert_to_english(999)
'nineninenine'
>>> numbers_of_letters(60)
['sixzero', 'seven', 'five', 'four']
>>> numbers_of_letters(1)
['one', 'three', 'five', 'four']
>>> numbers_of_letters(37)
['threeseven', 'onezero', 'seven', 'five', 'four']
'''

conversor = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def convert_to_english(number):
    return ''.join([conversor[digit] for digit in str(number)])


def numbers_of_letters(number):
    resp = []
    number_in_english = convert_to_english(number)
    while number != len(number_in_english):
        resp.append(number_in_english)
        number = len(number_in_english)
        number_in_english = conversor[str(number)]
    resp.append(number_in_english)
    return resp
