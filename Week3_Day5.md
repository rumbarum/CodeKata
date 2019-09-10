#  * 문제

재귀를 사용하여 팩토리얼(factorial)을 구하는 함수를 구현해주세요.

팩토리얼이란 1에서부터 n까지의 정수를 모두 곱한것을 말합니다.  

1! = 1

2! = 1 * 2

5! = 1 * 2 * 3 * 4 * 5

# *해답

```python
def factorial(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return n*factorial(n-1)

```

