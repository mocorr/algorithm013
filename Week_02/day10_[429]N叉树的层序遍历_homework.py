# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索 
#  👍 100 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

import collections


class Solution:
    def levelOrderCommon(self, root: 'Node') -> List[List[int]]:
        """
        迭代法 时间复杂度O(n) 空间复杂度O(n)
        """
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            level = []
            for i in range(len(deque)):
                curr = deque.popleft()
                level.append(curr.val)
                deque.extend(curr.children)
            res.append(level)
        return res

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        迭代法-简化 时间复杂度O(n) 空间复杂度O(n)
        """
        if not root:
            return []
        res = []
        curr_layer = [root]
        while curr_layer:
            next_layer = []
            res.append([])
            for curr in curr_layer:
                res[-1].append(curr.val)
                next_layer.extend(curr.children)
            curr_layer = next_layer
        return res

    def levelOrderCur(self, root: 'Node') -> List[List[int]]:
        """
        递归法 访问顺序并非层序，各层内部相对顺序正确
        时间复杂度O(n) 空间复杂度O(n)
        """

        def helper(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                helper(child, level + 1)

        if not root:
            return []
        res = []
        helper(root, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
