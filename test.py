def search(nums, target):
  
  def halfs (somelist, target, index):
    
    half = int(len(somelist)/2)
    #print("index:",index)
    #print("direct:",direct)
    #print(somelist)
    #print("half:",half)
    if len(somelist) == 1 and target != somelist[0]:
      return print(-1)
    if target > somelist[half]:
      index += half
      halfs(somelist[half:], target, index)
    elif target < somelist[half]: 
      halfs(somelist[:half],target, 0)
    elif target == somelist[half]:
        index += half
        print (index)
    
      
  return halfs(nums, target, 0)
''' 
search([-1,0,3,5,9,12],-1)
search([-1,0,3,5,9,12],0)
search([-1,0,3,5,9,12],3)
search([-1,0,3,5,9,12],5) 
search([-1,0,3,5,9,12],9)
search([-1,0,3,5,9,12],5)
'''
search([1, 2], 1)
search([1, 2], 2)
search([1, 2], 3)
search([1, 2], 0)

