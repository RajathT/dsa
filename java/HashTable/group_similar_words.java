class Solution {
    public int numSpecialEquivGroups(String[] A) {
        Set<String> set= new HashSet<>();
        for (String s: A){
            int[] odd_letters = new int[26];
            int[] even_letters = new int[26];
            for (int i=0; i<s.length(); i++){
                if (i%2==1) odd_letters[s.charAt(i)-'a']++;
                else even_letters[s.charAt(i)-'a']++;
            }
            String full= Arrays.toString(odd_letters)+Arrays.toString(even_letters);
            set.add(full);
        }
        return set.size();
    }
}
