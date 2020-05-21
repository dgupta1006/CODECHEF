t=int(input())
for i in range(t):
    b=int(input())
    if(b<1500):
          h=0.1*b
          d=0.9*b
          g=d+h+b
    else:
          h=500
          d=0.98*b
          g=h+d+b
    print(g)
