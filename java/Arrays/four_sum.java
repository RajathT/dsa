class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        while (i<nums.length-3){
            int j = i+1;
            while (((i>0 && nums[i]!=nums[i-1]) || i==0) && j<nums.length-2){
                int k = j+1, l = nums.length-1;
                while (((j>i+1 && nums[j]!=nums[j-1]) || j==i+1) && k<l){
                    while (k>j+1 && k<nums.length && nums[k]==nums[k-1]) k++;
                    while (l<nums.length-1 && l>=0 && nums[l]==nums[l+1]) l--;
                    if (k>=l) break;
                    int val = nums[i] + nums[j] + nums[k] + nums[l];
                    if (val == target) {res.add(Arrays.asList(nums[i],nums[j],nums[k],nums[l])); k++; l--;}
                    else if (val < target) k++;
                    else l--;
                }
                j++;
            }
            i++;
        }
        return res;
    }
}
