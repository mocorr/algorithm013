# Week3学习笔记

---
## 1. 问题

- 递归问题（除了树形遍历），特别是回溯问题，我都算不清时间/空间复杂度。
- 回溯问题感觉完全套泛型递归模板不太合适，自己改了下模板，主要是需要理解回溯是暴力穷举试错，回退到上一层时需要消除当前影响，可加入剪枝。

## 2. Tricks
- list.index时间复杂度为O(n)，可以考虑使用dict进行优化（类似数据库MapReduce倒排索引的思路）
- 递归时能传指针尽量不要用切片，会增加大量额外空间

## 3. 知识点

### 3.1 泛型递归、树递归

 - 不要人肉递归（递归的最大误区）
 - 找最近or最优重复子问题 
 - 数学归纳法思维

```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
	
    # process logic in current level 
    process(level, data...) 
    
    # drill down 
    self.recursion(level + 1, p1, ...) 
    
    # revert the current level status if needed
```

### 3.2 分治、回溯

分治、回溯是特殊的递归

#### 3.2.1 分治

 - 分解：找重复性，将原问题分解为多个子问题
 - 解决：求解各子问题
 - 组合：将子问题的结果组合成原问题结果

```python
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

#### 3.2.2 回溯

 - 本质是暴力穷举试错
 - 回到上层前需要撤销当前层造成的影响 
 - 时间复杂度高，可剪枝

自己写了个模板：
```python
# Python
def backtrack(track, options):
    # recursion terminator
    if reslut_condition: 
	   result.append(track)
	   return 

    # try all options
    for option in options:
        # pre-pruning(预剪枝）
        if bad_condition:
            continue

        # process logic in current layer
        process(level, data...)

        # drill down
        self.backtrack(track)
    
        # revert the current level states
        process_revert(level, data...)
```








