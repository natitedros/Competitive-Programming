public static List<Integer> countingSort(List<Integer> arr) {
    // Write your code here
    int minVal = arr.get(0);
    int maxVal = arr.get(0);
    for(int i = 0; i<arr.size(); i++){      
            if(arr.get(i)>maxVal){
                maxVal = arr.get(i);
            }
            if(arr.get(i)<minVal){
                minVal = arr.get(i);
            }
        }
    int[] counter = new int[maxVal - minVal + 1];
    for(int i = minVal; i <=  maxVal; i++){     
            for(int j = 0; j < arr.size(); j++){
                if(i == arr.get(j)){
                    counter[i-minVal]++;
                    continue;
                }
            }
    }
    ArrayList<Integer> sortedArr = new ArrayList<Integer>();
    for(int i = 0; i < counter.length; i++){        
            if(counter[i]==0){
                continue;
            }
            for(int j = 0; j < counter[i]; j++){
                sortedArr.add(i + minVal);
            } 
         }
         return sortedArr;
    }
