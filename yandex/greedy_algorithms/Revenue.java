import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Revenue {

    //3 - n
    //2 3 9 - prices
    //7 4 2 - clicks

    public void calcRevenue(int count, ArrayList<Long> prices, ArrayList<Long> clicks) {
        Collections.sort(prices);
        Collections.sort(clicks);
        long maxSum = 0;
        for (int i = 0; i < count; i++) {
            maxSum += prices.get(i) * clicks.get(i);
        }
        System.out.println(maxSum);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        ArrayList<Long> prices = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            prices.add(scanner.nextLong());
        }
        ArrayList<Long> clicks = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            clicks.add(scanner.nextLong());
        }
        Revenue revenue = new Revenue();
        revenue.calcRevenue(count, prices, clicks);
    }
}
