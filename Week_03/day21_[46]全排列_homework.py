# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 840 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        递归法(回溯)
        """
        def helper(tmp):
            if len(tmp) == n:
                res.append(tmp)
                return
            for num in nums:
                if num not in tmp:
                    helper(tmp + [num])
        res = []
        n = len(nums)
        helper([])
        return res

# leetcode submit region end(Prohibit modification and deletion)
