/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    private int maxSum;
    
    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        findMax(root);
        return maxSum;
    }
    
    private int findMax(TreeNode node) {
        if (node == null) return 0;
        int left = findMax(node.left);
        int right = findMax(node.right);
        maxSum = Math.max(node.val + left + right, maxSum);
        int path = node.val + Math.max(left, right);
        return Math.max(path, 0);
    }
}
