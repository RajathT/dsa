class Solution {
    public boolean isSubsequence(String s, String t) {
        int fromIndex = 0;
        for (char c : s.toCharArray()) {
            fromIndex = t.indexOf(c, fromIndex);
            if (fromIndex++ < 0) return false;
        }
        return true;
    }
}
