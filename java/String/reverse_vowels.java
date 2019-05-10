class Solution {
    public String reverseVowels(String s) {
        int i=0, j=s.length()-1;
        char[] temp = s.toCharArray();
        
        while (i<j){
            while (i<temp.length && !("aeiouAEIOU").contains(""+temp[i])) i++;
            
            while (j>=0 && !("aeiouAEIOU").contains(""+temp[j])) j--;
            
            if (i<j){
                char ch = temp[i];
                temp[i] = temp[j];
                temp[j] = ch; 
                i++; j--;
            }
        }
        
        return new String(temp);
    }
}
