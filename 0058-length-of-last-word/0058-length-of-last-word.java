class Solution {
    public int lengthOfLastWord(String s) {
        String space = " ";
        String[] array = s.split(" ");
        int last = array.length-1;
        return array[last].length();
    }
}