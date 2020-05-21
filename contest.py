t = int(input())
for i in range(t):
    n=input()
    s = input()
    n = len(s)
    if((n%2)==0):
        first = s[0:len(s) // 2]
        fr=first[::-1]
        second = s[len(s) // 2 if len(s) % 2 == 0
                      else ((len(s) // 2) + 1):]
        sr=second[::-1]
        if(first==fr and second==sr):
               print("YES")
        else:
               print("NO")

