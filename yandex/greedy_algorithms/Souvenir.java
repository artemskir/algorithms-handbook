import java.util.*;

public class Souvenir {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int countSouvenirs = scanner.nextInt();
        int budget = scanner.nextInt();
        ArrayList<Integer> souvenirs = new ArrayList<>();

        for (int i = 0; i < countSouvenirs; i++) {
            souvenirs.add(scanner.nextInt());
        }
        Collections.sort(souvenirs);
        System.out.println(maxSouvenirs(budget, souvenirs));
    }

    public static int maxSouvenirs(int budget, ArrayList<Integer> souvenirs) {
        int sumSouvenirs = 0;
        while (budget >= 0) {
            if (souvenirs.get(0) == 0) {
                sumSouvenirs++;
                souvenirs.remove(0);
            } else if (souvenirs.get(0) <= budget) {
                sumSouvenirs++;
                budget -= souvenirs.get(0);
                souvenirs.remove(0);
            } else {
                break;
            }
        }
        return sumSouvenirs;
    }

}