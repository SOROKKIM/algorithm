import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {

        String result;

        int sizeOfStacks = 4; //스택의 개수
        ArrayList<Stack<Integer>> stacks = new ArrayList<>();
        Scanner sc = new Scanner(System.in);


        //순열의 길이 N 입력 받기
        int N = sc.nextInt();
        //순열의 원소 1이상 N 이하의 서로 다른 정수 공백으로 입력 받기
        sc.nextLine();
        //입력 받은 순열들의 요소를 가진 배열
        String[] elements = sc.nextLine().split(" ");

        //4개의 Stack 초기화
        for (int i = 0; i < sizeOfStacks; i++) {
            stacks.add(new Stack<>());
            stacks.get(i).push(0);
        }

        //결과 가져오기
        result = getResult(N, elements, sizeOfStacks, stacks);
        System.out.print(result);

    }
    public static String getResult(int N, String[] elements, int sizeOfStacks, ArrayList<Stack<Integer>> stacks) {
        int element;

        for (int i = 0; i < N; i++) {
            element = Integer.parseInt(elements[i]);

            for (int j = 0; j < sizeOfStacks; j++) {
                if(stacks.get(j).peek() < element) {
                    stacks.get(j).push(element);
                    element = 0;
                    break;
                }
            }
            if(element != 0) {
                return "NO";
            }
        }
        return "YES";
    }

}
