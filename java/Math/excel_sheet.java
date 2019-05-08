class Solution {
    public int titleToNumber(String s) {
        int res=0, n = s.length()-1;
        for (int i=n; i>=0; i--)
            res += (Math.pow(26, n-i))*((int)s.charAt(i)-64);
        return res;
    }
}
