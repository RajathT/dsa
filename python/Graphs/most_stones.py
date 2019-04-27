'''
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
'''
class Solution(object):
    def removeStones(self, points):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent.setdefault(x,x)
            parent.setdefault(y,y)
            parent[find(x)] = find(y)
            
        for x, y in points:
            union(x, ~y)
            
        return len(points) - len({find(x) for x in parent})
        
            
        
