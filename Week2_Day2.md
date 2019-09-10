# * 문제

숫자로 이루어진 배열인 nums를 인자로 전달합니다.

숫자중에서 과반수(majority, more than a half)가 넘은 숫자를 반환해주세요.  

예를 들어,  

```
nums = [3,2,3]
return 3
```



```
nums = [2,2,1,1,1,2,2]
return 2
```

*가정 - nums 배열의 길이는 무조건 2개 이상*

# *해답

2개의 포문을 사용함.

1번이 돌면서 배열의 인자를 특정함 

2번이 돌면서 1번의 인자와 같은 개수가 몇개가 있는지 판단함. 

과반수가 넘는 수를 구하는 것이기 때문에 카운터가 전체 엘리먼트의 절반이 넘으면 해당 엘리먼트를 리턴하고 함수 종료 

```javascript
function moreThanHalf(nums) {
  
  for (let i = 0; i< nums.length; i++){
    let counter=0;
    for (let j =0; j < nums.length; j++){
      if(nums[i]===nums[j]){
        counter +=1 ;
      }
    }
    if (counter> nums.length/2){
      return nums[i]
    }
    
  }
}

moreThanHalf([1,1,1,11,2,2,2,2,2,22,2,2,])
```