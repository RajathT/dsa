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
        matrix = [[0 for __ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(word1)+1):matrix[0][i] = i
        for i in range(len(word2)+1):matrix[i][0] = i
        
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                matrix[i][j] = 1 + min(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j]) if word2[i-1] != word1[j-1] else matrix[i-1][j-1]
        return matrix[-1][-1]
        
