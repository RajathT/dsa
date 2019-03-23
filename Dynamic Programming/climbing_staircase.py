class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 1:
            return 1

        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1

        for stair in range(2, n + 1):
            table[stair] = table[stair - 1] + table[stair - 2]

        return table[n]
        
            
        
        
