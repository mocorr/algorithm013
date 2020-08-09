# 编写一个程序，找出第 n 个丑数。 
# 
#  丑数就是质因数只包含 2, 3, 5 的正整数。 
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
#  Related Topics 堆 数学 动态规划 
#  👍 353 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumberBad1(self, n: int) -> int:
        """
        暴力法1 对所有正整数逐个判断是否为丑数
        """
        count = 0
        i = 0
        while count < n:
            i += 1
            a = self.isUglyNumber(int(i))
            if a:
                count += 1
        return i

    def isUglyNumber(self, num):
        if num <= 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1

    def nthUglyNumberBad2(self, n: int) -> int:
        """
        暴力法2 由丑数扩充丑数
        """
        count = 0
        i = 0
        ugly = [1]
        while count < n:
            i += 1
            if i in ugly:
                count += 1
                ugly.extend([2 * i, 3 * i, 5 * i])
        return i

    def nthUglyNumber(self, n: int) -> int:
        """
        三指针 时间复杂度O(n) 空间复杂度O(n)
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            f2 = ugly[i2] * 2
            f3 = ugly[i3] * 3
            f5 = ugly[i5] * 5
            ugly.append(min(f2, f3, f5))
            if ugly[i] == f2:
                i2 += 1
            if ugly[i] == f3:
                i3 += 1
            if ugly[i] == f5:
                i5 += 1
        return ugly[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
