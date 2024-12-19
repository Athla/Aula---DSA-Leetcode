from typing import override


class TreeNode:
    """
    Definition for a binary tree node.
    A binary tree node has a value, a left child, and a right child.
    """

    def __init__(self, x: int):
        self.val: int = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    @override
    def __str__(self) -> str:
        return str(self.val)

    ## Create a function that represents the whole tree
    ## This function is used to create a standard tree for testing.
    ## The tree is created in the following way:
    ##         1
    ##        / \
    ##       2   3
    ##      / \ / \
    ##     4  5 6  7


def create_standard_tree() -> TreeNode:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def show_std_tree() -> str:
    return "         1\n        / \\\n       2   3\n      / \\ / \\\n     4  5 6  7"
