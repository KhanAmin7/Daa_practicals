class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorderTraversal(root):
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Pre order traversal of tree")
preorderTraversal(root)
print("\nPost order traversal of tree ")  
postorderTraversal(root)
print("\nIn-Order Traversal Of Tree:")  
inorderTraversal(root)