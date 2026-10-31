public class Solution {
    public int countPrimes(int n) {
        if (n < 3) return 0;

        boolean[] composto = new boolean[n];

        for (int i = 2; (long) i * i < n; i++) {
            if (composto[i]) continue;
            for (int j = i * i; j < n; j += i) {
                composto[j] = true;
            }
        }

        int count = 0;
        for (int k = 2; k < n; k++) {
            if (!composto[k]) count++;
        }
        return count;
    }
}