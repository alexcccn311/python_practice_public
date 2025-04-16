import random
import copy


class WaveFunctionCollapse:
    def __init__(self, width, height, tiles, adjacency_rules):
        self.width = width
        self.height = height
        self.tiles = tiles  # 可用瓦片
        self.rules = adjacency_rules  # 邻接规则
        self.grid = [[set(tiles) for _ in range(width)] for _ in range(height)]
        self.history = []  # 用于回溯
        self.change_counter = {}

    def get_neighbors(self, x, y):
        """ 获取 (x, y) 的邻居坐标 """
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < self.width - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < self.height - 1: neighbors.append((x, y + 1))
        return neighbors

    def collapse(self, x, y):
        """ 选择熵最小的一个单元格，并传播影响 """
        if len(self.grid[y][x]) > 1:
            self.history.append(copy.deepcopy(self.grid))  # 记录状态
            self.grid[y][x] = {random.choice(list(self.grid[y][x]))}

    def propagate(self):
        """ 传播约束 """
        stack = [(x, y) for y in range(self.height) for x in range(self.width) if len(self.grid[y][x]) == 1]
        while stack:
            x, y = stack.pop()
            tile = list(self.grid[y][x])[0]

            # 限制传播变更次数
            self.change_counter[(x, y)] = self.change_counter.get((x, y), 0) + 1
            if self.change_counter[(x, y)] > 10:
                print(f"⚠️ 发现死锁，回溯 {x, y}")
                self.backtrack()
                return

            # 传播影响
            for nx, ny in self.get_neighbors(x, y):
                if len(self.grid[ny][nx]) > 1:
                    allowed_tiles = {t for t in self.grid[ny][nx] if (tile, t) in self.rules}
                    if allowed_tiles != self.grid[ny][nx]:
                        self.grid[ny][nx] = allowed_tiles
                        if not self.grid[ny][nx]:  # 无可用瓦片，回溯
                            print(f"⚠️ 无解，回溯 {nx, ny}")
                            self.backtrack()
                            return
                        stack.append((nx, ny))

    def backtrack(self):
        """ 回溯上一步 """
        print("⚠️ 进入回溯模式...")
        if self.history:
            self.grid = self.history.pop()
        else:
            print("❌ 无解，完全失败！")

    def run(self):
        """ 运行 WFC """
        while any(len(cell) > 1 for row in self.grid for cell in row):
            x, y = min(((x, y) for y in range(self.height) for x in range(self.width) if len(self.grid[y][x]) > 1),
                       key=lambda pos: len(self.grid[pos[1]][pos[0]]))
            self.collapse(x, y)
            self.propagate()

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(list(cell)[0]) for cell in row))


# 测试运行
tiles = [0, 1, 2]
rules = {(0, 1), (1, 0), (1, 2), (2, 1), (2, 2)}

wfc = WaveFunctionCollapse(5, 5, tiles, rules)
wfc.run()
wfc.print_grid()
