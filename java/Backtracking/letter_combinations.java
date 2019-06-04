class Solution {
    public List<String> helper(List<String> combos, int index, String temp, List<String> res){
        if (index == combos.size()){
            res.add(temp); return res;
        }
        
        for (char ch: (combos.get(index)).toCharArray()){
            temp += ch;
            helper(combos, index+1, temp, res);
            temp = temp.substring(0, temp.length()-1);
        }
        return res;
    }
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return new ArrayList<String>();
        
        Map<Character, String> map = new HashMap<>();
        map.put('2',"abc");map.put('3',"def");map.put('4',"ghi");map.put('5',"jkl");
        map.put('6',"mno");map.put('7',"pqrs");map.put('8',"tuv");map.put('9',"wxyz");
        List<String> combos = new ArrayList<>();
        for (char ch: digits.toCharArray()) combos.add(map.get(ch));
        
        return helper(combos, 0, "", new ArrayList<String>());
    }
}
