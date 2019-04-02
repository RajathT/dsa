class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key = lambda x: (x.start, x.end))
        
        currEnd, res = intervals[0].end, 0
        for i in intervals[1:]:
            if i.start < currEnd:
                res += 1
                currEnd = min(currEnd, i.end)
            else:
                currEnd = i.end
        return res
            
