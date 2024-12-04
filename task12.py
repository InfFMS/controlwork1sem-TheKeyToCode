def f(n):
    M = 0
    j = 0
    i=1
    while i*i<n:
        if(n%i==0):
            j+=2
            if(j>0):
                M = max(i,n//i)
        i+=1
    return M
l=[]
i = 3000000000
while(len(l)<10):
    M = f(i)
    if(M>0):
        l.append(i)
        l.append(M)
    i+=1
for i in range(0,10,2):
    print(l[i],l[i+1])
