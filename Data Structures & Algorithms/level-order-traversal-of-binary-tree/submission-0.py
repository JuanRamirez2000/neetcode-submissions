# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, depth):
            #No node at this depth for this branch
            if not node:
                return None
            #New depth reached, create an array for it
            if len(res) == depth:
                res.append([])

            #Get index of depth in final result array, add curr node value
            res[depth].append(node.val)

            #traverse left and right with depth + 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        #start alg
        dfs(root, 0)
        return res 