# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        递归法(回溯)
        """
        def helper(tmp):
            if len(tmp) == n:
                res.append(tmp)
                return
            for i in range(n):
                if visited[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:  # 剪枝条件:和前一个元素值相同，且前一个元素未被使用
                    continue
                visited[i] = 1
                helper(tmp + [nums[i]])
                visited[i] = 0

        nums.sort()
        res = []
        n = len(nums)
        visited = [0] * n
        helper([])
        return res

# leetcode submit region end(Prohibit modification and deletion)
