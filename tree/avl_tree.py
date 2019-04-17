class AvlTree:

    # Node data for AVL Tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    # Insertion into AVL tree
    def insert(self, root, data):
        if not root:
            return AvlTree(data)
        elif root.data > data:
            root.left =  self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        # Update the height of the tree
        root.height = 1 + (max( self.getHeight(root.left),
                    self.getHeight(root.right)))

        # Get the balance factor(for type of rotation)
        balance = self.getBalance(root)

        # If the node is not balanced
        # Case 1 - Left Left
        if balance > 1 and data < root.left.data: 
            return self.rightRotate(root)
        
        # Case 2 - Right Right 
        if balance < -1 and data > root.right.data: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and data > root.left.data: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and data < root.right.data: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root  
        
    def leftRotate(self, node):
        nodeR = node.right
        nodeRL = nodeR.left

        # Perform rotation
        nodeR.left = node
        node.right = nodeRL

        # Update heights
        node.height = 1 +max(self.getHeight(node.left),
                    self.getHeight(node.right))
        nodeR.height = 1 +max(self.getHeight(nodeR.left),
                    self.getHeight(nodeR.right))
        
        # Return the new root
        return nodeR

    def rightRotate(self, node):
        nodeL = node.left
        nodeLR = nodeL.right

        # Perform rotation
        nodeL.right = node
        node.left = nodeLR

        # Update height
        node.height = 1 +max(self.getHeight(node.left),
                    self.getHeight(node.right))
        nodeL.height = 1 +max(self.getHeight(nodeL.left),
                    self.getHeight(nodeL.right))
        
        # Return the new root
        return nodeL
    
    def getHeight(self, root):
        if not root: 
            return 0
        return root.height

    def getBalance(self, root):
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def preOrder(self, root): 
        if not root: 
            return
        print(f"{root.data,root.height}", end ="")
        self.preOrder(root.left) 
        self.preOrder(root.right)

if __name__ =="__main__":
    # Driver program
    myTree = AvlTree(None)
    root = None
    
    root = myTree.insert(root, 10) 
    root = myTree.insert(root, 20) 
    root = myTree.insert(root, 30) 
    root = myTree.insert(root, 40) 
    root = myTree.insert(root, 50) 
    root = myTree.insert(root, 25)
    """
    The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50
    """  
    # Preorder Traversal
    print("Preorder traversal of the", "constructed AVL tree is") 
    myTree.preOrder(root) 
    print()  