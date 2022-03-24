"""
# Testes separar números:
>>> separar_numeros('1+1=?')
['1', '1', '?', '+']
>>> separar_numeros("123*45?=5?088")
['123', '45?', '5?088', '*']
>>> separar_numeros("??*??=302?")
['??', '??', '302?', '*']
>>> separar_numeros("-5?*-1=5?")
['-5?', '-1', '5?', '*']
>>> separar_numeros("19--45=5?")
['19', '45', '5?', '+']
>>> separar_numeros("?8?170-1?6256=7?2?14")
['?8?170', '1?6256', '7?2?14', '-']

# Teste resposta
>>> solve_runes("1+1=?")
2
>>> solve_runes("123*45?=5?088")
6
>>> solve_runes("-5?*-1=5?")
0
>>> solve_runes("19--45=5?")
-1
>>> solve_runes("??*??=302?")
5
>>> solve_runes("?*11=??")
2
>>> solve_runes("??*1=??")
2
>>> solve_runes("?8?170-1?6256=7?2?14")
9
"""


def separar_numeros(string):
    temp = '-' if string[0] == '-' else ''
    op = ''
    resp = []

    if '--' in string:
        string = string.replace('--', '+')

    if temp == '-':
        string = string[1:]

    for numero in string:
        if numero.isalnum() or numero == '?':
            temp += numero
        else:
            resp.append(temp)
            temp = ''
            if not op:
                op = numero

    resp.append(temp)
    resp.append(op)

    return resp


def solve_runes(runes):
    num_separados = separar_numeros(runes)

    for num in range(10):
        num1 = int(num_separados[0].replace('?', str(num)))
        num2 = int(num_separados[1].replace('?', str(num)))
        resultado = int(num_separados[2].replace('?', str(num)))

        if num == 0:
            if str(num_separados[0]).replace('?', '') == '' and len(num_separados[0]) > 1:
                continue

            if str(num_separados[1]).replace('?', '') == '' and len(num_separados[1]) > 1:
                continue

            if str(num_separados[2]).replace('?', '') == '' and len(num_separados[2]) > 1:
                continue

        if str(num) in runes:
            continue

        if num_separados[-1] == '+' and num1 + num2 == resultado:
            return num

        if num_separados[-1] == '-' and num1 - num2 == resultado:
            return num

        if num_separados[-1] == '*' and num1 * num2 == resultado:
            return num
    return -1
