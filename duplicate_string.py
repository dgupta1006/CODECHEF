
def isSubsetSum(set, n, sum):
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum);

    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


t=int(input())
for i in range(t):
       p=int(input())
       sum = int(input())
       set = list(map(int,input().split()))
       count=0
       n = len(set)
       if (isSubsetSum(set, n, sum) == True):
              count+=1
       print(count)       



