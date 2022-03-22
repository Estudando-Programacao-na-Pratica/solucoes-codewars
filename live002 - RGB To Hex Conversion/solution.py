"""
A função deve fazer a conversão de cores RGB para HEX
Testes:
>>> rgb(255, 255, 255)
'FFFFFF'
>>> rgb(255, 255, 300)
'FFFFFF'
>>> rgb(0,0,0)
'000000'
>>> rgb(148, 0, 211)
'9400D3'
"""


def DectoHex(dec):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F"]
    r = []
    hex1 = ''
    if dec == 0:
        return '00'
    while dec > 0:
        r.append(hex[(dec % 16)])
        dec = dec // 16
    for i in range(len(r) - 1, -1, -1):
        hex1 += r[i]
    return str(hex1)


def rgb(r, g, b):
    if r < 0:
        r = 0
    if r > 255:
        r = 255

    if g < 0:
        g = 0
    if g > 255:
        g = 255

    if b < 0:
        b = 0
    if b > 255:
        b = 255

    return f'{DectoHex(r)}{DectoHex(g)}{DectoHex(b)}'
