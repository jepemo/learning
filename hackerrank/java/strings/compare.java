import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        List<String> subs = new ArrayList<String>();
        for (int i=0; i <= s.length()-k; ++i) {
            String sub = s.substring(i, i+k);
            //System.out.println(sub);
            subs.add(sub);
        }
        
        Collections.sort(subs);
        smallest = subs.get(0);
        largest = subs.get(subs.size()-1);
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
