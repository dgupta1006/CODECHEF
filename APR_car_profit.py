t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    count = 0
    p.sort()
    t=p[::-1]
    while(len(t)>=1):
       count+=t[0]
       while (count>1000000007):
           count = (count) % (1000000007)

       del t[0]
       for i in range(len(t)):
          if(t[i]>=1):
             t[i]=t[i]-1

    print(count)


