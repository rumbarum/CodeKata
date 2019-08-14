# * 문제

String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

```

텍스트
return: 중복되지 않은 알파벳 길이 (숫자 반환)
```

 예를 들어,

```
str = "abcabcabc"
return은 3
=> 'abc' 가 제일 길기 때문
```

```
str = "aaaaa"
return은 1
=> 'a' 가 제일 길기 때문
```

```
str = "sttrg"
return은 3
=> 'trg' 가 제일 길기 때문
```



*answer 

1. str 인자가 중복되는 값이 나오기 전까지의 길이를 구한다.
   1. 1번 for 문, i번째 인자부터 시작해서 somearr 에 집어넣는다. 
   2. 어레이를 forEach method로 다음에 오는 str[j]와 비교 한다. 
   3. 중복되는 값이 안나오면 중복검사를 한 인자를 somearr 에 추가한다.
   4. 같은 값이 나오는 경우가 생기면 2번 for 문을 break로 정지하고 다음번 인자로 넘어간다..
2. Result array에 str[i]로 시작하는 중복되지 않는 단어의 길이를 저장한다.
3. 저장된 길이중 최대값을 리턴한다. 

```javascript
const getLengthOfStr = str => {
 let result = [] 
 if (str.length>0){
 for( let i = 0 ; i < str.length-1 ; i++) { 
    let somearr=[]  
    somearr.push(str[i])
    for(j= i+1 ;j<str.length; j++ ) {
      let checker=false ;
      somearr.forEach(ele=>{
        if (checker===false && ele===str[j]){
           checker=true;
        }
      })
      if(checker===true){
        break;
      }else {
        somearr.push(str[j])
      }
   } result.push(somearr.length)
  }console.log(result)
  return Math.max(...result)
 }
 else{
   return 0
 }
}
```

