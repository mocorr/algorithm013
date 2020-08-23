# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令： 
# 
#  
#  -2：向左转 90 度 
#  -1：向右转 90 度 
#  1 <= x <= 9：向前移动 x 个单位长度 
#  
# 
#  在网格上有一些格子被视为障碍物。 
# 
#  第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1]) 
# 
#  机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。 
# 
#  返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。 
# 
#  
# 
#  示例 1： 
# 
#  输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#  
# 
#  示例 2： 
# 
#  输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  答案保证小于 2 ^ 31 
#  
#  Related Topics 贪心算法 
#  👍 105 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        虽然自己写的代码惨不忍睹 但是击败了双99% 所以姑且留在这里有空再优化
        """
        max_route = 0
        flag = 0  # 0/1/2/3 北/东/南/西
        position = [0, 0]
        ob_x_dic = {}
        for ob in obstacles:
            if ob[0] not in ob_x_dic:
                ob_x_dic[ob[0]] = [ob[1]]
            else:
                ob_x_dic[ob[0]].append(ob[1])
        ob_y_dic = {}
        for ob in obstacles:
            if ob[1] not in ob_y_dic:
                ob_y_dic[ob[1]] = [ob[0]]
            else:
                ob_y_dic[ob[1]].append(ob[0])
        for c in commands:
            if c == -2:
                flag = (flag + 3) % 4
            elif c == -1:
                flag = (flag + 1) % 4
            elif c > 0:
                if flag == 0:
                    aim = position[1] + c
                    if position[0] in ob_x_dic:
                        tmp = []
                        for i in ob_x_dic[position[0]]:
                            if position[1] < i <= aim:
                                tmp.append(i)
                        if tmp:
                            position[1] = min(tmp) - 1
                        else:
                            position[1] = aim
                    else:
                        position[1] = aim
                elif flag == 1:
                    aim = position[0] + c
                    if position[1] in ob_y_dic:
                        tmp = []
                        for i in ob_y_dic[position[1]]:
                            if position[0] < i <= aim:
                                tmp.append(i)
                        if tmp:
                            position[0] = min(tmp) - 1
                        else:
                            position[0] = aim
                    else:
                        position[0] = aim
                elif flag == 2:
                    aim = position[1] - c
                    if position[0] in ob_x_dic:
                        tmp = []
                        for i in ob_x_dic[position[0]]:
                            if aim <= i < position[1]:
                                tmp.append(i)
                        if tmp:
                            position[1] = max(tmp) + 1
                        else:
                            position[1] = aim
                    else:
                        position[1] = aim
                elif flag == 3:
                    aim = position[0] - c
                    if position[1] in ob_y_dic:
                        tmp = []
                        for i in ob_y_dic[position[1]]:
                            if aim <= i < position[0]:
                                tmp.append(i)
                        if tmp:
                            position[0] = max(tmp) + 1
                        else:
                            position[0] = aim
                    else:
                        position[0] = aim
                # 显然，任意一次移动中: dis(原点，过程点) < max(dis(原点，本次起点), dis(原点，本次终点))
                max_route = max(max_route, position[0] * position[0] + position[1] * position[1])
        return max_route

    def robotSim1(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        官方题解
        个人改进：
        任意一次移动中: dis(原点，过程点) < max(dis(原点，本次起点), dis(原点，本次终点))，所以无需对每个过程点计算distance
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        direction = 0  # 北/东/南/西 --> 0/1/2/3
        obstacles = set(map(tuple, obstacles))
        x, y = 0, 0
        route = 0
        for c in commands:
            if c == -2:
                direction = (direction + 3) % 4
            elif c == -1:
                direction = (direction + 1) % 4
            elif c > 0:
                for i in range(c):
                    if (x + dx[direction], y + dy[direction]) not in obstacles:
                        x += dx[direction]
                        y += dy[direction]
                route = max(route, x * x + y * y)
        return route

# leetcode submit region end(Prohibit modification and deletion)
