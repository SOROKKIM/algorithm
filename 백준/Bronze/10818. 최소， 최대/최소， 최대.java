import java.util.Arrays;
import java.util.Scanner;

public class Main {

    //선형 자료구조 - 배열 (Array)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //정수의 개수
        int N;
        N = sc.nextInt();
        //입력받은 N개의 정수
        int[] num = new int[N];
        for (int i = 0; i < N; i++) {
            num[i] = sc.nextInt();
        }


        Arrays.sort(num); // 배열을 오름차순으로 정리해주는 메소드
        //최솟값
        int minNum = num[0];

        //최댔값
        int maxNum = num[N - 1];

        System.out.print(minNum+" "+maxNum);
    }
}
