class node:
    def _init_(self,data=None):
        self.data=data
        self.left=None
        self.right=None


def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def preorder(root):
    if root == None:
        return
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)


# def levelorder(root):
#     Q=[root]
#     Q.append(None)

#     while Q:
#         cur = Q.pop(0)
#         if cur:
#             print(cur.data,ends=" ")
#         elif len(Q)==0:
#             return
#         else:
#             Q.append(None)
#             print()
            
#         if cur.left:
#             Q.append(cur.left)
#         if cur.right:
#             Q.append(cur.right)
        
def levelorder(root):
    if root is None:
        return
    
    Q = [root]

    while Q:
        level_length = len(Q)
        for _ in range(level_length):
            cur = Q.pop(0)
            print(cur.data, end=" ")
            
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)
        print()  # Move the newline here to print after each level
     

root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(19)
root.left.right=node(14)
root.right.left=node(6)
root.right.right=node(12)
root.left.right.left=node(9)
root.left.right.right=node(5)
root.left.right.left.right=node(10)
root.right.left.right=node(16)
root.right.right.left=node(8)
root.right.right.right=node(11)
root.right.right.left.left=node(15)
root.right.right.right.left=node(17)
root.right.right.right.right=node(20)

print(root)
print(root.data)

# print("Inorder traversal")
# inorder(root)

# print("Preorder traversal")
# preorder(root)

# print("Postorder traversal")
# postorder(root)

print("Level order Traversal")
levelorder(root)