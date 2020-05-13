import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        scan.useDelimiter("\r\n");
        
        int i = Integer.valueOf(scan.next());
        double d = Double.valueOf(scan.next());
        String s = scan.next();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
