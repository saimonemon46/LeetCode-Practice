from collections import deque

class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert_Into_bst(root, d):
    # Base case : tree empty return new node
    if root is None:
        return BstNode(d)
    
    # Otherwise recur down the tree
    if d > root.data:
        root.right  = insert_Into_bst(root.right, d)
    else:
        root.left = insert_Into_bst(root.left, d)   
    return root


# Print (Level Order Traversal )
def level_traverse(root):
    # start from root
    # take a queue and put root, left, right and pop
    # same for all nodes till queue is empty    
    if root is None:
        return
    
    q = deque()
    q.append(root)
    q.append(None) # level marker
    
    # until queue is empty
    while q:
        curr = q.popleft() # pop front element
        
        # if current is None, we reached end of level
        if curr is None:
            print() # newline for level
            if q: # if queue is not empty, append another level marker
                q.append(None)
        else:
            print(curr.data, end = " ") # print current node
            # push left and right children
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)    
                
                
                
def take_input():
    print("Enter  intger data to be inserted in BST, -1 to stop")
    root = None
    while True:
        val = int(input())
        if val == -1:
            break
        # add val to BST
        root =insert_Into_bst(root, val)
    return root 



# Main Execution
if __name__ == "__main__":
    root = take_input()
    print("Level Order Traversal of BST is :")
    level_traverse(root)
    

