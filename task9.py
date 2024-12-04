def f(a,b):
    if b == 0:
        return 0
    if(a>b):
        return f(a-1,b) + b
    if(a<=b and b>0):
        return f(a,b-1) + a
def prime_number(n):
    i=1
    while i*i<n:
        if(n%i==0):
            print(i)
            if(i*i<n):
                print(int(n/i))
        i+=1
    return 0
print(prime_number(2097152))
#f = a*b, по сути, а 2 097 152 = 2**21, т.е. нужно понять сколько возможных пар
#a,b, где a*b = 2**21, т.е. a = 2**k, где k принадлежит [0,21], и будет такое b = 2**21-k.
#Ответ 22.
