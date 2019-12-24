public class HiWorld {

    public static void main(String[] args) {

        int a = 10;
        a = a++;                // Pointer conflict
        System.out.println(a);
    }
}