class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length<=1) return points.length;
        
        Arrays.sort(points, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                return a[1]-b[1];
            }
        });
        
        int res=1, end=points[0][1];
        for (int i=1; i<points.length; i++){
            if (end>=points[i][0]) continue;
            else{
                res++; end = points[i][1];
            }
        }
        
        return res;
    }
}
