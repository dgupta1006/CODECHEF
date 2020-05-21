t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    new=[]
    res=[]

    for i in range(len(a)):
        if a[i]==1:
            new.append(i)
    if len(new)==1:
        print("YES")
    else:
       for i in range(len(new)-1):
         res= [new[i+1]-new[i]]
         minimum=min(res)
       if minimum>=6:
            print("YES")
       else:
            print("NO")

