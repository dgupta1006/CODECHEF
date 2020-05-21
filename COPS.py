t=int(input())
for i in range(t):
    m,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    c=x*y
    house = []
    cops=[]
    for i in range(1,101):
        house.append(i)
    for i in range(len(a)):
        for i in range(a[i]-c,a[i]+c+1):
            cops.append(i)
    res = [i for i in house if i not in cops]
    print(len(res))
