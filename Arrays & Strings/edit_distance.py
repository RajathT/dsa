class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
        """
        INFI = 999999
        m = len(word1)
        n = len(word2)
        MED = [[INFI for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            MED[i][0] = i #all deletion
        for j in range(n + 1):
            MED[0][j] = j #all insertion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    MED[i][j] = min(MED[i - 1][j - 1], 1 + MED[i - 1][j], 1 + MED[i][j - 1])
                else:
                    MED[i][j] = 1 + min(MED[i - 1][j], MED[i][j - 1], MED[i - 1][j - 1])
        return MED[m][n]
        
