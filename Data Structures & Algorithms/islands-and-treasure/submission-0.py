class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows= len(grid)
        cols = len(grid[0])
        INF = 2**31 -1 

        from collections import deque 
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        visited = set()
        while q:
            r,c = q.popleft() 
            visited.add((r,c))
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                nr = r+dr 
                nc = c+dc 
                if nr<0 or nc <0 or nr ==rows or nc ==cols or grid[nr][nc] in [-1,0] or (nr,nc) in visited:
                    continue
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c]+1
                    q.append((nr,nc))
            

                
        
        
        
