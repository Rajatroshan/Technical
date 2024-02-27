https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&status=solved&sortBy=submissions
class Solution
{
    static int majorityElement(int a[], int size)
    {
       
         int candidate = -1;
    int count = 0;
     for(int i=0;i<size;i++){
         if(count==0){
             candidate=a[i];
             count=1;
         }else if(candidate==a[i]){
             count++;
         }else{
             count--;
         }
     }
     count=0;
     for(int i=0;i<size;i++){
         if(a[i]==candidate){
             count++;
         }
     }
     if(count>size/2){
         return candidate;
     }else{
         return -1;}

    }
}