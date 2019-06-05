class Solution {
    int first(int[] nums, int target){
        int i=0, j=nums.length-1, ans=-1;
        
        while (i<=j){
            int mid = (i+j)/2;
            if (nums[mid]==target) ans = mid;
            
            if (nums[mid]<target) i=mid+1;
            else j=mid-1;
        }
        
        return ans;
    }
    
    int last(int[] nums, int target){
        int i=0, j=nums.length-1, ans=-1;
        
        while (i<=j){
            int mid = (i+j)/2;
            if (nums[mid]==target) ans = mid;
            
            if (nums[mid]<=target) i=mid+1;
            else j=mid-1;
        }
        
        return ans;
    }
    public int[] searchRange(int[] nums, int target) {
        return new int[]{first(nums, target), last(nums, target)};
    }
}
