class Solution {
    public int rob(int[] nums) {
        if(nums.length==0)
            return 0;
        int temp[] = new int[nums.length+1];
        temp[0]= 0;
        temp[1]= nums[0];
        for(int i=2;i<temp.length;i++){
            temp[i]= Math.max(temp[i-1],temp[i-2]+nums[i-1]);
        }
        return temp[temp.length-1];
    }
}
