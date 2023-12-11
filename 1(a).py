n=input()
e="" 
count=0 
for i in n: 
    if i=='0': 
        e=e+i
        count=0
    if i=='1': 
        e=e+i 
        count=count+1 
        if count==5: 
            e=e+'0' 
            count=0
print(e)
