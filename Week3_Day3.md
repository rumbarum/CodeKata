# 문제

양수로 이루어진 m x n 그리드를 인자로 드립니다.

상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.

 한 지점에서 우측이나 아래로만 이동할 수 있습니다.  

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7

설명: 1→3→1→1→1 의 합이 제일 작음

```

# *해답

그리드가 움직이는 경로의 경우의 수 계산하는 식을 만들고 그 경로를 타고 가면서 값을 더하는 걸 구현 

경우의 수 만들어가는 과정은 리커젼으로 쪼개면서 들어감. 움직이면서 경우가 나뉘면 두가지 경우를 다시 정의한 함수로 타고 내려간다. 그러다가 오른쪽 끝 또는 아래끝을 만나면 한가지로만 되는 경우로 움직인다. 

그 과정에서 위의 함수에서 내려받은 z 값들을 계속 더해 가면서 나온 z 값들을 result 배열에 담고 그중 최대값을 리턴한다. 

```python
def minPathSum(grid):
    result = []
    p=grid
    a=len(grid)-1
    b=len(grid[0])-1
    
    def flag (x,y,z):
      z=p[x][y]+z
      if x<a and y<b :
        flag(x+1,y,z)
        flag(x,y+1,z)
      if x==a and y<b :
        flag(x,y+1,z)
      if x<a and y==b:
        flag(x+1,y,z)
      if x==a and y==b:
        result.append(z)
    
    flag(0,0,0)
    print(result)
    return min(result)
```

