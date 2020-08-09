# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseListRecur(self, head: ListNode) -> ListNode:
        """
        递归法 时间复杂度o(n)
        递归返回部分相当于已经完成反转，需要对当前node也反转
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverseListRecur(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代法 时间复杂度o(n)
        """
        curr, pre = head, None
        while curr:
            # next_src = curr.next
            # curr.next = pre
            # pre = curr
            # curr = next_src
            curr.next, pre, curr = pre, curr, curr.next  # curr.next与curr赋值顺序不能反
        return pre

# leetcode submit region end(Prohibit modification and deletion)
