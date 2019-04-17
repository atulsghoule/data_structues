##dictionary to store the tree
store=dict()

##node class represent the parent and rank of a particular set
class node:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.rank=0

##make set
def makeset(data):
    new_node=node(data)
    new_node.parent=new_node
    store[data]=new_node

##union set
def union(data1,data2):
    node1=store[data1]
    node2=store[data2]

    parent1=findset(node1)
    parent2=findset(node2)
    if parent1.data==parent2.data :
        return
    if parent1.rank >= parent2.rank :
        parent1.rank+=int(parent1.rank==parent2.rank)
        parent2.parent=parent1
    else:
        parent1.parent=parent2

##find set with path compression
def findset(new_node):
    parent=new_node.parent
    if new_node==parent :
        return new_node
    new_node.parent=findset(new_node.parent)
    return new_node.parent

##find representative
def repre(data):
    return findset(store[data]).parent.data
    
    
makeset(1)
makeset(2)
makeset(3)
makeset(4)
makeset(5)
makeset(6)
makeset(7)

union(1, 2)
union(2 ,3)
union(4 ,5)
union(6 ,7)
union(5 ,6)
union(3 ,7)

for i in range(1,8):
    print repre(i)
