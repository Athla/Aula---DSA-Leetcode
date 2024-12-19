import utils


def dfs_pre_order(node: utils.TreeNode | None):
    """
    Pre-order traversal is a type of depth-first search algorithm.
    """
    if node is None:
        return
    print(node.val)
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)


def dfs_in_order(node: utils.TreeNode | None):
    """
    In-order traversal is a type of depth-first search algorithm.
    """
    if node is None:
        return
    dfs_in_order(node.left)
    print(node.val)
    dfs_in_order(node.right)


def dfs_post_order(node: utils.TreeNode | None):
    """
    Post-order traversal is a type of depth-first search algorithm.
    """
    if node is None:
        return

    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node.val)


def bfs(node: utils.TreeNode | None):
    """
    Breadth-first search is a type of search algorithm that traverses a tree level
    """
    if node is None:
        return
    queue: list[utils.TreeNode] = []
    queue.append(node)
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


def test_bfs():
    print("---BFS---")
    base_tree = utils.create_standard_tree()
    bfs(base_tree)
    print("---------")


def test_dfs_all_cases():
    print("---DFS---")
    base_tree = utils.create_standard_tree()
    print("DFS Pre-order")
    dfs_pre_order(base_tree)
    print("DFS In-order")
    dfs_in_order(base_tree)
    print("DFS Post-order")
    dfs_post_order(base_tree)
    print("---------")


if __name__ == "__main__":
    print("Running tests")
    print(f"Initial Node: \n{utils.show_std_tree()}")
    test_bfs()
    test_dfs_all_cases()
