# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = [root]

        while len(q) != 0:
            size = len(q)
            curr = []
            for _ in range(size):
                v = q.pop(0)
                curr.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)

            res.append(curr)

        return res[::-1]
