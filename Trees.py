import utils


def dfs_pre_order(node: utils.TreeNode | None):
    if node is None:
        return
    print(node.val)
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)


def dfs_in_order(node: utils.TreeNode | None):
    if node is None:
        return
    dfs_in_order(node.left)
    print(node.val)
    dfs_in_order(node.right)


def dfs_post_order(node: utils.TreeNode | None):
    if node is None:
        return

    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node.val)


def bfs(node: utils.TreeNode | None):
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
    base_tree = utils.create_standard_tree()
    bfs(base_tree)


def test_dfs_all_cases():
    base_tree = utils.create_standard_tree()
    print("DFS Pre-order")
    dfs_pre_order(base_tree)
    print("DFS In-order")
    dfs_in_order(base_tree)
    print("DFS Post-order")
    dfs_post_order(base_tree)


if __name__ == "__main__":
    test_bfs()
    test_dfs_all_cases()
