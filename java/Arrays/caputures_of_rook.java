class Solution {
    public int numRookCaptures(char[][] board) {
        int res = 0;
        for (int i=0; i<board.length; i++){
            for (int j=0; j<board[0].length; j++){
                if (board[i][j] == 'R'){
                    
                    int[][] directions = {{-1,0},{1,0},{0,1},{0,-1}};
                    
                    for (int k=0; k<4; k++){
                        int new_i = i, new_j = j;
                        
                        new_i += directions[k][0];
                        new_j += directions[k][1];
                        
                        while (0<=new_i && new_i<8 && 0<=new_j && new_j<8){
                            if (board[new_i][new_j] == 'p'){
                                res += 1;
                                break;
                            }
                            else if(board[new_i][new_j] == 'B')
                                break;
                            new_i += directions[k][0];
                            new_j += directions[k][1];
                        }
                    }
                }
            }
        }
        
        return res;
    }
}
