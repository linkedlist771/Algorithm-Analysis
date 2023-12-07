from __future__ import annotations

class BinaryTreeNode:
    data: int   
    left: BinaryTreeNode
    right: BinaryTreeNode
    
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    root: BinaryTreeNode
    
    def __init__(self, root: BinaryTreeNode):
        self.root = root
        
    def insert(self, data: int) -> None:
        self._insert_recursive(self.root, data)
        
    def _insert_recursive(self, node: BinaryTreeNode, data: int) -> None:
        if not node:
            return BinaryTreeNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def inorder(self) -> None:
        def _inorder_recursive(node: BinaryTreeNode):
            if node:
                _inorder_recursive(node.left)
                print(node.data)
                _inorder_recursive(node.right)
        _inorder_recursive(self.root)

    def preorder(self) -> None:
        def _preorder_recursive(node: BinaryTreeNode):
            if node:
                print(node.data)
                _preorder_recursive(node.left)
                _preorder_recursive(node.right)
        _preorder_recursive(self.root)

    def postorder(self) -> None:
        def _postorder_recursive(node: BinaryTreeNode):
            if node:
                _postorder_recursive(node.left)
                _postorder_recursive(node.right)
                print(node.data)
        _postorder_recursive(self.root)


def main():
    # 创建一个根节点
    root = BinaryTreeNode(10)

    # 初始化二叉树
    tree = BinaryTree(root)

    # 插入一些数据
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    # 中序遍历
    print("Inorder Traversal:")
    tree.inorder()

    # 前序遍历
    print("\nPreorder Traversal:")
    tree.preorder()

    # 后序遍历
    print("\nPostorder Traversal:")
    tree.postorder()

if __name__ == "__main__":
    main()