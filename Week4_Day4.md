# *문제 

숫자로 이루어진 리스트 nums를 인자로 주면,

그 안에서 어떤 연속적인 요소를 더했을 때 가장 큰 값이 나오나요?

가장 큰 값을 찾아 return해주세요. 

```
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
설명: [4,-1,2,1] 를 더하면 6이 가장 크기 때문
```

# *해답

앞의 수와 더한 값이 더하지 않은값과 비교해서 큰수를 자리에 남긴다. 

그 배열에서 최고값을 구해서 return 한다. 

```python
def maxSubArray(nums):
    for i in range(1, len(nums)):
      nums[i] = max(nums[i], nums[i-1]+nums[i])
    
    return max(nums)
```

