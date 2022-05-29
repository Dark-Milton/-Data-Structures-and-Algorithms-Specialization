def bsearch(a,n):
    i,j = 0,len(a)
    # k < i => a[k] < n
    # k >= j => a[k] >= n
    while i != j:
        k = i + (j-i)//2
        if a[k] < n:
            i = k+1
        else:
            j = k
    return i
 
def find(a,n):
    k = bsearch(a,n)
    if k < len(a) and a[k] == n:
        return k

n = int(input())
a = list(map(int, input().split()))

m = int(input())
s = list(map(int, input().split()))
loc = []
for i in s:
    l=find(a,i)
    if l==0:
        loc.append(0)
    elif l:
        loc.append(l)
    else:
        loc.append(-1)
    
print(*loc, sep = " ")
        
# [(0, 0, None), (1, 0, 0), (2, 1, 1), (3, 3, None), (4, 3, 3), (5, 7, None)]