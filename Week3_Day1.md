#  문제

두 개의 input에는 복소수(complex number)가 string 으로 주어집니다.

복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.



input으로 받은 두 수를 곱해서 반환해주세요.

반환하는 표현도 복소수 형태의 string 이어야 합니다.



복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.



** 제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.*



**예제 1:**

```

Input: "1+1i", "1+1i"
Output: "0+2i"
설명: 
(1 + i) * (1 + i) = 1 + i + i + i^2 = 2i 
2i를 복소수 형태로 바꾸면 0+2i.

```

**예제 2:**

```

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
설명: 
(1 - i) * (1 - i) = 1 - i - i + i^2 = -2i, 
-2i를 복소수 형태로 바꾸면 0+-2i.

```

**예제 3:**

```

Input: "1+3i", "1+-2i"
Output: "7+1i"
설명: 
(1 + 3i) * (1 - 2i) = 1 - 2i + 3i -6(i^2) = 1 + i + 6, 
7+i를 복소수 형태로 바꾸면 7+1i.

```

###### 가정

input은 항상 a+bi 형태입니다.

output도 a+bi 형태로 나와야 합니다.

# *해답

계산할 값들을 확인(c, d, e, f ), 계산할 값들 특정 짓기(a1, a2, b1, b2), 계산하고 리턴에 반영 (r1, r2)

```python
def complexNumberMultiply(a, b):
  """
  :type a: c+di
  :type b: e+fi
  :rtype: str
  """
  a1 = int(a[0:a.index('+')]) 
  a2 = int(a[a.index('+')+1:a.index('i')])
  b1 = int(b[0:b.index('+')]) 
  b2 = int(b[b.index('+')+1:b.index('i')])
  r1 = a1*b1+a2*b2*(-1)
  r2 = a1*b2+a2*b1
  return f"{r1}+{r2}i"
```

