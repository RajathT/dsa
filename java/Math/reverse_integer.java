class Solution {
    public int reverse(int x) {
        int result = 0;
        
        while (x!=0){
            int remainder = x%10;
            int new_number = result*10 + remainder;
            if ((new_number-remainder)/10!=result) return 0;
            result = new_number;
            x /= 10;
        }
        
        return result;
    }
}
