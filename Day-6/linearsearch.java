import java.util.*;
class linearsearch{
    public static void main(String[] args) {
        int a[ ] = {12, 45, 67, 89};
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the element to be searched:");
        int n =sc.nextInt();    
        for(int i=0;i<a.length;i++)
        {
            if(n==a[i])
            {
                System.out.println(n+" is present at index "+i);
                break;
            }
            else{
                System.out.println("Element not found in arrray");
            }
        }

    }
}
        