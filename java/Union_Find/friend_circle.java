class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    
    public int findCircleNum(int[][] M) {
        for (int i=0; i<M.length; i++){
            for (int j=0; j<M[0].length; j++){
                if (M[i][j]==1) union(i,j);
            }
        }
        
        Set<Integer> set = new HashSet<>();
        
        for (int key: map.keySet())
            set.add(find(key));
        
        return set.size();
    }
    
    public int find(int i){
        if (map.get(i)!=i) map.put(i, find(map.get(i)));
        return map.get(i);
    }
    
    public void union(int i, int j){
        if (!map.containsKey(i)) map.put(i,i);
        if (!map.containsKey(j)) map.put(j,j);
        
        int parent1 = find(i);
        int parent2 = find(j);
        
        if (parent1 != parent2)
            map.put(parent1,parent2);
    }
    
}
