class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        
        String prefix = strs[0];
        
        for (String str: strs){
            while (!str.startsWith(prefix) && !prefix.equals("")){
                prefix = prefix.substring(0,prefix.length()-1);
            }    
        }
        
        return prefix;
        
    }
}
