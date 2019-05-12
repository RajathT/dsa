class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph = paragraph.replaceAll("[^A-Za-z0-9\\s]"," ").toLowerCase();
        String[] words = paragraph.split(" ");
        Map<String, Integer> map = new HashMap<>();
        
        for (String word: words) map.put(word, map.getOrDefault(word, 0)+1);
        
        for (String ban: banned) map.remove(ban);
        if (map.containsKey("")) map.remove("");
        
        int max = Integer.MIN_VALUE;
        String res = "";
        for (Map.Entry<String, Integer> entry: map.entrySet()) {
            if(entry.getValue()>max){ 
                max=entry.getValue();
                res = entry.getKey();
            }
                
        }
        return res;
    }
}
