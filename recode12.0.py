t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    list=[]
    M=max(a)
    sum=1
    total=0
    maximum=0
    for i in(1,len(a)):
        for j in range(1,M):
            if(a[j]==a[i]):
             list.append(i)
             for k in range(1,len(list)):
                 if(list[k]-1==list[k-1]):
                     sum+=1
                     if (sum%2==0):
                       total+=sum/2
                     else:
                       total+=sum/2+1
                 else:
                     total+=1
                 if(total>max):
                     maximum=j
    print(maximum)



