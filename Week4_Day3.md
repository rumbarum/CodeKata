# *문제

다음과 같이 input이 주어졌을 때,

같은 알파벳으로 이루어진 단어끼리 묶어주세요.

```python
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

output에서 순서는 상관없습니다.

# *해답

3개의 for loop이 사용 되었다. 

1번 for loop이 돌면서 배열의 첫 인자로 시작한다. set() 함수를  str에 사용하면, 중복된 값이 제거된 set 라는 데이터 타입이 나온다. 그리고 동일한 배열이 있는 문자는 순서가 달라도 set()을 사용시 비교 연산자에서 True 를 반환한다. 

2번째 for loop이 순환하면서 기존에 앞에 값과 겹치는 경우가 있는지 확인한다. 겹치는 경우가 있으면 switch 가 True가 된다. 

겹치는 경우가 있으면 다음 for loop 으로 넘어가고,겹치는 경우가 없다면 3번째 for loop이 뒤로 가면서 겹치는 경우가 있는지 확인을 하나. 겹치는 경우가 있으면 temp list 에 등록을 한다. 그리고 switch2가 True가 된다. 

앞에도 겹치는 경우가 없고, 뒤에도 겹치는 경우가 없을 경우 result에 1번 for loop의 해당 element 가 배열에 담겨 result에 추가 된다. 

앞에는 안겹치고 뒤에 겹치는 경우가 있으면 temp에 자신을 추가한다. 그리고 reslut에 temp를 추가한다. 

그리고 result를return 한다. 

```python
def groupAnagrams(strs): 
    result= []
    for i in range(0, len(strs)):
        temp = []
        switch = False
        switch2 = False
        for k in range(i-1, -1, -1 ):
          if set(strs[i]) == set(strs[k]):
              switch = True              
        if not switch: 
          for j in range(i+1, len(strs)): 
            if set(strs[i]) == set(strs[j]):
    	        temp.append(strs[j])
    	        switch2 = True 
                    
        if not switch and not switch2:
          result.append([strs[i]])
        if not switch and switch2 :
          temp.append(strs[i])
          result.append(temp)
        print(result)
    return result
```

