def f(n):
    l = []
    i = 2
    while i*i<n:
        if(n%i==0):
            if(len(l)!=0):
                return 0
            else:
                l.append(i)
                l.append(n//i)
        i+=1
    if(len(l)==0):
        return 0
    print(n,l[0],l[1])
    return 1
for i in range(174457, 174505+1):
    f(i)
print("programm end")
