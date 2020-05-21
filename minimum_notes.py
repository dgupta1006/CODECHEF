def note(n):
    l = [100, 50, 10, 5, 2, 1]
    sum=0
    for i in range(l):
        sum+=n/i
t=int(input())
for i in range(t):
    n=int(input())


    for j in range(len(l)):
        while n>=l[j]:
            s=n/l[j]
            sum=sum+s
            n=n%l[j]
        if n==0:
            break
    print(int(sum))