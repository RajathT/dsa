class Solution {
    public int minDistance(String word1, String word2) {
        int[][] matrix = new int[word1.length()+1][word2.length()+1];
        
        for (int i=0;i<word1.length()+1;i++) matrix[i][0] = i;
        for (int i=0;i<word2.length()+1;i++) matrix[0][i] = i;
        
        for (int i=1; i<word1.length()+1; i++){
            for (int j=1; j<word2.length()+1; j++){
                if (word1.charAt(i-1)!=word2.charAt(j-1))
                    matrix[i][j] = 1 + Math.min(Math.min(matrix[i-1][j],matrix[i-1][j-1]),matrix[i][j-1]);
                else
                    matrix[i][j] = matrix[i-1][j-1];
            }
        }
        
        return matrix[word1.length()][word2.length()];
    }
}
