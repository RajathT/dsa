'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.memo = [-1]*len(cost)
        self.memo[0], self.memo[1] = cost[0], cost[1]
        
        def helper(n):
            if self.memo[n] != -1:
                return self.memo[n]
            else:
                self.memo[n] = min(cost[n]+helper(n-1), cost[n]+helper(n-2))
                return self.memo[n]
        
        helper(len(cost)-1)
        
        return min(self.memo[-1], self.memo[-2])
        
        '''a, b = cost[0], cost[1]
        for i in cost[2:]:
            a, b = b, i + min(a,b)
        return min(a,b)'''
                
