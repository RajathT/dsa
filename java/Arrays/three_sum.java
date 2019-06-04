class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i=0; i<nums.length-2; i++){
            int a = nums[i];
            int j = i+1, k = nums.length-1;
            while ((i>0 && nums[i]!=nums[i-1] || i==0) && j<k){
                while (j>i+1 && j<nums.length && nums[j]==nums[j-1]) j++;
                while (k<nums.length-1 && k>=0 && nums[k]==nums[k+1]) k--;
                if (j>=k) break;
                int b = nums[j], c = nums[k];
                int val = a+b+c;
                if (val==0) {res.add(Arrays.asList(a,b,c)); j++; k--;}
                else if (val<0) j++;
                else k--;
            }
        }
        return res;
    }
}
