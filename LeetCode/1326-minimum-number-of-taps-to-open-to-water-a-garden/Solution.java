class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] alcance = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            int inicio = Math.max(0, i - ranges[i]);
            int termino = Math.min(n, i + ranges[i]);
            alcance[inicio] = Math.max(alcance[inicio], termino);
        }

        int abertas = 0;
        int fim = 0;
        int melhor = 0;

        for (int x = 0; x < n; x++) {
            melhor = Math.max(melhor, alcance[x]);

            if (x == fim) {
                if (melhor <= x) return -1;

                abertas++;
                fim = melhor;
            }
        }

        return abertas;
    }
}