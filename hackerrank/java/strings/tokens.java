import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        
        s = s.trim();
        
        if (s.length() > 400000) {
            System.out.println("");
        }
        else if (s.length() == 0) {
            System.out.println("0");
        }
        else {
            //String[] splitted = s.split("[A-Za-z !,\\?\\._'@]+");
            //String[] splitted = s.split("[ ',\\?!@\\._]+");
            String[] splitted = s.split("[^A-Za-z]+");
            System.out.println(splitted.length);
            for (String ss: splitted) {
                System.out.println(ss);
            }
        }
        scan.close();
    }
}
