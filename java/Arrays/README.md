### CheatSheet
~~~java
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int row_length = A[0].length;
        for (int[] row: A){
            for (int i=0; i<(row_length+1)/2; i++){
                int temp = row[i] ^ 1;
                row[i] = row[row_length-i-1] ^ 1;
                row[row_length-i-1] = temp;
            }
        }
        return A;
    }
}
~~~
