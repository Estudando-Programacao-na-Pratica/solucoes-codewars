from live012.solution import solve_runes


def test_solve_runes():
    assert solve_runes("1+1=?") == 2
    assert solve_runes("1+1=?") == 2
    assert solve_runes("123*45?=5?088") == 6
    assert solve_runes("-5?*-1=5?") == 0
    assert solve_runes("19--45=5?") == -1
    assert solve_runes("??*??=302?") == 5
    assert solve_runes("?*11=??") == 2
    assert solve_runes("??*1=??") == 2
    assert solve_runes("?8?170-1?6256=7?2?14") == 9
