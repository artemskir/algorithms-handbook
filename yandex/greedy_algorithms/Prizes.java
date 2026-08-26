import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Prizes {
    public static void main(String[] args) {
        int sweets = 0;

        Scanner scanner = new Scanner(System.in);
        sweets = scanner.nextInt();
        prizesDistribution(sweets);
    }

    public static void prizesDistribution(int sweets) {
        int countPlace = 0;
        while ((countPlace * (countPlace + 1)) / 2 <= sweets) {
            countPlace++;
        }
        countPlace--;

        System.out.println(countPlace);
    }

    public static void prizesDistributionWithPlaces(int sweets) {
        int countPlace = 0;
        while ((countPlace * (countPlace + 1)) / 2 <= sweets) {
            countPlace++;
        }
        countPlace--;
        int countPlaceOutput = countPlace;

        int[] placeSweets = new int[countPlace];

        for(int i = 0; i < countPlace; i++) {
            placeSweets[i] = i + 1;
        }
        placeSweets[countPlace - 1] += sweets - IntStream.of(placeSweets).sum();

        String sweetsPlacesOutput = Arrays.toString(placeSweets).replace(", ", " ");
        sweetsPlacesOutput = sweetsPlacesOutput.substring(1, sweetsPlacesOutput.length() - 1);
        System.out.println(countPlaceOutput);
        System.out.println(sweetsPlacesOutput);
    }
}
