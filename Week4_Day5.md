

# *문제

오름차순인 숫자 nums 배열과 찾아야할 target을 인자로 주면,

target이 몇 번째 index인지 return 해주세요.  



```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
설명: 찾지 못하면 -1로 return 해주세요.
```

\* nums 배열에 있는 요소는 서로 중복된 값이 없습니다.      

# *해답

search내에 halfs라는 function 을 정의한다. halfs 는 인자로 somelist, target, index를 받는다 .

halfs 실행시 somelist의 길이의 절반 값을 half에 할당한다. 그리고 그 somelist[half]의 값과 target 값의 대소를 비교 한다. 

target 이 크면 index에 half를 더한 값을 가지고 halfs 를 진행하고 target이 작으면 index에 0을 넣고 halfs를 다시 돌린다. 

somelist의 길이가 1 이고 , target 이 아니라면 -1 을 return하여 리커전을 종료하고,  target과 sometlist[half]가 일치하면 index + half 를 return 하여 함수를 종료한다. 

```python
def search(nums, target):
  
  def halfs (somelist, target, index):
    
    half = int(len(somelist)/2)
    if len(somelist) == 1 and target != somelist[0]:
      return print(-1) 
    if target > somelist[half]:
      index += half
      halfs(somelist[half:], target, index)
    if target < somelist[half]:
      halfs(somelist[:half],target, 0)
    if target == somelist[half]:
      index += half
      return index
      
  return halfs(nums, target, 0) 
```