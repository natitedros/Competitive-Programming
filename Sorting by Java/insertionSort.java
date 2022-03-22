public class insertionSort {
    public static void main(String[] args){
        int[] arr;
        arr = new int[]{3,5,2,8,6,9,1,4,7};
        for(int i = 0; i<arr.length; i++){
            for(int j = i; j>0; j--){
                if(arr[j-1] > arr[j]){
                    int a = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = a;      //inserting minimum values to the front 
                }
            }
        }
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
    } 
}
