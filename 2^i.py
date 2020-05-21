t=int(input())
for i in range(t):
    l=[2048,1024,512,256,128,64,32,16,8,4,2,1]
    p=int(input())
    sum=0
    for j in range(len(l)):
        while p>=l[j]:
            sum+=1
            p=p-l[j]
        if p==0:
                break
    print(sum)