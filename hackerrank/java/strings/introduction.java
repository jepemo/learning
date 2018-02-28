import java.io.*;
import java.util.*;

public class Solution {
    
    public static String capitalize(String input) {
        return input.substring(0, 1).toUpperCase() + input.substring(1, input.length());
    }

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        System.out.println(A.length() + B.length());
        if (A.compareTo(B) > 0) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
        
        String result = capitalize(A) + " " + capitalize(B);
        System.out.println(result);
    }
}
