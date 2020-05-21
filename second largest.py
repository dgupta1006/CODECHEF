t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    m=[]
    m.append(a)
    m.append(b)
    m.append(c)
    m.sort()
    print(m[-2])
