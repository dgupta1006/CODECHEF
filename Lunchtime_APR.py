t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    p = list(map(int, input().split()))
    v = list(map(int, input().split()))
    zero = []
    one = []
    rem = 100 - s
    count=0
    for i in range(len(v)):
        if (v[i] == 0):
            zero.append(p[i])
        else:
            one.append(p[i])
        for i in range(len(zero)):
            for j in range(len(one)):
                if(zero[i] + one[j]<= rem):
                       count+=1
                else:
                    count=count+0
    if count>0:
        print("yes")
    else:
        print("no")



