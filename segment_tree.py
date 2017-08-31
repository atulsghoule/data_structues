##Segment tree implementation in python
##For minimum number in a given range

from math import ceil,log
array=[-1,2,4,0]
size=(1<<int(ceil(log(len(array),2))))*2-1
tree=[99999999]*size
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
construct(0,len(array)-1,0)    
    
