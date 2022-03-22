"""
A função deve retornar o elemento da lista que apareceu um número ímpar de vezes.
Testes:
>>> find_it([7])  # Should return 7, because it occurs 1 time (which is odd).
7
>>> find_it([0])  # Should return 0, because it occurs 1 time (which is odd).
0
>>> find_it([1,1,2]) # Should return 2, because it occurs 1 time (which is odd).
2
>>> find_it([0,1,0,1,0])  # Should return 0, because it occurs 3 times (which is odd).
0
>>> find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])  # Should return 4, because it appears 1 time (which is odd).
4
"""
def find_it(seq):
    for x in set(seq):
        if seq.count(x)%2:
            return x
