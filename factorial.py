def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
t=int(input())
for i in range (t):
    p=int(input())
    print(fact(p))