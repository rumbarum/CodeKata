# *문제

strs은 단어가 담긴 배열입니다.

공통된 시작 단어(prefix)를 반환해주세요.  

예를 들어

```
strs = ['start', 'stair', 'step']
return은 'st'

```

```
strs = ['start', 'wework', 'today']
return은 ''
```



## *Answer

3개의 로직이 함께 돌아간다. 

1.  배열의 첫 단어, 한글자씩 증가하면서 slice로 잘라내기 

2. 배열의 단어 증가 

3. 배열의 단어들 앞글자를 1.의 단어와 비교하기 

    아 그리고 flag 변수를 사용하여 로직의 탈출케이스 만들었다.

   이걸 조합해서 따단!~ 

```javascript
const getPrefix = strs => {
  if(strs.length>0){
  let flag = false; 
  let resultlength = 0
  for (let i=1 ; i < strs[0].length+1 ; i ++ ){
     if(flag===true){
         break;
    }else{
     let stand = strs[0].slice(0,i) ;
     for(let j = 1; j < strs.length ; j ++){
       console.log(stand)
       if( !strs[j].startsWith(stand) ){
         flag=true;
         resultlength=i-1
         break; 
       }else{
         resultlength=i
       }
      }
    } 
  }console.log(resultlength)
  return strs[0].slice(0,resultlength)}
  else{
    return ""
  }
}

getPrefix(['aac','aas'])
```

