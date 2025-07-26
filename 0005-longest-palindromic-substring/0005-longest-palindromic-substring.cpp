class Solution {
public:
    bool is_palindrome(string s , int i , int j  ){
        if( j >= s.length() ) return false ; 
        while(i < j ){
            if(s[i] != s[j] ) return false ;
            i ++ ; j-- ; 
        }
        return true ; 
    }
    string longestPalindrome(string s) {
        int n = s.length() ; 
        // the worst case complexity of this is n ^ 3 as we know , if we find the answer for every subarray and check it
        // that it is palindrome or not ?? 
        // so the palindrome checking can be done using dp , by storing just previous two lenghths subarrays starting with each index  
        // the dp will give the complexity n ^ 2 and the memory will be n 

        // now another idea which comes into my mind is binary search it will give n^ 2 * log(n) ; 

        int lower = 1 , upper = n ; 
        pair<int,int>ans = {0,1} ;
        while(lower <= upper ){
            int mid = (upper + lower ) /2 ;
            bool found = false ;  
            for(int i = 0 ; i < n ; i++ ){
                if(is_palindrome(s,i,i+mid-2) ) {
                    found = true ;
                    ans = {i,mid-1} ; 
                    break ; 
                }
            }
            for(int i = 0 ; i < n ; i++ ){
                if(is_palindrome(s,i,i+mid-1) ) {
                    found = true ;
                    ans = {i,mid} ; 
                    break ; 
                }
            }
            if(found ) lower = mid+1 ;
            else upper = mid-1 ;
        }
        return s.substr(ans.first, ans.second);
    }
};