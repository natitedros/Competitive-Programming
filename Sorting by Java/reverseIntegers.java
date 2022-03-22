class Solution {
    public int reverse(int x) {
        long rev1 = 0;
        int rem;
        boolean overload = false;
        while(x!=0){
            rem = x % 10;
            rev1 = rev1*10 + rem;
            x = x/10;
            if ((rev1<-Math.pow(2,31))||(rev1>(Math.pow(2,31)-1))){
                overload = true;
                break;
            }
        }
        if (overload){
            return 0;
        }
        else{
            int rev = (int) rev1;
            return rev;
        }
        
    }
}
