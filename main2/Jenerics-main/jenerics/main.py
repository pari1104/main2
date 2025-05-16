# from typing import Generic, TypeVar

# T = TypeVar("T")

# class Box(Generic[T]):
#     def __init__(self, value: T):
#         self.value = value

#     def get_value(self) -> T:
#         return self.value

# int_box = Box(10)
# str_box = Box("hello")

# print(int_box.get_value())
# print(str_box.get_value())

# # def sum_number_generics(number:list[T]) -> T:
# #     return sum(numbers)
# # print(sum_number_generics([1,2,3,4,5,6]))
# # print(sum_number_generics([1.2, 2.1, 3.90]))



# # def sum_number(number:list[int]) -> int:
# #     return sum(numbers)




















# def factorial(n: int) -> int:
#     if n == 0  or n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(10))




# def fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2) 

# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))









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