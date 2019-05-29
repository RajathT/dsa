class Solution {
    public int romanToInt(String s) {
        if (s.length()==0) return 0;
        
        Map<Character, Integer> map = new HashMap<>();
        map.put('I',1); map.put('V',5); map.put('X',10); map.put('L', 50); map.put('C',100); map.put('D',500); map.put('M',1000);
        
        int prev = map.get(s.charAt(s.length()-1)), res = map.get(s.charAt(s.length()-1));
        
        for (int i = s.length()-2; i>=0; i--){
            int val = map.get(s.charAt(i));
            if (val < prev) res -= val;
            else res += val;
            prev = val;
        }
        
        return res;
    }
}
