"""
Doctests:
>>> likes([])
'no one likes this'
>>> likes(["Peter"])
'Peter likes this'
>>> likes(["Jacob", "Alex"])
'Jacob and Alex like this'
>>> likes(["Max", "John", "Mark"])
'Max, John and Mark like this'
>>> likes(["Alex", "Jacob", "Mark", "Max"])
'Alex, Jacob and 2 others like this'
"""


# NOSSA SOLUÇÃO
def likes(names):
    tamanho = len(names)
    if tamanho == 0:
        return 'no one likes this'
    elif tamanho == 1:
        return f'{names[0]} likes this'
    elif tamanho == 2:
        return f'{names[0]} and {names[1]} like this'
    elif tamanho == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {tamanho - 2} others like this'
