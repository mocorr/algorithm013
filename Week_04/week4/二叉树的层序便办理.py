# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    queue = collections.deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            cur = queue.popleft()
            if not cur: continue
            level.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
        if level: res.append(level)
    return res
