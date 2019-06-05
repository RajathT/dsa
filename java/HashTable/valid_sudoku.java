class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        for (int i=0; i<board.length; i++){
            Set<Character> set = new HashSet<>();
            for (int j=0; j<board[0].length; j++){
                if (board[i][j] != '.'){
                    System.out.print(board[i][j] + " ");
                    if (!set.add(board[i][j])) return false;
                }
            }
        }
        for (int i=0; i<board.length; i++){
            Set<Character> set = new HashSet<>();
            for (int j=0; j<board[0].length; j++){
                if (board[j][i] != '.'){
                    if (!set.add(board[j][i])) return false;
                }
            }
        }
        
        int[][] coords = new int[][]{{0,0}, {0,3}, {0,6}, {3,0}, {3,3}, {3,6}, {6,0},{6,3},{6,6}};
        
        for (int[] coord: coords){
            int i_max = coord[0]+3, j_max=coord[1]+3;
            Set<Character> set = new HashSet<>();
            for (int i=coord[0]; i<i_max; i++){
                for (int j=coord[1]; j<j_max; j++){
                    if (board[i][j] != '.'){
                        if (!set.add(board[i][j])) return false;
                    } 
                }
            }
        }
        
        return true;
    }
}
