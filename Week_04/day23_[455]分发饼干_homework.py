# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干
# 的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满
# 足越多数量的孩子，并输出这个最大数值。 
# 
#  注意： 
# 
#  你可以假设胃口值为正。 
# 一个小朋友最多只能拥有一块饼干。 
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3], [1,1]
# 
# 输出: 1
# 
# 解释: 
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,2], [1,2,3]
# 
# 输出: 2
# 
# 解释: 
# 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
# 你拥有的饼干数量和尺寸都足以让所有孩子满足。
# 所以你应该输出2.
#  
#  Related Topics 贪心算法 
#  👍 191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # kids
        s.sort()  # cookies
        g_p, s_p = 0, 0
        count = 0
        while g_p < len(g) and s_p < len(s):
            if s[s_p] >= g[g_p]:
                count += 1
                g_p += 1
                s_p += 1
            else:
                s_p += 1
        return count

        
# leetcode submit region end(Prohibit modification and deletion)
