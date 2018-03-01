import java.io.*;
import java.util.*;

public class Solution {

    static Map<String, Integer> getFrequencies(String a) {
        Map<String, Integer> freqA = new HashMap<String, Integer>();
        for (char ch: a.toCharArray()) {
            String chStr = ("" + ch).toUpperCase();
            if (!freqA.containsKey(chStr)) freqA.put(chStr, 0);
            freqA.put(chStr, freqA.get(chStr)+1);
        }
        return freqA;
    }

    static Set<String> getAllKeys(Map<String, Integer> freqA, Map<String, Integer> freqB) {
        Set<String> allKeys = new HashSet<String>();
        
        allKeys.addAll(freqA.keySet());
        allKeys.addAll(freqB.keySet());
        
        return allKeys;
    }

    static boolean isAnagram(String a, String b) {
        Map<String, Integer> freqA = getFrequencies(a);
        Map<String, Integer> freqB = getFrequencies(b);
        
        boolean eq = true;
        Set<String> allKeys = getAllKeys(freqA, freqB);
        for (String key: allKeys) {
            if (!freqA.containsKey(key) || !freqB.containsKey(key)) {
                eq = false;
                break;
            }
            
            int valA = freqA.get(key);
            int valB = freqB.get(key);
            
            if (valA != valB) {
                eq = false;
                break;
            }
        }
        
        return eq;  
    }
    
     public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
