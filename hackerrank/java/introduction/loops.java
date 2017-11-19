import java.util.*;
import java.io.*;
import java.lang.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            String result = "";
            for(int j=0; j < n; ++j) {
                int total = a;
                int acum = 0;
                for (int k=0; k < j+1; ++k) {
                    total += ((int)Math.pow(2, k)) * b;
                }
                
                result += "" + total + " ";
            }
            System.out.println(result);
        }
        
        in.close();
    }
}
