import java.util.*;

public class RobberMaxValue {

    public double robberMaxValue(ExersiceInput exersiceInput) {
        ArrayList<ArrayList<Double>> valueProducts = new ArrayList<>();

        for (ArrayList<Integer> arr: exersiceInput.products) {
            double value = arr.get(0) * ((double) 1 / arr.get(1));
            valueProducts.add(new ArrayList<>(Arrays.asList(value, arr.get(1).doubleValue())));
        }

        valueProducts.sort((a, b) -> Double.compare(b.get(0), a.get(0)));

        double maxValue = 0;
        for (ArrayList<Double> product : valueProducts) {
            if (product.get(1) > exersiceInput.volumeBackpack && exersiceInput.volumeBackpack != 0) {
                maxValue += product.get(0) * exersiceInput.volumeBackpack;
                exersiceInput.volumeBackpack = 0;
            } else if (exersiceInput.volumeBackpack != 0 && product.get(1) <= exersiceInput.volumeBackpack) {
                maxValue += product.get(0) * product.get(1);
                exersiceInput.volumeBackpack -= product.get(1);
            }
        }
        return maxValue;
    }

    public static void main(String[] args) {
        ExersiceInput exersiceInput = new ExersiceInput();
        Scanner scanner = new Scanner(System.in);
        exersiceInput.count = scanner.nextInt();
        exersiceInput.volumeBackpack = scanner.nextInt();

        for (int i = 0; i < exersiceInput.count; i++) {
            exersiceInput.products.add(new ArrayList<>(Arrays.asList(scanner.nextInt(), scanner.nextInt())));
        }

        RobberMaxValue main = new RobberMaxValue();
        String output = String.valueOf(Math.floor(main.robberMaxValue(exersiceInput) * 1000 +.5) / 1000);
        if (output.endsWith(".0")) {
            System.out.println(output + "00");
        } else {
            System.out.println(output);
        }
    }
}

class ExersiceInput {
    public int count;
    public int volumeBackpack;
    public ArrayList<ArrayList<Integer>> products = new ArrayList<>();
}