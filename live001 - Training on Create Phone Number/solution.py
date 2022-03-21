'''
A função recebe uma lista (ex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) e retorna os números dessa lista formatados
(ex: "(123) 456-7890")
Sendo assim:
>>> create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
'(123) 456-7890'
>>> create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
'(111) 111-1111'
>>> create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
'(123) 456-7890'
>>> create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
'(023) 056-0890'
>>> create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
'(000) 000-0000'
'''


def create_phone_number(n):
    num = "("
    num += str(n[0])
    num += str(n[1])
    num += str(n[2])
    num += ") "

    num += str(n[3])
    num += str(n[4])
    num += str(n[5])
    num += "-"

    num += str(n[6])
    num += str(n[7])
    num += str(n[8])
    num += str(n[9])

    return num
