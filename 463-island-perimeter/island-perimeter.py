class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = [0]
        
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                ans[0] += 1
                return
            
            if (r,c) in visited :
                return 0
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        return ans[0]

            
            

            