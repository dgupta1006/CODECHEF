t=int(input())
for i in range(t):
    string=str(input())
    n=len(string)
    if(n%2!=0):
        a=string[:n//2]
        b=string[n//2+1:n]
    else:
        a = string[:n // 2]
        b = string[n // 2 :n]
    x = sorted(a)
    y = sorted(b)

    if (x==y):
        print("YES")
    else:
        print("NO")

