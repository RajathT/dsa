class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length==1 || nums.length==0) return nums.length;
        
        int begin=1, end=1, prev=nums[0];
        
        while (end<nums.length){
            if (nums[end] != prev){
                int temp = nums[end];
                nums[end] = nums[begin];
                nums[begin] = temp;
                begin++; prev = temp;
            }
            end++;
        }
        
        return begin;
    }
}
