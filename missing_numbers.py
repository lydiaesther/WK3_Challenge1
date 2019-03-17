a = [1,2,4,6,8,10]              
missing_num = []
for i in range(a[0],a[-1]+1):
    if i not in a:
        missing_num.append(i)
print(missing_num)    

