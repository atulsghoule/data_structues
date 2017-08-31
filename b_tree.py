
## node of the tree
class node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        
## insertion in tree
def insert(root,data):
    if root is None:
        root = node(data)
    else:
        if root.data > data:
            if root.l_child is None:
                root.l_child = node(data)
            else:
                insert(root.l_child,data)
        else:
            if root.r_child is None:
                root.r_child = node(data)
            else:
                insert(root.r_child,data)
    return root



##deletion in binary search tree
def delete(root,data):
    if root==None :
        return root
    elif data < root.data :
        root.l_child=delete(root.l_child,data)
    elif data > root.data :
        root.r_child=delete(root.r_child,data)
    else:
        if root.l_child==None and root.r_child==None:
            root=None
        elif root.l_child==None :
            root= root.r_child
        elif root.r_child==None:
            root = root.l_child
        else:
            temp=findmin(root.r_child)
            root.data=temp.data
            root.r_child=delete(root.r_child,temp.data)
    return root
        
##find min in a tree
def findmin(root):
    if root==None or root.l_child==None:
        return root
    root=root.l_child


                    
## find a node and its level in the tree
def find(root,data,level=0):
    if root is None:
        return [False,level]
    elif root.data==data:
        return [True,level]
    elif root.data > data:
        return find(root.l_child,data,level+1)
    else:
        return find(root.r_child,data,level+1)

##inorder traversal
def pre_order(root,array=list()):
    if not root:
        return 
    pre_order(root.l_child,array)
    array.append(root.data)
    pre_order(root.r_child,array)
    return array

##preorder traversal
def in_order(root,array=list()):
    if not root:
        return        
    array.append(root.data)
    in_order(root.l_child,array)
    in_order(root.r_child,array)
    return array

## finds the max height of the tree
def max_height(root,l_start=0,r_start=0):
    if (not root) or (not root.l_child and not root.r_child):
        return 0
    l_start=max_height(root.l_child,l_start,r_start)+1
    r_start=max_height(root.r_child,l_start,r_start)+1
    return max(l_start,r_start)

