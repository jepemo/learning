import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

static int B = -1;
static int H = -1;
static boolean flag = true;

static {
    Scanner scan = new Scanner(System.in);
    
    B = scan.nextInt();
    H = scan.nextInt();
    
    if (B <= 0 || H <= 0) {
        flag = false;
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class
