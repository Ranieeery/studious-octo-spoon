public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int total = 0;
        int controle = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                controle++;

                total = controle >= total ? controle : total;
            } else {
                controle = 0;
            }
        }

        return total;
    }
}