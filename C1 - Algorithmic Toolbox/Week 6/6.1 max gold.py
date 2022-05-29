# Uses python3
import sys
import random
import time

def optimal_weight(W, w):
    # write your code here
    result = 0
    for i in w:
      if result+i>W:
        continue
      result= result + i
    return result

def bubblesort(a, n):
    for i in range(1,n):
      j=i
      while j<=n-2:
        if a[j-1]<a[j]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
        j=j+1  



W, n = list(map(int, input().split()))
a = []
a = list(map(int, input().split()))
bubblesort(a, n)
print(optimal_weight(W, a))









# Uses python3
import sys
import random
import time

def optimal_weight(W, w, n):
    # write your code here
    result = 0
    for j in range(n-1, 2):
      for i in range(j, 1):
        if result+a[i]>W:
          continue
        result= result + a[i]
    return result


W, n = list(map(int, input().split()))
a = []
a = list(map(int, input().split()))
print(optimal_weight(W, a, n))

