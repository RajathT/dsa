class Solution {
    public String check(char[] digits){
        int sum = 0;
        for (char digit: digits) sum+=Math.pow(Integer.parseInt(String.valueOf(digit)),2);
        char[] sum_val = Integer.toString(sum).toCharArray();
        Arrays.sort(sum_val);
        return new String(sum_val);
    }
    public boolean isHappy(int n) {
        
        char[] digits = Integer.toString(n).toCharArray();
        Set<String> set = new HashSet<>();
        
        while (true){
            String val = check(digits);
            System.out.println(val);
            if (val.equals("1")) return true;
            else if (set.contains(val)) return false;
            else{
                set.add(val);
                digits = val.toCharArray();
            }
        }
    }
}
