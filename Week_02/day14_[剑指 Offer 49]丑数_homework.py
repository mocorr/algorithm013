# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
#  Related Topics 数学 
#  👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        三指针法 时间复杂度O(n) 空间复杂度O(n)
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            f2 = ugly[i2] * 2
            f3 = ugly[i3] * 3
            f5 = ugly[i5] * 5
            ugly.append(min(f2, f3, f5))
            if ugly[-1] == f2:
                i2 += 1
            if ugly[-1] == f3:
                i3 += 1
            if ugly[-1] == f5:
                i5 += 1
        return ugly[n-1]
        
# leetcode submit region end(Prohibit modification and deletion)
