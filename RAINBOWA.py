t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    temp=[]
    if (arr==arr[::-1]):
        temp=list(set(arr))
        if (temp[-1]==7 and len(temp)==7):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


