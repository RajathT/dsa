class Solution {
    public int numJewelsInStones(String J, String S) {
        if (J.length()==0 || S.length()==0) return 0;
        
        Map<Character, Integer> map = new HashMap<>();
        for (char jewel: J.toCharArray()) map.put(jewel, 0);
        for (char stone: S.toCharArray()) if (map.containsKey(stone)) map.put(stone, map.get(stone)+1);
        
        int res = 0;
        for (char key: map.keySet()) res+=map.get(key);
        
        return res;
    }
}
