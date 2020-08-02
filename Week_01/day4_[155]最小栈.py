# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  
#  push(x) —— 将元素 x 推入栈中。 
#  pop() —— 删除栈顶的元素。 
#  top() —— 获取栈顶元素。 
#  getMin() —— 检索栈中的最小元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  pop、top 和 getMin 操作总是在 非空栈 上调用。 
#  
#  Related Topics 栈 设计 
#  👍 625 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:
    def __init__(self):
        """
        为使常数时间内检索到最小元素，需另开一变量存储，使得每个元素与其相应的最小值一一对应
        不能直接使用python中的sort()，时间复杂度为o(nlogn)，原理为Timesort
        """
        self.stack = []
        self.min_stack = [float('inf')]  # math.inf

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    def getStack(self):
        return self.stack

    def getMinStack(self):
        return self.min_stack


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-4)
print(obj.getMin())
print(obj.getStack())
print(obj.getMinStack())

obj.pop()
print(obj.getStack())
print(obj.getMinStack())
print(obj.top())
print(obj.getMin())

# leetcode submit region end(Prohibit modification and deletion)
