
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
                
## deletion in binary search tree
'''def delete(self, key):
    if self.key == key:
        if self.right and self.left:  
            [psucc, succ] = self.right._findMin(self)
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            succ.left = self.left
            succ.right = self.right
            return succ                
        else:
            if self.left:
                return self.left    
            else:
                return self.right    
    else:
        if self.key > key:          
            if self.left:
                self.left = self.left.delete(key)
        else:           
            if self.right:
                self.right = self.right.delete(key)
    return self'''
                    
## find a node and its level in the tree
def find(root,data,level=0):
    if root is None:
        return False,level
    elif root.data==data:
        return True,level
    elif root.data > data:
        return find(root.l_child,data,level+1)
    else:
        return find(root.r_child,data,level+1)

##inorder traversal
def in_order(root,array=list()):
    if not root:
        return 
    in_order(root.l_child,array)
    array.append(root.data)
    in_order(root.r_child,array)
    return array

##preorder traversal
def pre_order(root,array=list()):
    if not root:
        return        
    array.append(root.data)
    pre_order(root.l_child,array)
    pre_order(root.r_child,array)
    return array

## finds the max height of the tree
def max_height(root,l_start=0,r_start=0):
    if (not root) or (not root.l_child and not root.r_child):
        return 0
    l_start=max_height(root.l_child,l_start,r_start)+1
    r_start=max_height(root.r_child,l_start,r_start)+1
    return max(l_start,r_start)

