# [Kata: Calculating with Functions](https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39)

**Rank:** 5 kyu  
**Solution date:** 02/09/2021

This time we want to write calculations using functions and get the results. Let's have a look at some examples:
```python
>>> seven(times(five()))
35
>>> four(plus(nine()))
13
>>> eight(minus(three()))
5
>>> six(divided_by(two()))
3
```
**Requirements:**
- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Division should be integer division. For example `eight(divided_by(three()))` should return 2, not 2.666666...
