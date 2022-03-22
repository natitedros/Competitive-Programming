public class BubbleSort {
    public static void main(String[] args){
        int[] arr;
        arr = new int[]{7,6,8,4,9,2,4,3,1};
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr.length - 1; j++){
                if(arr[j] > arr[j+1]){
                    int a = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = a;
                    
                }
            }
    
        }
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
        
    }
}
