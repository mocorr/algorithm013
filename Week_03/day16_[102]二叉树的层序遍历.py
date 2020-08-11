import collections


class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """
        迭代法 时间复杂度O(n) 空间复杂度O(n)
        """
        curr_layer = [root]
        res = []
        while curr_layer:
            next_layer = []
            tmp = []
            for curr in curr_layer:
                if not curr:
                    continue
                tmp.append(curr.val)
                next_layer.append(curr.left)
                next_layer.append(curr.right)
            curr_layer = next_layer
            if tmp:
                res.append(tmp)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        递归法 时间复杂度O(n) 空间复杂度O(n)
        访问顺序并非层序，各层内部相对顺序正确
        """
        def helper(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)

        res = []
        helper(root, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
