import unittest

from LCA import Node
from LCA import findLCA

class LCAtest(unittest.TestCase):
    
    #testing LCA function returns correct result for regular node cases
    def test_simple1(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 4, 5)
        assert lca == 2

    #tests if LCA returns 1 of the nodes searched
    def test_case2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 2, 4)
        assert lca == 2

    #testing LCA function when result is root node
    def test_case3(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 4, 6)
        assert lca == 1

    #testing LCA when root node of 1 subtree & child node of 2nd subtree is parent node
    def test_case4(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 3, 4)
        assert lca == 1

    #testing the case when the root node is the LCA
    def test_case5(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        lca = findLCA(root, 1, 3)
        assert lca == 1

    #null LCA test
    def test_null(self):
        root = None
        lca = findLCA(root, 4, 5)
        assert lca is None

if __name__ == '__main__':
    unittest.main()