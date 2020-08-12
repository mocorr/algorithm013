# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。 
# 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  进阶： 
# 
#  你能在线性时间复杂度内解决此题吗？ 
# 
#  
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 484 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """
        暴力法 时间复杂度O(n*k)
        """
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        双向队列 时间复杂度O(n) 空间复杂度O(n)
        思路：维护一个保存最大值(单调递减)的index的队列
        S1.右侧出队：比当前值小的
        S2.当前值入队
        S3.左侧出队：超出窗口的
        S4.队首即窗口内最大值
        """
        if len(nums) <= 1:
            return nums
        res = []
        quque = collections.deque()
        for i in range(len(nums)):
            while quque and nums[quque[-1]] < nums[i]:  # 只与最末比较 时间复杂度O(1)
                quque.pop()
            quque.append(i)
            if quque[0] < i - k + 1:
                quque.popleft()
            if i >= k - 1:
                res.append(nums[quque[0]])
        return res
# leetcode submit region end(Prohibit modification and deletion)
