t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=1
    max=1
    min=1000
    for i in range(1,n):
       if(a[i]-a[i-1]<=2):
          count+=1
       else:
          if(max<count):
              max=count
          if(min>count):
              min=count
          count=1
       if(i==n-1):
           if (max < count):
               max = count
           if (min > count):
               min = count
    print(min,max)