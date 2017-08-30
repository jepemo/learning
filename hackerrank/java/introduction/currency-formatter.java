import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        java.util.Currency zh = java.util.Currency.getInstance(Locale.CHINA);
        
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String india = NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
        
        NumberFormat chinaFmt = NumberFormat.getCurrencyInstance(Locale.CHINA);
            //chinaFmt.setCurrency(zh);
        
        String china = chinaFmt.format(payment);
        
        String france = NumberFormat.getCurrencyInstance(new Locale("fr", "FR")).format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
