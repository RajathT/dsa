class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        
        int begin=0, end=0, res=0, counter=0;
        
        while (end<s.length()){
            char ch = s.charAt(end);
            if (!map.containsKey(ch)) map.put(ch, 1);
            else{
                map.put(ch, map.get(ch)+1);
                counter++;
            }
            end++;
        
            while (counter==1){
                ch = s.charAt(begin);
                if (map.containsKey(ch)) {
                    if (map.get(ch)>1){
                        map.put(ch, map.get(ch)-1);
                        counter--;
                    }
                    else map.remove(ch);
                }
                begin++;
            }  
            
            res = Math.max(res, end-begin);
        }
        
        return res;
        
    }
}
