import java.util.Deque;
import java.util.ArrayDeque;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Deque<Integer> pilha = new ArrayDeque<>();

        for (int i = 0; i < temperatures.length; i++) {
            while (!pilha.isEmpty() && temperatures[i] > temperatures[pilha.peek()]) {
                int dia = pilha.pop();
                answer[dia] = i - dia;
            }
            pilha.push(i);
        }

        return answer;
    }
}
