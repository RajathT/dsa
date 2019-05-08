class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");
        
        int i = 0, j = s.length()-1;
        
        while (i<j && s.charAt(i) == s.charAt(j)){
            i++; j--;
        }
        
        if (i<j) return false;
        else return true;
    }
}
