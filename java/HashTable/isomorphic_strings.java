class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length()!=t.length()) return false;
        
        Map<Character, Character> map = new HashMap<>();
        
        for (int i=0; i<s.length(); i++){
            char ss = s.charAt(i);
            char tt = t.charAt(i);
            
            if (map.containsKey(ss)){
                if (map.get(ss)!=tt) return false;
            }
            else{
                if (map.containsValue(tt)) return false;
                else map.put(ss,tt);
            }
        }
        
        return true;
        
    }
}
