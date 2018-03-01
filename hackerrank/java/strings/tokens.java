import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        //String[] splitted = s.split("[A-Za-z !,\\?\\._'@]+");
        String[] splitted = s.split("[ ',\\?!@\\._]+");
        System.out.println(splitted.length);
        for (String ss: splitted) {
            System.out.println(ss);
        }
        // Write your code here.
        scan.close();
    }
}
