class Solution {
    public String countAndSay(int n) {
        StringBuilder val = new StringBuilder("1");
        for (int i=1; i<n; i++){
            char prev = val.charAt(0); int count = 1; StringBuilder temp = new StringBuilder();
            for (int j=1; j<val.length(); j++){
                if (val.charAt(j) == prev) count++;
                else{
                    temp.append(count).append(prev);
                    prev = val.charAt(j); count = 1;
                }
            }
            val = temp.append(count).append(prev);
        }
        return val.toString();
    }
}
