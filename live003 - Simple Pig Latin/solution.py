"""
Doctests:
>>> pig_it('Pig latin is cool')
'igPay atinlay siay oolcay'
>>> pig_it('Hello world !')
'elloHay orldway !'
"""

import string


def pig_it(text):
    final = []
    for word in text.split():
        if word in string.punctuation:
            final.append(word)
            continue

        final.append(word[1:] + word[0] + 'ay')
    return (' '.join(final))
