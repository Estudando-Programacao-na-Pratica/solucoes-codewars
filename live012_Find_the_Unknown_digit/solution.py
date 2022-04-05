
def separar_numeros(string):
    temp = '-' if string[0] == '-' else ''
    string = string.replace('--', '+') if '--' in string else string[1:] if temp == '-' else string
    op = ''
    resp = []

    for numero in string:
        if numero.isalnum() or numero == '?' or (numero == '-' and op != ''):
            temp += numero
        else:
            resp.append(temp)
            temp = ''
            if not op:
                op = numero
    resp.append(temp)
    resp.append(op)
    return resp


def pode_zero(num):
    for i in range(3):
        primeiro_caracter = num[i][1] if num[i][0] == '-' else num[i][0]
        if (str(num[i]).replace('?', '') == '' or primeiro_caracter == '?') and len(num[i]) > 1:
            return False
    return True

def solve_runes(runes):
    num_separados = separar_numeros(runes)
    
    for num in range(1, 10) if not pode_zero(num_separados) else range(10):
        if str(num) in runes:
            continue

        num1 = int(num_separados[0].replace('?', str(num)))
        num2 = int(num_separados[1].replace('?', str(num)))
        resultado = int(num_separados[2].replace('?', str(num)))
        operacoes = {
            '+': num1 + num2 == resultado,
            '-': num1 - num2 == resultado,
            '*': num1 * num2 == resultado,
        }

        if operacoes[num_separados[-1]]:
            return num
    return -1


