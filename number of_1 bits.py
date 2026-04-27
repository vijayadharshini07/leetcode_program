def hammingWeight(n):
    count=0
    while n:
        n=n&(n-1)
        count+=1
    return count
print("output for n=11:",hammingWeight(11))
print("output for n=128",hammingWeight(128))
print("output for n=2147483645:",hammingWeight(2147483645))
