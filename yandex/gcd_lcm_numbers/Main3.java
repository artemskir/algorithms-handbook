import java.util.Scanner;

public class Main3 {

    public long[] fibonacci(long n) {
        long last = 0;
        long current = 1;
        for (int i = 0; i < n; i++) {
            long temp = last + current;
            if (temp > n) {
                break;
            }
            last = current;
            current = temp;
        }
        return new long[]{last, current};
    }

    public static void main(String[] args) {
        Main3 mainInstance = new Main3();
         Scanner reader = new Scanner(System.in);
         long number = reader.nextLong();
         long[] output = mainInstance.fibonacci(number);
        System.out.println(output[0] + " " + output[1]);
    }
}