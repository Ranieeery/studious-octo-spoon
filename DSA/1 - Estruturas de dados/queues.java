
import java.util.LinkedList;
import java.util.Queue;

public class Queues {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        queue.add(2);
        queue.add(3);

        System.out.println("Queue size: " + queue.size());
        System.out.println("Queue empty: " + queue.isEmpty());

        System.out.println(queue.remove());
        System.out.println(queue.remove());
        System.out.println(queue.remove());

        System.out.println("Queue size after removes: " + queue.size());
        System.out.println("Queue empty: " + queue.isEmpty());
    }
}