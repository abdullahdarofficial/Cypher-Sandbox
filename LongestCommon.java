public class LongestCommon {
    public String longestCommonPrefix(String[] s){
        for(int i = 0; i< s[0].length(); i++){
            char c = s[0].charAt(i);
            for(int j = 1; j < s.length; j++){
                if(s[j].charAt(i) != c || i > s[j].length()){
                    return s[0].substring(0, i);
                }
            }
        }
        return s[0];
    }
}
