# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res=[]
        q=[]
        q.append(root)
        curr_level=0 
        while q:
            if root is None:
                return []   
            res.append([])
            for _ in range(len(q)):
                curr_node=q.pop(0)
                if curr_node is None:
                    res[curr_level].append(None)
                    continue
                res[curr_level].append(curr_node.val)
                
                q.append(curr_node.left)
                q.append(curr_node.right)
            
            mid=len(res[curr_level])//2
            if res[curr_level][0:mid] != res[curr_level][-1:-mid-1:-1]:
              return False
            if all(x is None for x in q):
                break
            curr_level+=1
        return True