class Result {

    /*
     * Complete the 'sockMerchant' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY ar
     */

    public static int sockMerchant(int n, List<Integer> ar) {
    // Write your code here
    int count = 0;
    int[] pairedSocks = new int[0];
    
    mainLoop:
    for(int i = 0; i < ar.size(); i++){
        for(int k = 0; k < pairedSocks.length; k++){
            if(i==pairedSocks[k]){
                continue mainLoop;
            }
        }
        for(int j = i+1; j < ar.size(); j++){
            if(ar.get(i)==ar.get(j)){
                int[] newarr = new int[pairedSocks.length+1];
                for(int k = 0; k < pairedSocks.length; k++){
                    newarr[k] = pairedSocks[k];
                }
                newarr[pairedSocks.length] = j;
                count++; 
                pairedSocks = newarr;
                continue mainLoop;
            }
        }
    }
    return count;

    }

    

}
