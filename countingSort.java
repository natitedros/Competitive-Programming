public class countingSort {
    public static void main(String[] args){
        int[] arr;
        int[] counter;            //array to represent of the frequency of elements at arr[]
        arr = new int[]{3,5,2,8,6,9,1,4,7};
        int maxValue = arr[0];
        int minValue = arr[0];
        for(int i = 0; i<arr.length; i++){       //fonding the minimum and maximum values of the main array to find range of counter array
            if(arr[i]>maxValue){
                maxValue = arr[i];
            }
            if(arr[i]<minValue){
                minValue = arr[i];
            }
        }
        counter = new int[maxValue - minValue + 1];   //declaring the counter array
        
        for(int i = minValue; i <=  maxValue; i++){     //iterating through the arrays to record the frequencies of all the elements
            for(int j = 0; j < arr.length; j++){
                if(i == arr[j]){
                    counter[i-minValue]++;
                    continue;
                }
            }
        } 
        for(int i = 0; i < counter.length; i++){        //printing out the sorted values using the frecuency counter array
            if(counter[i]==0){
                continue;
            }
            for(int j = 0; j < counter[i]; j++){
                System.out.println(i + minValue);
            }
             
        }
    }
}
