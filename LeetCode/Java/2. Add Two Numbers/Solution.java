class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int index = 0;
        ListNode head = new ListNode(0);
        ListNode node = head;

        while (l1  != null || l2  != null || index != 0) {
            int num1 = (l1 != null) ? l1.val : 0;
            int num2 = (l2 != null) ? l2.val : 0;

            int num = (num1 + num2 + index) % 10;
            index = (num1 + num2 + index) / 10;

            ListNode newNode = new ListNode(num);
            node.next = newNode;
            node = node.next;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        ListNode result = head.next;
        head.next = null;
        return result;
    }

    public void main(String[] args) {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        System.out.println(addTwoNumbers(l1, l2));
    }
}