##Segment tree implementation in python
##For minimum number in a given range

from math import ceil,log
array=[2,3,-1,4]
size=(1<<int(ceil(log(len(array),2))))*2-1

##initialization of tree with literal that wont count
tree=[99999999]*size
##lazy nodes of the tree
lazy=[0]*size

##construction of the segment tree
    ##low -> 0 (starting index array)
    ##high -> size-1 (last indes of the array)
    ##pos -> 0 (initial starting insed)
def construct(low,high,pos):
    if(low==high):
        ## the base node
        tree[pos]=array[low]
        return
    mid=(low+high)/2
    construct(low,mid,2*pos+1)
    construct(mid+1,high,2*pos+2)

    ##type of query to be performed
    tree[pos]=min(tree[2*pos+1],tree[2*pos+2])


##query on a segment tree
    ##qlow -> 'l' (starting query index)
    ##qhigh -> 'r' (endinng query index)
    ##low -> 0 (starting index array)
    ##high -> size-1 (last indes of the array)
    ##pos -> 0 (initial starting insed)
def query(qlow,qhigh,low,high,pos):
    if(qlow<=low and qhigh>=high):
        return tree[pos]
    if(qlow>high or qhigh<low):
        ##return something that wont count
        return 99999999
    mid=(low+high)/2
    ## type of query to be performed
    return min(query(qlow,qhigh,low,mid,2*pos+1),
               query(qlow,qhigh,mid+1,high,2*pos+2))


##lazy propagation on the segment tree
    ##startrange -> 'l_r' (starting index update)
    ##endrange -> 'r_r' (endinng index update)
    ##delta -> (updating factor)
    ##low -> 0 (starting index array)
    ##high -> size-1 (last indes of the array)
    ##pos -> 0 (initial starting insed)
def lazy_p(startrange,endrange,delta,low,high,pos):
    if(low > high):
        return
    if(lazy[pos] != 0):
        ##type of update to be performed
        tree[pos]+=lazy[pos]
        if(low != high):
            lazy[2*pos+1]+=lazy[pos]
            lazy[2*pos+2]+=lazy[pos]
        lazy[pos]=0
    if(startrange>high or endrange<low):
        return
    if(startrange<=low and endrange>=high):
        ##type of update to be performed
        tree[pos]+=delta
        if(low != high):
            lazy[2*pos+1]+=delta
            lazy[2*pos+2]+=delta
        return
    mid=(high+low)/2
    lazy_p(startrange,endrange,delta,low,mid,2*pos+1)
    lazy_p(startrange,endrange,delta,mid+1,high,2*pos+2)
    ##type of query to be performed
    tree[pos]= min(tree[2*pos+1],tree[2*pos+2])


##lazy propagation query
    ##qlow -> 'l' (starting query index)
    ##qhigh -> 'r' (endinng query index)
    ##low -> 0 (starting index array)
    ##high -> size-1 (last indes of the array)
    ##pos -> 0 (initial starting insed)
def query_p(qlow,qhigh,low,high,pos):
    if(low>high):
        ##return something that wont count
        return 99999999
    if(lazy[pos] != 0):
        ##type of update to be performed
        tree[pos]+=lazy[pos]
        if(low != high):
            lazy[2*pos+1]+=lazy[pos]
            lazy[2*pos+2]+=lazy[pos]
        lazy[pos]=0
    if(qlow>high or qhigh<low):
        ##return something that wont count
        return 99999999
    if(qlow<=low and qhigh>=high):
        return tree[pos]
    mid=(low+high)/2
    ## type of query to be performed
    return min(query_p(qlow,qhigh,low,mid,2*pos+1),
               query_p(qlow,qhigh,mid+1,high,2*pos+2))

construct(0,len(array)-1,0)
