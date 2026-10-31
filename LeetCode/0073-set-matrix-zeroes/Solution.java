public class Solution {
    public int[][] setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean[] linhas = new boolean[m];
        boolean[] colunas = new boolean[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    linhas[i] = true;
                    colunas[j] = true;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (linhas[i] || colunas[j]) {
                    matrix[i][j] = 0;
                }
            }
        }

        return matrix;
    }
}
