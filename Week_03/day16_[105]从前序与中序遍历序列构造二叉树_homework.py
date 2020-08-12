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
#  👍 615 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution:
    def buildTreeBad(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归法 使用list.index 时间复杂度O(n^2) 空间复杂度O(n) 但切片使用额外空间
        """
        if not preorder and not inorder:
            return
        root = TreeNode(preorder[0])
        mid_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+mid_index], inorder[:mid_index])
        root.right = self.buildTree(preorder[1+mid_index:], inorder[mid_index+1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归法（优化） 时间复杂度O(n) 空间复杂度O(n)
        已知树中没有重复的元素，将中序转为set方便取根节点索引
        递归只传指针（尾指针不取到，所以头尾指针相等时就返回）
        """
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start == pre_end:
                return
            node = TreeNode(preorder[pre_start])
            mid_index = inorder_dic[preorder[pre_start]]
            node.left = helper(pre_start + 1, pre_start + 1 + mid_index - in_start, in_start, mid_index)
            node.right = helper(pre_start + 1 + mid_index - in_start, pre_end, mid_index + 1, in_end)
            return node

        inorder_dic = {v: k for k, v in enumerate(inorder)}
        root = helper(0, len(preorder), 0, len(preorder))
        return root

# leetcode submit region end(Prohibit modification and deletion)
