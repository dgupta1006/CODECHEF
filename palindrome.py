t=int(input())
for i in range(t):
    p=input()
    q=p[::-1]
    if (p==q):
        print("wins")
    else:
        print("losses")

