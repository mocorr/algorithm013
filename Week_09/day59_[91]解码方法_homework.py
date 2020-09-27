# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划 
#  👍 489 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
	    """
		纸老虎 i-1和i-2级台阶有条件的爬楼梯问题而已！
		"""
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # 首位padding可以少写好几句
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':  # 最后一位能单独解码
                dp[i] += dp[i - 1]
            if i >= 2:  # 易漏
                if 10 <= int(s[i - 2]) * 10 + int(s[i - 1]) <= 26:  # 最后两位能组成有效码
                    dp[i] += dp[i - 2]
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
