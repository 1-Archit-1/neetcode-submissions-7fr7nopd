class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0 
        maxarea = 0 
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 
            if grid[r][c] == 1:
                grid[r][c] = 2
                self.curr_area+=1 
            else:
                return 
            leftr, leftc = r, c-1 
            rightr,rightc = r, c+1 
            upr,upc = r-1, c
            downr,downc = r+1, c
            dfs(leftr,leftc)
            dfs(rightr, rightc) 
            dfs(upr, upc)
            dfs(downr, downc)

        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                curr = grid[r][c]
                if curr == 1:
                    self.curr_area = 0 
                    dfs(r,c)
                    maxarea= max(maxarea, self.curr_area)
        return maxarea