class Solution {
    public int solution(String s) {
         String[] a = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < 10; i++) {
            s = s.replace(a[i], Integer.toString(i));
        }
        int answer = Integer.parseInt(s);
        return answer;
    }
}