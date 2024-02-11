// Definition for singly-linked list.
class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null;
    }
}

class Solution {
    hasCycle(head) {
        if (!head) return false; // 빈 리스트 처리

        let slow = head; // 느린 포인터
        let fast = head; // 빠른 포인터

        while (fast !== null && fast.next !== null) {
            slow = slow.next; // 한 번에 한 칸 이동
            fast = fast.next.next; // 한 번에 두 칸 이동

            if (slow === fast) {
                // 사이클 존재
                return true;
            }
        }

        // 사이클 없음
        return false;
    }
}

// 사용 예:
// const list = new ListNode(1);
// list.next = new ListNode(2);
// list.next.next = list; // 사이클 생성
// const solution = new Solution();
// console.log(solution.hasCycle(list)); // true 반환
