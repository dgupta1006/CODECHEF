t = int(input())
for i in range(t):
    side = list(map(int, input().split()))
    side.sort()
    if(side[0]==side[1] and side[2]==side[3]):
        print("YES")
    else:
        print("NO")