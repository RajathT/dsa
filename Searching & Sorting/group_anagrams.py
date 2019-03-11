class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        """
        d = {}
        
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in d:
                d[temp] = [i]
            else:
                d[temp] += [i]
        
        return d.values()
        
