# * 문제

양수 N을 이진법으로 바꿨을 때, 연속으로 이어지는 0 중에서 가장 큰 값을 return해 주세요.

\* 이어지는 0은 1과 1사이에 있는 것을 의미합니다.

\* 이런 것을 binary gap 이라고 합니다.

```
input: 9
output: 2
설명: 9의 이진수는 1001 입니다. 
1과 1사이에 있는 0은 2 이므로, 2를 return

```

```
input: 529
output: 4
설명: 529의 이진수는 1000010001 입니다. 
1과 1사이에 있는 연속된 0의 수는 4와 3입니다.
이 중 큰 값은 4이므로 4를 return
```

```
input: 20
output: 1
설명: 20의 이진수는 10100 입니다. 
1과 1사이에 있는 연속된 0의 수는 1 뿐입니다.
(뒤에 있는 0은 1사이에 있는 것이 아니므로)
```

```
input: 15
output: 0
설명: 15의 이진수는 1111 입니다. 
1과 1사이에 있는 0이 없으므로 0을 return
```

```
input: 32
output: 0
설명: 32의 이진수는 100000 입니다. 
1과 1사이에 있는 0이 없으므로 0을 return
```



# *해답

파이썬 함수중에 2진법 숫자로 바꿔주는 함수 bin이 있다.

bin(param)을 하게 되면 str으로 된  '0b이진법숫자'를 return 한다. 

그 숫자에서 숫자 부분만 골라내서 0으로 시작해서 0으로 끝나는 부분까지 0의 개수를 새서 counter에 저장하고 1이 튀어나오면 counter 를 result 저장한다. 그리고 result 중 최고값을 max로 불러온다. 

```python
def solution(N):  
  bi_num = bin(N)[2:]
  result = []
  counter = 0
  for i in range(0, len(bi_num)):
    if bi_num[i]=='1':
      result.append(counter)
      counter=0
    else : 
      counter= counter+1 
  return max(result)
```

