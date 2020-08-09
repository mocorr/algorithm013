# 给定一个二叉树，返回它的中序 遍历。 
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
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 605 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversalCur(self, root: TreeNode) -> List[int]:
        """
        递归法
        """
        if not root:
            return []
        return self.inorderTraversalCur(root.left) + [root.val] + self.inorderTraversalCur(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代法-Pythonic 时间复杂度O(n) 空间复杂度O(n)
        """
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            if isinstance(curr, TreeNode):
                stack.extend([curr.right, curr.val, curr.left])
            elif isinstance(curr, int):
                res.append(curr)
        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        迭代法-标记法 时间复杂度O(n) 空间复杂度O(n)
        """
        stack, res = [(0, root)], []
        while stack:
            flag, node = stack.pop()
            if not node:
                continue
            if flag == 0:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:
                res.append(node.val)
        return res
# leetcode submit region end(Prohibit modification and deletion)
