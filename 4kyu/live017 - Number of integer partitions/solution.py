"""
Doctests
# Teste resposta
>>> partitions(1)
1
>>> partitions(2)
2
>>> partitions(5)
7
>>> partitions(10)
42
>>> partitions(25)
1958

Referência de estudo para chegar na solução: https://edisciplinas.usp.br/mod/assign/view.php?id=3466279

p(1 1) = 1

p(2 1) => p(2-1 1) => p(1 1) => 1
p(2 2) => p(2 1)  2 => 2
p(2) = 2

p(3 1) => p(3-1 1) => p(2 1) => p(2-1 1) => p(1 1) => 1
p(3 2) => p(3 1) 2 1 => 2
p(3 3) => p(3 2) 3 => 3
p(3) = 3

p(4 1) => p(4-1, 1) => p(3, 1) => p(3-1 1) => p(2 1) => p(2-1 1) => p(1 1) => +1
p(4 2) => p(4-2, 2) => p(2,2)= 2 => 1 + 2 = 3
p(4 3) => p(4-3, 3) = 1 => 4
p(4 4) => 5

p(5 1) => p(4 1) => p(4-1, 1) => p(3, 1) => p(3-1 1) => p(2 1) => p(2-1 1) => p(1 1) => +1
p(5 2) => p(3 2) => 3
p(5 3) => p(2 3) => 5
p(5 4) => p(1 4) => 6
p(5 5) => p(0 5) => 7

p(6 1) => p(5 1) => p(4 1) => p(4-1, 1) => p(3, 1) => p(3-1 1) => p(2 1) => p(2-1 1) => p(1 1) => +1
p(6 2) => p(4 2) = 3 => 4
p(6 3) => p(3 3) => 7
p(6 4) => p(2 4) => 9
p(6 5) => p(1 5) => 10
p(6 6) => p(0 6) => 11
"""


def partition_recursion(n1, n2):
    if n2 == 1:
        return 1

    if n1 == n2:
        return partition_recursion(n1, n2-1) + 1

    if n1 - n2 < n2:
        return partition_recursion(n1, n2-1) + partition_recursion(n1-n2, n1-n2)

    if n1 - n2 >= n2:
        return partition_recursion(n1, n2-1) + partition_recursion(n1-n2, n2)


def partitions(n):
    return partition_recursion(n1=n, n2=n)


