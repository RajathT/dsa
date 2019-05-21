class Solution {
    public int maxProfit(int[] prices) {
        int max_val = 0, min_val = Integer.MAX_VALUE;
        
        for (int price: prices){
            min_val = Math.min(price, min_val);
            max_val = Math.max(max_val, price-min_val);
        }
        
        return max_val;
    }
}
