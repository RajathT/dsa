class Solution {
    public int helper (int[] nums){
        if(nums.length==0) return 0;
        int temp[] = new int[nums.length+1];
        temp[0]= 0;
        temp[1]= nums[0];
        for(int i=2;i<temp.length;i++){
            temp[i]= Math.max(temp[i-1],temp[i-2]+nums[i-1]);
        }
        return temp[temp.length-1];
    }
    public int rob(int[] nums) {
        if(nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];
        int[] withFirstHouse = Arrays.copyOfRange(nums, 0, nums.length-1);
        int[] withLastHouse = Arrays.copyOfRange(nums, 1, nums.length);
        
        return Math.max(helper(withFirstHouse), helper(withLastHouse));
        
    }
}
