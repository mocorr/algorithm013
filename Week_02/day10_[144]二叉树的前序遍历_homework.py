# 给定一个二叉树，返回它的 前序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 330 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversalCur(self, root: TreeNode) -> List[int]:
        """
        递归法 时间复杂度O(n) 空间复杂度O(n)
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversalCur(root.left) + self.preorderTraversalCur(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代法 前/后序可用 中序不行
        时间复杂度O(n) 空间复杂度O(n)
        """
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        return res

    def preorderTraversalPython(self, root: TreeNode) -> List[int]:
        """
        迭代法 Pythonic（即标识法） 前/中/后序通用
        时间复杂度O(n) 空间复杂度O(n)
        """
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            if isinstance(curr, TreeNode):
                stack.append(curr.right)
                stack.append(curr.left)
                stack.append(curr.val)
            elif isinstance(curr, int):
                res.append(curr)
        return res

# leetcode submit region end(Prohibit modification and deletion)
