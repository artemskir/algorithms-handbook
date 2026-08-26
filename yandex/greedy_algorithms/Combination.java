import java.util.*;

public class Combination {

    public ArrayList<Integer> minimumSum(int money) {
        ArrayList<Integer> combination = new ArrayList<>();
        while (money > 0) {
            if (money >= 50) {
                combination.add(50);
                money -= 50;
            } else if (money >= 20) {
                combination.add(20);
                money -= 20;
            } else if (money >= 10) {
                combination.add(10);
                money -= 10;
            } else if (money >= 5) {
                combination.add(5);
                money -= 5;
            } else if (money >= 1) {
                combination.add(1);
                money -= 1;
            }
        }
        return combination;
    }

    public static void main(String[] args) {
        Combination mainInstance = new Combination();
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> combination = mainInstance.minimumSum(scanner.nextInt());
        StringBuilder stringBuilder = new StringBuilder();
        for (Integer number : combination) {
            stringBuilder.append(number);
            stringBuilder.append(" ");
        }
        System.out.println(combination.size());
        System.out.println(stringBuilder);
    }
}