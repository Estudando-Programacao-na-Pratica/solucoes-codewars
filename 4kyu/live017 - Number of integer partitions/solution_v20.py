def partitions(n):
    return partitions_recursion(n1=n, n2=n)


def partitions_recursion(n1, n2):
    if n2 == 1:
        return 1

    if n1 == n2:
        return partitions_recursion(n1, n2-1) + 1

    if n1 != n2:
        return partitions_recursion(n2, n2)


print(partitions(4))