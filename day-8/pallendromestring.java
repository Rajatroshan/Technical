class Solution {
    int isPalindrome(String S) {
        
        for(int i=0;i<S.length()/2;i++)   //The for loop will be go to the half of the length of the string
        {
            int n = S.length();  
            if(S.charAt(i)!=S.charAt(n-1-i))    //it will check that the first character and the last character same or not
            {
                return 0;    //if not same it returns 0
            }
        }
        return 1;           //other wise it will return 1
    }
}