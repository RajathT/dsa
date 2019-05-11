class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    int res = 0;
    
    public int find(int x){
        if (map.get(x) != x) map.put(x,find(map.get(x)));
        return map.get(x);
    }
    
    public void union(int i, int j){
        
        int parent1 = find(i);
        int parent2 = find(j);
        
        if (parent1 != parent2) {
            map.put(parent1, parent2);
            res--;
        }
        
    }
    
    public int numIslands(char[][] grid) {
        if (grid.length==0) return 0;
        
        int L = grid.length, W = grid[0].length; 
        
        for (int i=0; i<L; i++){
            for (int j=0; j<W; j++){
                if (grid[i][j]=='1'){
                    map.put(i*W+j, i*W+j); 
                    res++;
                }
            }
        }
        
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        
        for (int i=0; i<L; i++){
            for (int j=0; j<W; j++){
                if (grid[i][j]=='1'){
                    for (int[] dir: dirs){
                        int new_i = i+dir[0], new_j = j+dir[1];
                        if (new_i>=0 && new_j>=0 && new_i<L && new_j<W && grid[new_i][new_j]=='1') {
                            union(i*W+j, new_i*W+new_j);
                        }     
                    }
                }
            }
        }
        
        return res;
    }
}
