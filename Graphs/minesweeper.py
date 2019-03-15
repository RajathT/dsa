'''
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        elif board[x][y] == 'E':
            mines = 0
            for i,j in ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)):
                if x+i>=0 and x+i<len(board) and y+j>=0 and y+j<len(board[0]):
                    if board[x+i][y+j] == 'M':
                        mines += 1
            if mines:
                board[x][y] = str(mines)
                return board
            else:
                board[x][y] = 'B'
                for i,j in ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)):
                    if x+i>=0 and x+i<len(board) and y+j>=0 and y+j<len(board[0]):
                        self.updateBoard(board, [x+i,y+j])
        return board
                
                
        
