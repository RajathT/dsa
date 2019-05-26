class Solution {
    int start = 0, len = 0;
    
    public void helper(int i, int j, String s){
        while (i>=0 && j<s.length() && s.charAt(i) == s.charAt(j)){
            i--; j++;
            if (j-i-1 > len){
                start = i+1;
                len = j-i-1;
            }
        }
    }
    
    public String longestPalindrome(String s) {
        for (int i=0; i<s.length(); i++){
            helper(i,i,s);
            helper(i,i+1,s);
        }
        
        return s.substring(start, start+len);
    }
}
