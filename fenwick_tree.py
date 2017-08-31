# Python implementation of Binary Indexed Tree
tree=list()
def getsum(i):
    s = 0  
    i = i+1
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s
def updatebit(n , i ,v):
    i += 1
    while i <= n:
        tree[i] += v
        i += i & (-i)
 
def construct(array, n):
    for i in range(n):
        updatebit(n, i, array[i])
 
# Driver code to test above methods
array= [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
tree=[0]*(len(array)+1)
construct(array,len(array))
print("Sum of elements in arr[0..5] is " + str(getsum(5)))
array[3] += 6
updatebit(len(array), 3, 6)
print("Sum of elements in arr[0..5] is " + str(getsum(5)))
 

