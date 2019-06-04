class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put('{','}');map.put('(',')');map.put('[',']');
        
        Stack<Character> stack = new Stack<>();
        
        for (char ch: s.toCharArray()){
            if (map.containsKey(ch)) stack.push(ch);
            else{
                if (stack.empty()) return false;
                else{
                    if (map.get(stack.peek()) == ch) stack.pop();
                    else return false;
                }
            }
        }
        return stack.empty();
    }
}
