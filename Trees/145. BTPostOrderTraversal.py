# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def dfs(root):
            if root:
                dfs(root.left)
                
                dfs(root.right)
                a.append(root.val)
            else:
                return
        dfs(root)
        return a
