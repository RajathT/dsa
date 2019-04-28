class Solution {
    public int fib(int N) {
        if (N == 0)
            return 0;
        else if (N == 1)
            return 1;
        else{
            int a = 0, b = 1, temp;
            for (int i=2; i<=N; i++){
                temp = b;
                b = a + b;
                a = temp;
            }
            return b;
        }
    }
}
