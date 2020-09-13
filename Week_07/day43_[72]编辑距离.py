# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#  Related Topics 字符串 动态规划 
#  👍 1113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        递归+缓存 时间复杂度O(mn), 空间复杂度O(mn)
        编辑距离：3种(增删改)*2个词 看似有6种，其实只有3种
        """

        @functools.lru_cache(None)
        def _helper(i, j):
            if i == m or j == n:
                return max(m - i, n - j)
            if word1[i] == word2[j]:
                return _helper(i + 1, j + 1)
            return 1 + min(_helper(i, j + 1), _helper(i + 1, j), _helper(i + 1, j + 1))

        m, n = len(word1), len(word2)
        return _helper(0, 0)

    def minDistance_dp(self, word1: str, word2: str) -> int:
        """
        DP法 时间复杂度O(mn), 空间复杂度O(mn)
        第一行，是word1为空,变成word2的最少步数
        第一列，是word2为空,变成word1的最少步数
        """
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
