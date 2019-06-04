class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int i = 0, smallest_val = nums[0]+nums[1]+nums[2]; 
        while(i<nums.length-2){
            int j = i+1, k = nums.length-1;
            while (j<k){
                int val = nums[i] + nums[j] + nums[k];
                if (Math.abs(val-target) < Math.abs(smallest_val-target)) {smallest_val = val;}
                else if (val < target) j++;
                else k--;
            }
            i++;
        }
        return smallest_val;
    }
}
