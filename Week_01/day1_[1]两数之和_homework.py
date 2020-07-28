# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8755 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSumBad(self, nums: List[int], target: int) -> List[int]:
        """
        暴力法 两层循环 时间复杂度o(n^2)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        排序+双指针 时间复杂度o(n) 但两元素相等时不能取同一index，代码较丑
        """
        tmp = nums.copy()
        tmp.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            s = tmp[i] + tmp[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                src_i = nums.index(tmp[i])
                if tmp[i] != tmp[j]:
                    src_j = nums.index(tmp[j])
                else:
                    nums.pop(src_i)
                    src_j = nums.index(tmp[j]) + 1
                return [src_i, src_j]
        return []

    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        """
        # TODO:哈希法看不懂
        """



# leetcode submit region end(Prohibit modification and deletion)
