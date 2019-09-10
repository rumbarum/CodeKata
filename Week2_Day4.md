# * 문제

nums는 숫자로 이루어진 배열입니다. 

가장 자주 등장한 숫자를 k 개수만큼 return해주세요.



```
nums = [1,1,1,2,2,3],
k = 2

return [1,2]

```

```
nums = [1]
k = 1

return [1]
```

# *해답

처음 for loop이 돌면서 각각의 숫자 개수를 파악하고 obj에 저장한다. obj = {배열의 값: 배열의 값 갯수 }

그리고 저장한 값을 키와 밸류를 반대로 만들어서 revobj에 저장 (revobj = {배열의값 갯수 : 배열의 값} ) 배열에 배열의 값 갯수를 함께 저장한다.  

저장한 배열을 값크기 순으로 정렬한다. 

정렬된 값을 k 갯수만큼 새로운배열에 담아 그 배열을 반환한다. 

```javascript
function topK(nums, k) {
  let obj={}
  for( let i=0 ; i<nums.length; i++){
    if(obj[nums[i]]===undefined){
      obj[nums[i]]=1
    }else{
      obj[nums[i]]+=1
    }
  }
 let revobj={}
 let arr =[]
  for (let key in obj){
    revobj[obj[key]]=Number(key);
    arr.push(obj[key])
  }
  arr.sort( (a,b)=>b-a)
let result= []
for(let i=0; i<k;i++){
  result.push(revobj[arr[i]])
}
return result
}

topK([1,],1)
```

모델 솔루션에서 본 축약하기, 나는 키와 밸류를 뒤집은 배열을 만들었는데, 그럴 필요 없이 배열에 집어넣고 배열의 값[1]을  기준으로 정렬하고 다른 값[0]을 리턴해도 된다. 

```javascript
 return arr.sort((a, b) => (b[1] - a[1])).slice(0,k).map(el => Number(el[0]));
```

