# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def __init__(self):
        self.res = []

    def preorderCur(self, root: 'Node') -> List[int]:
        """
        递归法
        """
        if not root:
            return []
        self.res.append(root.val)
        for i in root.children:
            self.preorderCur(i)
        return self.res

    def preorder(self, root: 'Node') -> List[int]:
        """
        迭代法 时间复杂度O(n) 切片操作是O(1)? 空间复杂O(n)
        """
        if not root:
            return []
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children[::-1])
        return res


# leetcode submit region end(Prohibit modification and deletion)
