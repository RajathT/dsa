class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        String s = "";

        for (int i=0; i<str.length(); i++){
            char ch = str.charAt(i);
            if (Character.isDigit(ch) || ch == '-' || ch == '+') {
                if (i==0 && (ch == '-' || ch == '+')) s += ch;
                else if (Character.isDigit(ch)) s+=ch;
                else break;
            }
            else break;
        }
        
        if (s.equals("") || s.equals("-") || s.equals("+")) return 0;
        
        int res = 0, sign = 1;
        
        for (char ch: s.toCharArray()){
            if (ch == '-') sign = -1;
            else if (ch == '+') sign = 1;
            else{
                int val = Integer.parseInt(String.valueOf(ch));
                res = res * 10 + (val);
                if (res % 10 != val) {
                    if (sign == 1) return (int)Math.pow(2,31);
                    else return -(int)Math.pow(2,31)-1;
                }
            }
        }
        
        return res * sign;
    }
}
