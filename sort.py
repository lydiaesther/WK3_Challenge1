def list():
  list_sort=[2,0,6,5,1,7,'z','a']
  nums = {'evens':[],'odds':[],'chars':[]}
  for z in list_sort:
    if isinstance(z,str):
        nums['chars'].append(z)
    elif isinstance(z,int):
        if z % 2 !=0:
             nums['odds'].append(z)
        elif z % 2 ==0:
             nums['evens'].append(z)
  print(nums)

list()
        

        









