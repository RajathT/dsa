class Solution {
    public boolean wordPattern(String pattern, String str) {
        char[] pat = pattern.toCharArray();
        String[] s = str.split(" ");
        
        if (pat.length != s.length) return false;
        
        Map<Character, String> map = new HashMap<>();
        
        for (int i=0; i<pat.length; i++){
            if (map.containsKey(pat[i])){
                if (!map.get(pat[i]).equals(s[i])) 
                    return false;
            }
            else{
                if (map.containsValue(s[i])) return false;
                else map.put(pat[i], s[i]);
            }
        }
        
        return true;
    }
}
