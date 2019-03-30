'''
Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
'''
import collections, heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        C = collections.Counter(tasks)
        heap = [-x for x in C.values()]
        heapq.heapify(heap)
        cycle = 0
        while heap:
            temp = []
            for i in range(n+1):
                if heap:
                    temp.append(heapq.heappop(heap))
            for val in temp: 
                if val+1<0:
                    heapq.heappush(heap,val+1)
            cycle += n+1 if heap else len(temp)
        return cycle
                
            
                    
                
