# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 694 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        迭代法
        """
        res = [[]]
        for num in nums:
            res.extend([r + [num]for r in res])
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        递归法（回溯）
        """
        def helper(index, tmp):
            res.append(tmp)
            if index == n:
                return
            for i in range(index, n):
                helper(i + 1, tmp + [nums[i]])

        res = []
        n = len(nums)
        helper(0, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
