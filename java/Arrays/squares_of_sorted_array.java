class Solution {
    public int[] sortedSquares(int[] A) {
        int[] res = new int[A.length];
        int a = 0, b = A.length-1;
        
        for (int i= A.length-1; i>=0; i--){
            if (Math.abs(A[a]) > Math.abs(A[b])){
                res[i] = A[a]*A[a]; a++;
            }
            else{
                res[i] = A[b]*A[b]; b--;
            }
        }
        return res;
    }
}
