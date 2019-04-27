'''
Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
'''
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [0]*len(edges)
        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x-1)
            rootY = find(y-1)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        for x, y in edges:
            if not union(x,y):
                return [x,y]
                
                
            
            
