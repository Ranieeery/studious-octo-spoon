import java.util.Deque;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public boolean isValid(String s) {
        Deque<Character> pilha = new ArrayDeque<>();
        Map<Character, Character> foo = new HashMap<>();
        foo.put(')', '(');
        foo.put(']', '[');
        foo.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (foo.containsKey(c)) {
                if (pilha.isEmpty()) return false;
                
                char topo = pilha.pop();

                if (topo != foo.get(c)) return false;
            } else {
                pilha.push(c);
            }
        }
        return pilha.isEmpty();
    }
}
