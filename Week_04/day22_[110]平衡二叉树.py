# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。 
#  
# 
#  示例 1: 
# 
#  给定二叉树 [3,9,20,null,null,15,7] 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回 true 。 
#  
# 示例 2: 
# 
#  给定二叉树 [1,2,2,3,3,null,null,4,4] 
# 
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#  
# 
#  返回 false 。 
# 
#  
#  Related Topics 树 深度优先搜索 
#  👍 454 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return 0
            left_height, right_height = helper(node.left), helper(node.right)
            if abs(left_height - right_height) > 1:
                flag[0] = False
            return max(left_height, right_height) + 1

        flag = [True]
        helper(root)
        return flag[0]


# leetcode submit region end(Prohibit modification and deletion)
