class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length==0||intervals.length==1) return intervals;
        
        Arrays.sort(intervals, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                return a[0]-b[0];
            }
        });
        
        List<int[]> res = new ArrayList<int[]>();
        
        int j=1;
        res.add(intervals[0]);
        
        while (j<intervals.length){
            int[] curr = res.get(res.size()-1);
            int[] next = intervals[j];
            
            if (curr[1] >= next[0]){
                res.set(res.size()-1, new int[]{curr[0], Math.max(curr[1], next[1])});
            }
            else res.add(next);
            
            j++; 
        }
        
        return res.toArray(new int [res.size()][]);
    }
}
