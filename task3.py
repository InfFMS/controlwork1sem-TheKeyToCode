def f(x,y,z,w):
    print(((x!=z) or (not(y) or w)) == (not( not(w) or z or not(x) or y)))
    if ((x!=z) or (not(y) or w)) == (not(( not(w) or z) or (not(x) or y))):
        print("YES ",x,y,z,w)
        return 1
    return 0
for i in range(0,16):
    f(i//8,i//4%2,i//2%2,i%2)
