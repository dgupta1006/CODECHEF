t= int(input())
for i in range(t):
    N,K=map(int,input().split())
    dic=list(map(str,input().split()))
    new=[]
    for i in range(K):
        p=list(map(str,input().split()))
        for j in range(1,len(p)):
            new.append(p[j])
    for i in dic:
        if i in new:
            print("Yes",end=" ")
        else:
            print("No",end=" ")


