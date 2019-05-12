class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        String string;
        
        if (A.length()==0) string = B;
        else if (B.length()==0) string = A;
        else string = A +" "+ B;
        
        Map<String, Integer> map = new HashMap<>();
        
        String[] words = string.split(" ");
        
        for (String word: words) {
            if (map.containsKey(word)) map.put(word, map.get(word)+1);
            else map.put(word, 1);
        }
        
        String res = "";
        
        for (Map.Entry<String, Integer> entry: map.entrySet()) if (entry.getValue()==1) res += entry.getKey()+" ";
        
        if (res.length()==0) return new String[0];
        else return res.split(" ");
    }
}
