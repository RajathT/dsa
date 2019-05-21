class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        Map<Character, Integer> map = new HashMap<>();
        for (char ch: p.toCharArray()) map.put(ch, map.getOrDefault(ch, 0)+1);
        int counter = map.size();
        
        int begin=0, end=0;
        List<Integer> list = new ArrayList<>();
        
        while (end<s.length()){
            char ch = s.charAt(end);
            if (map.containsKey(ch)){
                map.put(ch, map.get(ch)-1);
                if (map.get(ch)==0) counter--;
            }
            end++;
            
            while (counter==0){
                ch = s.charAt(begin);
                if (map.containsKey(ch)){
                    map.put(ch, map.get(ch)+1);
                    if (map.get(ch)==1) counter++;     
                }
                if(end-begin == p.length()){
                    list.add(begin);
                }
                begin++;
            }
        }
        return list;
    }
}
