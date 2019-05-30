class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String res = strs[strs.length-1];
        
        for (String str: strs){
            while (!str.startsWith(res) && !res.equals("")){
                res = res.substring(0, res.length()-1);
            } 
        }
        return res;
    }
}
