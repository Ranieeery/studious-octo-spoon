public class Solution {
    public int maxProfit(int[] prices) {
        int lowest = Integer.MAX_VALUE;
        int answer = 0;

        for (int i = 0; i < prices.length; i++) {
            lowest = prices[i] < lowest ? prices[i] : lowest;

            answer = prices[i] - lowest > answer ? prices[i] - lowest : answer;
        }

        return answer;
    }
}