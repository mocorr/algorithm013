# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 
# 的朋友。所谓的朋友圈，是指所有朋友的集合。 
# 
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出：2 
# 解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回 2 。
#  
# 
#  示例 2： 
# 
#  输入：
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出：1
# 解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 200 
#  M[i][i] == 1 
#  M[i][j] == M[j][i] 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 317 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCircleNumDFS(self, M: List[List[int]]) -> int:
        """
        DFS法
        时间复杂度：O(n^2)，整个矩阵都要被遍历，大小为n^2
        空间复杂度：O(n)，visited数组的大小? 递归本身带来的空间复杂度不考虑吗？
        """
        def _dfs(x):
            for y in range(len(M)):
                if y not in visited and M[x][y] == 1:
                    visited.add(y)
                    _dfs(y)

        cnt = 0
        visited = set()
        for i in range(len(M)):  # 不必写两层循环
            if i not in visited:
                cnt += 1
                visited.add(i)
                _dfs(i)
        return cnt

    def findCircleNumP(self, M: List[List[int]]) -> int:
        """
        并查集法
        时间复杂度：O(n^2) 访问整个矩阵一次n^2，并查集有路径压缩是O(1)?
        空间复杂度：O(n)，parent大小为n。
        """
        def _union(x, y):
            p[_parent(x)] = _parent(y)

        def _parent(x):
            root = x
            while p[root] != root:
                root = p[root]
            while p[x] != x:
                x, p[x] = p[x], root
            return root

        p = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    # M[i][j] = 0
                    # M[j][i] = 0
                    _union(i, j)

        return len(set([_parent(i) for i in range(len(M))]))

# leetcode submit region end(Prohibit modification and deletion)
