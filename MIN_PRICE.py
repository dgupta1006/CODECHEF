t=int(input())
for i in range(t):
    q,p=map(int,input().split())
    if (q>1000):
        a=q*p*0.9
    else:
        a=q*p
    print(format(a,'.6f'))
