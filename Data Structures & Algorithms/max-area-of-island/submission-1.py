class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 
        isVisited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in isVisited
            or grid[r][c] == 0):
                return 0

            isVisited.add((r,c)) 
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if((r, c) not in isVisited and grid[r][c] == 1):
                    res = max(res, dfs(r, c))

        return res