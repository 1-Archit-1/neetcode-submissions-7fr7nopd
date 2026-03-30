class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set()  for i in range(9)]
        colset = [set() for i in range(9)]
        sqset = [set() for i in range(9)]
        for i in range(81):
            row = i//9
            col = i%9
            sq = row//3*3 + col//3
            num = board[row][col]
            if num=='.':
                continue
            if num in rowset[row]:
                return False
            else:
                rowset[row].add(num)
            if num in colset[col]:
                return False
            else:
                colset[col].add(num)
            if num in sqset[sq]:
                return False
            else:
                sqset[sq].add(num)
        return True 
                