public class selectionSort {
    public static void main(String[] args){
        int[] arr;
        arr = new int[]{3,5,2,8,6,9,1,4,7};
        for(int i = 0; i < arr.length; i++){
            for(int j = i+1; j < arr.length; j++){
                int val = arr[i];      //passing the initial array value of index i for the variables
                int spot = i;
                if(val>arr[j]){
                    val = arr[j];      //saving and holding the minimum value of the iteration for the place of i
                    spot = j;
                }
                arr[spot] = arr[i];    //exchanging the values
                arr[i] = val;
            }
        }
    }
}
