class Solution {
    public String reverseWords(String s) {
        
        String[] words = s.split(" ");
        
        for (int k=0; k<words.length; k++){
            int i=0, j=words[k].length()-1;
            char[] temp = words[k].toCharArray();
            while (i<j){
                char ch = temp[i];
                temp[i] = temp[j];
                temp[j] = ch;
                i++;j--;
            }
            words[k] = String.valueOf(temp);
        }
        
        return String.join(" ", words);
    }
}
