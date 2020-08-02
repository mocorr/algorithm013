# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表 
#  👍 566 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归法 时间复杂度o(n)
        """
        if head is None or head.next is None:
            return head
        # head.next.next和head.next赋值顺序不能反
        new_head, head.next.next, head.next = head.next, head, self.swapPairs(head.next.next)
        return new_head
# leetcode submit region end(Prohibit modification and deletion)
