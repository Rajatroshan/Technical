import java.util.*;
class year
{
    //creating another method
    static void year(int number_of_days){         
        int years = number_of_days / 365;     //calculate the year
        int remaining_days = number_of_days % 365; //remainder days 
        int months = remaining_days / 30;  //calculate the month
        int days = remaining_days % 30;  //calculate the days
        
        //printing the year,month,days
        System.out.println("years :"+years);   
        System.out.println("months :"+months);
        System.out.println("Days :"+days);
       
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Number of Days: ");
        int num=sc.nextInt();
        year(num);  //calling function
    }
}