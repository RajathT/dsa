class Solution {
    public int[] findErrorNums(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] res = new int[2]; int sum=0;
        for (int num: nums) {
            if (map.containsKey(num)) {
                res[0] = num;
            }
            else map.put(num, 1);
            sum+=num;
        }
        res[1] = ((nums.length * (nums.length+1)) / 2) - (sum-res[0]);
        
        return res;
    }
}
