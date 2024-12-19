# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = [root]
        res = []

        while len(q) != 0:
            size = len(q)
            for i in range(size):
                v = q.pop(0)

                if i == size - 1:
                    res.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
        return res
