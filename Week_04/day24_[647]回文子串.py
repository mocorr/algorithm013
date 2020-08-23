# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 333 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstringsBad(self, s: str) -> int:
        """
        暴力法 时间复杂度O(n^3) 空间复杂度？
        """
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count

    def countSubstringsDP(self, s: str) -> int:
        """
        动态规划法 dp的缺点是空间复杂度高
        时间复杂度O(n^2) 空间复杂度O(n^2)
        三类可合并：
        ① i = j 奇数base
        ② s[j] == s[i], j - i = 1 偶数base
        ③ s[j] == s[i], 且其中间是回文
        """
        count = 0
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for j in range(n):  # 两层遍历的顺序是难点
            for i in range(j + 1):
                if s[j] == s[i] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        """
        双指针法 容易理解 时间复杂度O(n^2) 空间复杂度O(1)
        不会找回文中心，奇偶各算一遍- -
        """

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                count[0] += 1
                i -= 1
                j += 1

        n = len(s)
        count = [0]
        for k in range(n):
            helper(k, k)
            helper(k, k + 1)
        return count[0]

# leetcode submit region end(Prohibit modification and deletion)
