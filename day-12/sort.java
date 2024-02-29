class Solution {
    boolean arraySortedOrNot(int[] arr, int n) {
        for(int i=1;i<n;i++){                 //loop go at last of the element 
            if(arr[i]<arr[i-1]){             //if the number is less than from the previous number then it will return false
                return false;
            }
        }
        return true;                  //otherwise true
    }
}