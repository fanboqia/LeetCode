class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    #binary tree traversal
    def searchRange(self, root, k1, k2):
        # write your code here
        nums = []
        self.traverse(root,k1,k2,nums)
        return nums
    def traverse(self,root,k1,k2,arr):
        if root != None:
            #preorder search
            if root.val >= k1 and root.val <= k2:
                arr.append(root.val)
            self.traverse(root.left,k1,k2,arr)
            self.traverse(root.right,k1,k2,arr)
                
node1 = TreeNode(1);
node2 = TreeNode(2);
node3 = TreeNode(3);
node1.left = node2
node1.right = node3

print Solution().searchRange(node1,1,2);
