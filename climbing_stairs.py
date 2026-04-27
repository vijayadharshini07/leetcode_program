def climbstairs(n):
    if n<=2:
        return n
    a,b=1,2
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    return b
print("output for n=2:",climbstairs(2))
print("output for n=3:",climbstairs(3))
