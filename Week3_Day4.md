# * 문제

주어진 숫자 배열에서, 0을 배열의 마지막쪽으로 이동시켜주세요.

원래 있던 숫자의 순서는 바꾸지 말아주세요.

\* 새로운 배열을 생성해서는 안 됩니다.

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

# *해답

뒤에서 부터 0을 찾아 0이 나올 경우 삭제하면서 카운터가 올라감

다 찾은 뒤 0의 개수 만큼 0을 뒤에 붙여줌

```python
def moveZeroes(nums):
  length= len(nums)
  counter=0
  
  for i in range(length-1,-1,-1):
    if nums[i] == 0:
      nums.remove(nums[i])
      counter =1+counter
      
  for x in range(0, counter):
    nums.append(0)
  
  return(nums)
  
moveZeroes([9,9])
```

