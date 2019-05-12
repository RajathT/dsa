class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse_codes = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        Set<String> set = new HashSet<>();
        
        for (String word: words){
            char[] letters = word.toCharArray();
            StringBuilder code = new StringBuilder();
            for (char letter: letters) code.append(morse_codes[letter - 97]);
            set.add(code.toString());
        }
        return set.size();
    }
}
