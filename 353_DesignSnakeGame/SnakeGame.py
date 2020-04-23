class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food

        self.body = [[0, 0]]
        self.score = 0


    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # 取出当前蛇头
        head = self.body[0]
        x, y = head[0], head[1]
        if direction == 'U':
            nx, ny = x - 1, y
        elif direction == 'D':
            nx, ny = x + 1, y 
        elif direction == 'L':
            nx, ny = x, y - 1
        else:
            nx, ny = x, y + 1
        # 得到新的蛇头
        new_head = [nx, ny]

        # 蛇头撞墙
        if not (0 <= nx < self.height and 0 <= ny < self.width):
            return -1
        
        # 蛇头吃到东西
        if self.food and new_head == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            # 没有东西吃时，蛇头前进，蛇尾巴也要移动
            self.body.pop()
            # 没有吃到东西，但是蛇头撞到自己身上
            if new_head in self.body:
                return -1
        # 更新新的蛇头
        self.body.insert(0, new_head)
        return self.score




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
