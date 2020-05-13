import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
   //private static String tagChars = "[\\p{Print}^<^>]+";
   private static String tagChars = "[A-Za-z0-9\\ ]+";
   private static Pattern pattern = Pattern.compile("<(" + tagChars + ")>(.+?)</(" + tagChars + ")>");
    
   public static List<String> ParseLine(String input) {
       List<String> result = new ArrayList<String>();
       
       Matcher matcher = pattern.matcher(input);
       while (matcher.find()) {
           String oTag = matcher.group(1);
           String content = matcher.group(2);
           String eTag = matcher.group(3);
           //System.out.println("<" + oTag + ">" + content + "</" + eTag + ">");
           
           if (oTag.equals(eTag)) {
               result.add(matcher.group(2));
           }
           else {
               result.add("Nothing");
           }
       }
       
       return result;
   } 
    
    
   public static void main(String[] args){
      
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases>0){
         String line = in.nextLine();
         
         List<String> results = ParseLine(line);
         for (String res: results) {
             System.out.println(res);
         }
         
         testCases--;
      }
   }
}
