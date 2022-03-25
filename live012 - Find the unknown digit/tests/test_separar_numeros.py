from live012.solution import separar_numeros


def test_sep_num():
    assert separar_numeros("123*45?=5?088") == ['123', '45?', '5?088', '*']
    assert separar_numeros('1+1=?') == ['1', '1', '?', '+']
    assert separar_numeros("123*45?=5?088") == ['123', '45?', '5?088', '*']
    assert separar_numeros("??*??=302?") == ['??', '??', '302?', '*']

def test_sep_num_negativos():
    assert separar_numeros("-5?*-1=5?") == ['-5?', '-1', '5?', '*']
    assert separar_numeros("19--45=5?") == ['19', '45', '5?', '+']
    assert separar_numeros("?8?170-1?6256=7?2?14") == ['?8?170', '1?6256', '7?2?14', '-']
