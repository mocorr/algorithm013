# 学习笔记
## 一、循环(重复)

不断的重复、有始有终

循环实现

```java
private loop(){
    for(start; end; loop termination){
        expression1;
        expression2;
        expression3;        
    }
}
```

~~~python33
def loop():
    for start in end/loop_termination:
        expression1;
        expression2;
        expression3;  
~~~

## 二、递归

------

特征：自相似性、有始有终

实现：归去来兮、适可而止

何时想到递归？

> 子问题与原始问题做同样的事

递归实现：

~~~java
private void recursion(int level,int param1,int param2...):{
    // 终止条件(recursion terminato)
    if(level > MAX_LEVEL){
        # process_rsult
        return
    }
    // 处理此层过程逻辑(process logic in current level)
     process(level, data1, data2...)
    // 进入下一层（dill down）
    recursion(level: level + 1, newParam):
    // 如果需要恢复此层状态    
}
~~~

```python3
def recursion(level, param1, param2...):
    # 终止条件(recursion terminato)
    if level > MAX_LEVEL:
       # process_rsult
        return
    # 处理此层过程逻辑(process logic in current level)
    process(level, data1, data2...)
    # 进入下一层（dill down）
    self.recursion(level + 1, param1, param2...):
    # 如果需要恢复此层状态
```



## 二、分治

---

定义：分而治之，群臣归一

何时想到分治？

> 当复杂的问题可以拆分成简单的子问题

分治实现：

```Java
private static int divide_conquer(Problem, Param1, Param2...) {
  // 终止条件
  if (problem == NULL) {
    int res = process_last_result();
    return res;     
  }
  // 拆分子问题
  subProblems = split_problem(problem)
  
  res0 = divide_conquer(subProblems[0])
  res1 = divide_conquer(subProblems[1])
  ... 
  // 合并子问题结果
  result = process_result(res0, res1);
  
  return result;
}
```

~~~python3
def divide_conquer(Problem, Param1, Param2...):
     # 终止条件
     if problem is None:
        return 
     # 拆分子问题
     subproblems = split_problem(problem, data) 
     subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
     subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
     subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
      ...
   	 # 合并子问题结果
     result = process_result(subresult1, subresult2, subresult3, …)
~~~

## 三：回溯

---

采用“试错”思想，尝试“分步”去解决问题。在分步的过程中。根据上层结果，尝试此层最优解决此问题，如果此层较于上层不是最优则回溯。





## 四、DP(**Dynamic programming**) 动态规划/动态递推

------

定义

> In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. 
>
> 在这两种情况下，它都是指通过递归的方式将复杂问题分解为更简单的子问题来简化它。虽然有些决策问题不能用这种方式分解，但是跨越多个时间点的决策通常会递归地分解。
>
> Simplifying a complicated problem by breaking it down into simpler sub problem(in a recursibe manner)
>
> 把一个复杂的问题分解成更简单的子问题简化它(用一种递归的方式)

自低向上

动态规划关键点：

* 最优子结构
* 储存中间状态
* 递推公式(状态转移方程，DP方程)
* eg

```python3
# 一维
Fib：
    opt[i] = opt[n - 1] + opt[n - 2]
# 二维
  opt[i][j] = opt[i + 1][j] + opt[i][j + 1]
```



以斐波那契数列为例：

```shell
F(0) = 0, F(1) = 1 

F（N） =  F（N　－　１）　＋ F（N　－　２）（N >= 2）
```

递归(傻递归)：

若计算F(4)；需计算 

```
lin1 F(4) = f（3）、f（2）， 
lin2 F(3):f（2）、f（1）， F(2) = f(1) + f(0)
```

DP：

```
i(0) = 0, i(1) = 1
[0, 1, 1, 2, 3, 5]
```

## 总结

动态规划、递归、分治、无本质区别

共性： 重复子问题

异性：最优子结构、中途淘汰次优