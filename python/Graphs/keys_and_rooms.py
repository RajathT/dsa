'''
Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

'''
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        visited = []
        
        def helper(ind, rooms):
            if not rooms or ind in visited:
                return
            visited.append(ind)
            for room in rooms[ind]:
                helper(room, rooms)
        
        helper(0,rooms)
        
        return len(visited)==len(rooms)
            
                
            
        
