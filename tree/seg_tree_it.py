# array ,tree 3*n
def combine(node1,node2):
    return node1+node2 

def build(size):
    for i in xrange(size):
        tree[size+i] = array[i]
    for i in xrange(size-1,0,-1):
        tree[i] = combine(tree[i<<1],tree[i<<1 | 1] )

def update(index,value,size):
    i = index + size
    tree[i] = value
    while i > 1 :
        tree[i>>1] = combine(tree[i],tree[i^1])
        i >>= 1

def query(l,r,size):
    #update here
    res = 0
    l,r = l+size,r+size+1
    while l < r:
        if l&1:
            res = combine(tree[l],res)
            l+=1
        if r&1:
            r-=1
            res = combine(tree[r],res)
        l,r = l>>1,r>>1
    return res
array = [1,2,3,4,5,6]
tree = [0]*(len(array)*3)
build(len(array))
print query(0,len(array),len(array))
update(1,5,len(array))
print query(0,len(array),len(array))
