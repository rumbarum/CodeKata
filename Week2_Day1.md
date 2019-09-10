# *문제

로마자에서 숫자로 바꾸기

1~3999 사이의 로마자 s를 인자로 주면 그에 해당하는 숫자를 반환해주세요. 로마 숫자를 숫자로 표기하면 다음과 같습니다.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```



로마자를 숫자로 읽는 방법은 로마자를 왼쪽부터 차례대로 더하면 됩니다.

III = 3

XII = 12

XXVII = 27

입니다.

 그런데 4를 표현할 때는 IIII가 아니라 IV 입니다.

뒤의 숫자에서 앞의 숫자를 빼주면 됩니다. 

9는 IX입니다.  

```
I는 V와 X앞에 와서 4, 9
X는 L, C앞에 와서 40, 90
C는 D, M앞에 와서 400, 900 
```



# Answer 

1. 4,9 문자를 제외하면 로마자는 해당 문자가 보여주는 문자를 숫자로 치환하면 된다. 
2. 로마자 마다 해당하는 숫자를 객체로 만들어 선언한다. 
3. 4,9 가 될때는 1,10,100의 자리 문자가 특정 문자 앞에 올경우이다 .
4. 3의 경우에는 1,10,100의 자리가 음수값을 가지면 된다.
5. 특정 문자가 뒤에 오는 상황을 고려해서 처리할 로직을 세운다.
6. 앞에서 바꾼값이 뒤에서 다시 영향을 줄 수도 있으니 하나의 로직을 거치도록 if ,else if로 합쳐 놓는다.
7. 만약 별도의 if들로 쪼갠다면, 마지막 if 에서 str[i]의 값이 문자인지 숫자인지 구분해서 처리 하면 될듯하다.  

```javascript
function romanToNum(s) {
  str= s.split("")
 let nummatch2 = {
   I:1,
   V:5,
   X:10,
   L:50,
   C:100,
   D:500,
   M:1000}

for (let i = 0; i<str.length; i++){
  if(str[i]==="C" && (str[i+1]==="D" || str[i+1]==="M")){
    str[i]=-100
    console.log(str[i])
  }else if(str[i]==="X" && (str[i+1]==="L" || str[i+1]==="C")){
    str[i]=-10
  }else if(str[i]==="I" && (str[i+1]==="V" || str[i+1]==="X")){
    str[i]=-1
  } else {
    str[i]=nummatch2[str[i]]
  }
  }
  answer= str.reduce(function(acc,ele){
    return acc+ele;
  });
  return answer
}

```

