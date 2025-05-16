
class TreeNode:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None






class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value:int):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)
    
    def _insert_rec(self, node: TreeNode, value:int):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)

            else:
                self._insert_rec(node.left,value)

        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def inorder_travelsal(self, node: TreeNode):
        if node:
            self.inorder_travelsal(node.left)
            print(node.value, end=" ")
            self.inorder_travelsal(node.right)


tree = BinaryTree()
for number in [10,5, 15, 2,7, 12, 20, 11, 100, 80, 65]:
    tree.insert(number)

tree.inorder_travelsal(tree.root)
