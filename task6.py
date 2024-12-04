def f(n):
    if(n==1):
        return 1
    anser =f(n-1)+2**(n-1)
    return anser
print(f(12))
