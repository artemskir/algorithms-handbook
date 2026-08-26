import java.util.List;
import java.util.stream.Collectors;

public class Coins {
    static int count = 0;

    public static void countCombinations(int target, List<Integer> coins, int index) {
        if (target == 0) {
            count++;
            return;
        }
        if (target < 0 || index >= coins.size()) return;

        int coin = coins.get(index);

        countCombinations(target, coins, index + 1);

        if (target >= coin) {
            countCombinations(target - coin, coins, index);
        }
    }

    public static void printCombinations(int target, List<Integer> coins, int index, List<Integer> path, StringBuilder output) {
        if (target == 0) {
            output.append(path.size()).append(" ")
                    .append(path.stream().map(String::valueOf).collect(Collectors.joining(" ")))
                    .append("\n");
            return;
        }
        if (target < 0 || index >= coins.size()) return;

        int coin = coins.get(index);

        printCombinations(target, coins, index + 1, path, output);

        if (target >= coin) {
            path.add(coin);
            printCombinations(target - coin, coins, index, path, output);
            path.remove(path.size() - 1);
        }
    }
}
