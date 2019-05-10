class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int i=0;
        for (; i<nums.length; i++){
            if (map.containsKey(nums[i])) break;
            else map.put(target-nums[i], i);
        }
        return new int[]{i, map.get(nums[i])};
    }
}
