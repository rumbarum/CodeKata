# * 문제

인자인 height는 숫자로 이루어진 배열입니다.

그래프로 생각한다면 y축의 값이고, 높이 값을 갖고 있습니다.



아래의 그래프라면 height 배열은 [1, 8, 6, 2, 5, 4, 8, 3, 7] 입니다.

![img](https://storage.googleapis.com/replit/images/1555380144403_97221ca23fbb92beaae5b6c800ceb5c8.pn)

저 그래프에 물을 담는다고 생각하고, 

물을 담을 수 있는 가장 넓은 면적의 값을 반환해주세요.

###### *가정  배열의 길이는 2이상입니다.



# *해답

2가지 접근이 가능할것 같다. 

1. 최고의 넓이 구하는 루트를 만들어서 해결
2. 모든 가능한 넓이 구하고 그중 최대값 구하기 

1번은 케이스를 잘 뽑아내면 계산이 빨라질 수 있으나 모든 케이스 맞출라면 어려움 

2번이 계산이 길어지지만 단순하고 모든 케이스 소화가 가능하다 .

2개의 for loop 이 돌면서 배열인자값 별로 나오는 면적을 다 계산한다. 

처음 for loop이 인자들을 지칭하고 , 다음 for loop이 인자들과 떨어진 거리 * 두인자의 높이값중 작은 값을 가지고 면적을 구하여 배열에 저장한다. 

면적을 저장한 배열에서 최대값을 반환한다. 

```javascript
function getMaxArea(h) {
  result= [];
  for (let i =0; i<h.length ; i++ ){
    for (let j = 0; j<h.length; j++){
      if(j===i) continue;
      if(h[i]>=h[j]){
        result.push( h[j]*(Math.abs(j-i))  )
      }else{
        result.push( h[i]*(Math.abs(j-i)) )
      }
    }
  }
  return result.sort((a,b)=>b-a)[0]
  
}

getMaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7] ) ==> 49
```

