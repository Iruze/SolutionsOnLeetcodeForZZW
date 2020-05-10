# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 回退到上一格
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                new_d = (i + d) % 4
                # new_d保证了进入下一格的朝向跟进入之前还是一样的
                new_cell = (cell[0] + directions[new_d][0], \
                cell[1] + directions[new_d][1])
                # robot.move() 可能执行失败，如果成功则进入下一个格
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # 跟directions的四个方向对应，当进入下个格子，始终是向上的方向
                robot.turnRight()
        
        visited = set()
        # 依次是 上、右、下、左
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        backtrack()
        
