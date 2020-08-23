# 515. 在每个树行中找最大值
def largestValues(self, root: TreeNode) -> List[int]:
    res = []
    def dfs(root, depth):
        if not root: return
        if len(res) <= depth:
            res.append(float("-inf"))
        res[depth] = max(res[depth], root.val)
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)

    dfs(root, 0)
    return res