# * 문제

reverse 함수에 정수인 숫자를 인자로 받습니다.

그 숫자를 뒤집어서 return해주세요.

x: 숫자

return: 뒤집어진 숫자를 반환!

 예들 들어,

```
x: 1234
return: 4321
```

```
x: -1234
return: -4321
```

```
x: 1230
return: 321
```



Answer

```javascript
const reverse = x => {
 let stirngX = String(x);
 let arr = stirngX.split("")
 let arr2 = []
 for (let i = 0 ; i< arr.length ; i ++){
 arr2.unshift(arr[i])
 }
 if (arr2[0] === "0"){
   arr2.shift()
 }
 if (arr2[arr2.length-1] === "-"){
   arr2.unshift("-");
   arr2.pop()
 }
 return Number(arr2.join(""))
}
```

