# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

'''
由题意可知：p、q为子树，若p、q为在同一颗树上，则有公共祖先
若节点 pp 在节点 rootroot 的左（右）子树中，或 p = root p=root ，则称 root 是 pq 的祖先
left right == p q
'''


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q: return root
    left = self.lowestCommonAncestor(root.left, q, p)
    right = self.lowestCommonAncestor(root.right, q, p)
    if not left: return right
    if not right: return left
    return root


# 优化
def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q: return root
    left = self.lowestCommonAncestor(root.left, q, p)
    right = self.lowestCommonAncestor(root.right, q, p)
    if left and right: return root
    if left: return left
    if right: return right
