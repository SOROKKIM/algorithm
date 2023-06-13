//선형 자료구조 - 큐


import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        LinkedList<Integer> deque = new LinkedList<Integer>();

        int count = 0; //2번, 3번 연산 횟수 누적 카운트

        int N = sc.nextInt(); //큐의 크기(1~N)
        int M = sc.nextInt(); //뽑으려는 숫자의 개수

        //1~N까지 덱에 담기
        for (int i = 1; i <= N; i++) {
            deque.offer(i);
        }

        int[] select = new int[M]; //뽑고자 하는 수를 담은 배열

        for (int i = 0; i < M; i++) {
            select[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {


            int goal_index = deque.indexOf(select[i]); //덱에서 뽑고자 하는 숫자의 위치(index)
            int half_index; // 덱의 중간 지점

            /*
            * 현재 덱의 원소가 짝수 개라면 중간 지점을 현제 덱의 절반 크기에서 -1 감소 시킨다.
            * {1, 2, 3, 4}일떼, 2를 중간지점으로 하면 인덱스는 1이기 때문
            */

            if (deque.size() % 2 == 0) {
                half_index = deque.size() / 2 - 1;
            } else {
                half_index = deque.size() / 2;
            }

            //중간 지점 또는 중간 지점보다 원소의 위치가 앞에 있을 경우 -> 2번 연산이 더 이득
            if (goal_index <= half_index) {
                // 2번 연산 : 목표 원소보다 앞에 있는 원소들을 모두 뒤로 보낸다.
                for (int j = 0; j < goal_index; j++) {
                    int num = deque.pollFirst();
                    deque.offerLast(num);
                    count++;
                }
            } else { //중간 지점보다 원소의 위치가 뒤에 있는 경우 -> 3번 연산이 더 이득
                // 3번 연산 : 목표 원소를 포함한 뒤쪽에 있는 원소들을 모두 앞으로 보낸다.
                for (int j = 0; j < deque.size() - goal_index; j++) {
                    int num = deque.pollLast();
                    deque.offerFirst(num);
                    count++;
                }
            }
            deque.pollFirst(); //연산 끝나고 맨 앞 원소를 삭제
        }
        System.out.println(count);
    }
}
