# Week4学习笔记

---
## 1. 问题

- 二分法看似不难，但其实炒鸡难，完全分不清什么时候加等号，什么时候不加等号
- 本周着实有些太懈怠了 厌学情绪高涨

##２.作业

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
同leetcode 153题 寻找旋转排序数组中的最小值
```python
# Python
def findMinIndex(nums):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while lelft < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left
```

## ３. 知识点

### 3.1 深度优先搜索和广度优先搜索

* 树的前／中／后序其实就是深度优先搜索
* 树的层序遍历其实广度优先搜索
* 深度优先搜索(DFS)：借助一个栈；
* 广度优先搜索(BFS)：借助一个队列；

DFS 代码模板

递归写法
```python
# 递归写法
# Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

非递归写法
```python
# 非递归写法
# Python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```

BFS 代码模板
```python
# 非递归写法
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

### 3.2 贪心算法

贪心是思想．
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或者最优的算法
* 贪心：当下做局部最优判断（不能回退）；
* 回溯：能够回退；
* 动态规划：局部最优判断 + 回退；

### 3.3 二分查找

三个前提：
* 目标函数的单调性（单调递增或递减）；
* 存在上下界（bounded）；
* 能够通过索引访问（index accessible）；

代码模板：
```python
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```





