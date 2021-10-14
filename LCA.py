#Lowest Common Ancestor in a Binary Tree

#Binary Tree node
class Node:
    def __init__(self, data):
        self.data =  data
        self.left = None
        self.right = None

#Finds the path from root node to given root of the tree.
def findLCA(root, n1, n2):
    if (root is None or n1 is None or n2 is None):
     return None
    path1 = []
    path2 = []
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

#Finds the path from root node to given root of the tree, Stores the
#path in a vector path[], returns true if path exists otherwise false
def findPath( root, path, k):
   
    #Base case
    if root is None:
        return False
    
    #Store this node . The node will be removed if
    #not in path from root to n.
    path.append(root.data)

    if root.data == k :
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True

    #If not present in subtree rooted with root, remove root from
    #path[] and return false
    path.pop()
    return False

#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#Tests
print("LCA(4, 5) = %d" %(findLCA(root, 4, 5)))
print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" %(findLCA(root,3, 4)))
print("LCA(2, 4) = %d" %(findLCA(root,2, 4)))