"""
Doctests:
>>> increment_string('foo')
'foo1'
>>> increment_string('foobar23')
'foobar24'
>>> increment_string('foo0042')
'foo0043'
>>> increment_string('foo9')
'foo10'
>>> increment_string('foo099')
'foo100'
"""

def increment_string(strng):
    resp = ''
    cont = 0
    if len(strng) != 0:
        while cont < len(strng):
            if not strng[cont].isnumeric():
                resp += strng[cont]
                cont += 1
                if cont == len(strng):
                    break
            else:
                num = ''
                while strng[cont].isnumeric():
                    num += strng[cont]
                    cont += 1
                    if cont == len(strng):
                        return f'{strng[:len(strng)-len(num)]}{int(num) + 1:0>{len(num)}}'
        return f'{resp}1'
    else:
        return '1'
