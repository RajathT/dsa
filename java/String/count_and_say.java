class Solution {
    public String countAndSay(int n) {
        String val = "1";
        for (int i=1; i<n; i++){
            char prev = val.charAt(0); int count = 1; String temp="";
            for (int j=1; j<val.length(); j++){
                if (val.charAt(j) == prev) count++;
                else{
                    temp += count + "" + prev;
                    prev = val.charAt(j); count = 1;
                }
            }
            val = temp + "" + count + "" + prev;
        }
        return val;
    }
}
