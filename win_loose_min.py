t=int(input())
for i in range (t):
    x,y=map(int,input().split())
    w=x-y
    if(w<0):
        print(0)
    else:
        print(w)