import java.util.Scanner;
import java.util.*;

public class Solution {
    public static String getDay(String day, String month, String year) {
        Calendar cal = Calendar.getInstance();
        cal.set(Integer.valueOf(year), Integer.valueOf(month)-1, Integer.valueOf(day));
        
        int dayWeek = cal.get(Calendar.DAY_OF_WEEK);
        switch(dayWeek) {
            case Calendar.MONDAY: return "MONDAY";       
            case Calendar.TUESDAY: return "TUESDAY";       
            case Calendar.WEDNESDAY: return "WEDNESDAY";       
            case Calendar.THURSDAY: return "THURSDAY";       
            case Calendar.FRIDAY: return "FRIDAY";       
            case Calendar.SATURDAY: return "SATURDAY";       
            case Calendar.SUNDAY: return "SUNDAY";    
        }
        
        return "";
    }
        
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();
        
        System.out.println(getDay(day, month, year));
    }
}
