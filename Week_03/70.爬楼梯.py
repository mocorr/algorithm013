'''
f(1)= 1
f(2) = 2
f(3) = 3
f(4) = f(2) + f（3）
F(n) = F(n -2 ) + F(n - 1)
# 斐波那契数列
'''

"""
由题意可推导： F(n) = F(n -2 ) + F(n - 1)
法一：斐波那契
法二： 递归 + 缓存 
法三：动态规划：类似与累加；不断的给自己增大。滚雪球
"""


class Solution(object):
    def climbStairs(self, n):
        from math import pow
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = 5 ** 0.5
        func = pow((sqrt5 + 1) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)
        return int(func / sqrt5)


class Solution1(object):
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2(object):
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        i, j, k = 0, 0, 1
        for i in range(n):
            i = j
            j = k
            k = i + j
        return k
