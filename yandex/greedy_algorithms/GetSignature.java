import java.util.*;
import java.util.stream.Collectors;

public class GetSignature {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int countSegments = scanner.nextInt();
        ArrayList<ArrayList<Integer>> borders = new ArrayList<>();

        for (int i = 0; i < countSegments; i++) {
            ArrayList<Integer> bordersLocal = new ArrayList<>();
            bordersLocal.add(scanner.nextInt());
            bordersLocal.add(scanner.nextInt());
            borders.add(bordersLocal);
        }

        Collections.sort(borders, new Comparator<ArrayList<Integer>>() {
            @Override
            public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
                return Integer.compare(o1.get(1), o2.get(1));
            }
        });

        ArrayList<Integer> points = new ArrayList<>();

        for (ArrayList<Integer> border : borders) {
            boolean flag = false;
            for (Integer point : points) {
                if (border.getFirst() <= point) {
                    flag = true;
                    break;
                }
            }
            if (flag) continue;
            points.add(border.get(1));
        }
        System.out.println(points.size());
        System.out.println(points.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(" ")));
    }
}
