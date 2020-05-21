def convert(n):
    return bin(n).replace("0b", "")
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        A,B=map(int,input().split())
        print(convert(A))
        print(convert(B))
