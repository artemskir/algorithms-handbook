import java.util.*;

public class Billboards {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int countBillboards = scanner.nextInt();
        int countAdvertisers = scanner.nextInt();
        int countWeeks = scanner.nextInt();
        ArrayList<Offer> offers = new ArrayList<>();

        for (int i = 0; i < countAdvertisers; i++) {
            Offer offer = new Offer(scanner.nextInt(), scanner.nextInt(), i);
            offers.add(offer);
        }
        Collections.sort(offers);

       int place = countBillboards * countWeeks;
       int result = 0;
       for (Offer offer : offers) {
           if (place > 0) {
                int amount = Math.min(offer.weeks, place);
               result += offer.payment * amount;
               place -= amount;
           }
       }
       System.out.println(result);
    }

    private static class Offer implements Comparable<Offer> {
        public Offer(int payment, int weeks, int id) {
            this.payment = payment;
            this.weeks = weeks;
            this.id = id;
        }

        public int payment;
        public int weeks;
        public int id;

        @Override
        public int compareTo(Offer other) {
            return other.payment - this.payment;
        }
    }
}
