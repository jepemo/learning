import java.io.*;
import java.util.*;

public class Solution {

    public static String reverse(String in) {
        return new StringBuilder(in).reverse().toString();
    }
    
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        
        String rev = reverse(A);
        
        if (A.equals(rev)) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
