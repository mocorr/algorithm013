# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

from typing import List, Any


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind + 1:])
        return root


