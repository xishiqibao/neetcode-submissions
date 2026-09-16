class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 2):
                    q.append((i, j))
                if(grid[i][j] == 1):
                    fresh += 1

        while q and fresh > 0:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if(0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1



