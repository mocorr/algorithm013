# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start: int, idx: int):
            for i in range(start, n + 1 - (k - 1 - idx)):
                option[idx] = i
                if idx == k - 1:
                    ans.append(option[:])
                else:
                    dfs(i + 1, idx + 1)

        ans = []
        option = [0] * k
        dfs(1, 0)
        return ans
