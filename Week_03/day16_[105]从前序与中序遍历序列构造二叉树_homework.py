# 根据一棵树的前序遍历与中序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组 
#  👍 612 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTreeCur(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归法 时间复杂度O(n) 空间复杂度O(n)
        思路：递归最小重复单元：由前序得到根节点的值，在中序找到对应的index，从而划分左右子树
        """
        if not preorder:
            return None
        root_node = TreeNode(preorder[0])
        mid_index = inorder.index(preorder[0])
        root_node.left = self.buildTreeCur(preorder[1:mid_index+1], inorder[:mid_index])
        root_node.right = self.buildTreeCur(preorder[mid_index+1:], inorder[mid_index+1:])
        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        # TODO 迭代法
        """
        return
# leetcode submit region end(Prohibit modification and deletion)
