package Day-5;

class Solution {

    
    // a: input array
    // n: size of array
    // Function to find equilibrium point in the array.
    public static int equilibriumPoint(long arr[], int n) {
         int leftsum=0;              //initislizing ttwo value leftsum & sum
         int sum=0;
         for(int i=0;i<n;i++)        //starting a for loop that will calculate the sum value 
         {
             sum+=arr[i];     
         } 
         for(int i=0;i<n;i++)        //initializing the loop that would be count one by one
         {   
             sum-=arr[i];            //it will subtract the total sum from the element
             if(sum==leftsum)        //if the left sum value and the sum is equal then it will return the i+1 value
             {
                 return i+1;
             }
             leftsum+=arr[i];        //assign the left sum value that will be arr[i] value
         }
         return -1;
    }
}
