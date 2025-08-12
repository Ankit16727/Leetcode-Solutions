class Solution {
public:
    bool isPalindrome(int x) {
        bool p ; 
        if (x < 0){
            p = false;
        }else if(x >= 0 && x < 10){
            p = true; 
        }else{
            unsigned int x2 = x ; 
            unsigned int pn = 0 ; 
            int k = 1; 

            while (k){
                
                int digit = x2 % 10 ;  
                pn = pn * 10 + digit ;

                x2 = x2 / 10; 

                if (x2 == 0){
                    k  = 0;
                } ; 

                
            }; 
            

            p = x == pn ? true : false ; 

        } ; 
        return p; 
    }
};