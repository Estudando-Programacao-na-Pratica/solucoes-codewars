def separar_numeros(string):
    temp = '-' if string[0] == '-' else ''
    op = ''
    resp = []

    if '--' in string:
        string = string.replace('--', '+')

    if temp == '-':
        string = string[1:]

    for numero in string:
        # Acionado a condição final para lidar com o caso de -5*-5=5?
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
