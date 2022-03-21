'''
A função deve receber uma string como input e retornar a string com os caracteres das palvras que tem
mais de 5 letras ao contrário.
Testes:
>>> spin_words('Welcome')
'emocleW'
>>> spin_words("to")
'to'
>>> spin_words("CodeWars")
'sraWedoC'
>>> spin_words("Hey fellow warriors")
'Hey wollef sroirraw'
>>> spin_words("This sentence is a sentence")
'This ecnetnes is a ecnetnes'
'''

def spin_words(sentence):
    sentence = sentence.split()
    list = []

    for word in sentence:
        if len(word) >= 5:
            list.append(word[::-1])
        else:
            list.append(word)
    return ' '.join(list)
