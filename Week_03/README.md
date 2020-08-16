# 学习笔记

## 递归，归去来兮

树 ——> 递归

1. 节点的定义
2. 重复性（自相似性）

```python
# eg：阶乘
def Factoria(n):
    if n < = 1
  		return 1
    return  n * Factoria(n -1)

def recursion(level, param1, param2, ...): 
    # recursion terminator  终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level （当前级别的过程逻辑）
    process(level, data...) 
    # drill down （下层递归）
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed（清理当前层）
```

~~~java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
}
~~~

注意：

> 抵制人肉递归
>
> 找最近重复性
>
> 数据归纳法思维

## 分治

分治：将一个难以直接解决的大问题，分割成一些规模较小的相同问题，以便各个击破，分而治之。

适用范围：

> ​    1) 该问题的规模缩小到一定的程度就可以容易地解决
>
> ​    2) 该问题可以分解为若干个规模较小的相同问题，即该问题具有最优子结构性质。
>
> ​    3) 利用该问题分解出的子问题的解可以合并为该问题的解；
>
> ​    4) 该问题所分解出的各个子问题是相互独立的，即子问题之间不包含公共的子子问题。

算法基本步骤

> 分治法在每一层递归上都有三个步骤：
>
> step1 分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题；
>
> step2 解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题
>
> step3 合并：将各个子问题的解合并为原问题的解。

分治代码模板

```python
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

```java
private static int divide_conquer(Problem problem, ) {
  
  if (problem == NULL) {
    int res = process_last_result();
    return res;     
  }
  subProblems = split_problem(problem)
  
  res0 = divide_conquer(subProblems[0])
  res1 = divide_conquer(subProblems[1])
  
  result = process_result(res0, res1);
  
  return result;
}
```

## 回溯

**解决一个回溯问题，实际上就是一个决策树的遍历过程，核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」**，

思考

> 1、路径：也就是已经做出的选择。
>
> 2、选择列表：也就是你当前可以做的选择。
>
> 3、结束条件：也就是到达决策树底层，无法再做选择的条件。

```
def backtrack(...):
    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
```

