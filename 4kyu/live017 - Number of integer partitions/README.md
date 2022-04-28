# [Number of integer partitions](https://www.codewars.com/kata/546d5028ddbcbd4b8d001254)

**Rank:** 4 kyu  
**Solution date:** 

An integer partition of `n` is a weakly decreasing list of positive integers which sum to `n`.

For example, there are 7 integer partitions of 5:

`[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]`


Write a function which returns the number of integer partitions of `n`. 

The function should be able to find the number of
integer partitions of n for n at least as large as 100.

```python
# Teste resposta
>>> partitions(1)
1
>>> partitions(5)
7
>>> partitions(10)
42
>>> partitions(25)
1958
```

