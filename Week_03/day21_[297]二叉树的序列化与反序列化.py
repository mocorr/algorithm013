# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。 
# 
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树 设计 
#  👍 335 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CodecBFS:
    """
    广度优先 层序遍历
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        curr_layer = [root]
        res = []
        while curr_layer:
            next_layer = []
            for curr in curr_layer:
                if curr:
                    res.append(curr.val)
                    next_layer.extend([curr.left, curr.right])
                else:
                    res.append('n')
            curr_layer = next_layer
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodes = [(TreeNode(val) if val != 'n' else None) for val in eval(data)]
        i, j, n = 0, 1, len(nodes)  # i慢指针指向父节点，j快指针指向子节点
        while j < n:
            if nodes[i]:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]


class CodecDFS:
    """
    深度优先 先序遍历 递归
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'n'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def buildTree(nodes):
            val = nodes.popleft()
            if val == 'n':  # 若空则回到上一层
                return None
            node = TreeNode(val)
            node.left = buildTree(nodes)
            node.right = buildTree(nodes)  # 此时的nodes已经变化
            return node

        import collections
        data = collections.deque(data.split(','))
        root = buildTree(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
