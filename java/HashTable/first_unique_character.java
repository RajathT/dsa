class Solution {
    public int firstUniqChar(String s) {
        if (s.length() == 0) return -1;
        
        int[] count_arr = new int[26];
        
        for (int i=0; i<s.length(); i++){
            count_arr[s.charAt(i)-97] ++;
        }
        int i=0, flag=0;
        for (; i<s.length(); i++){
            if (count_arr[s.charAt(i)-97] == 1) {flag=1; break;}
        }
        if (flag==1) return i;
        else return -1;
    }
}
