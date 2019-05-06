class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<Integer>();
        for (int i=left; i<=right; i++)
            if (helper(i)) res.add(i);
        
        return res;
    }
    
    public boolean helper(int val){
        int temp = val;
        while (temp>0){
            int remainder = temp%10;
            if (remainder == 0 || (val%remainder)>0)
                return false;
            temp /= 10;
        }
        return true;
    }
    
}
