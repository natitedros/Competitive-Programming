    int sum = 0;
    int toyNumber = 0;
    int minVal = prices.get(0);
    int position = 0;
    for(int i = 0; i < prices.size(); i++){
        for(int j = 0; j < prices.size(); j++){
            minVal = prices.get(0);
            position = 0; 
            if(minVal > prices.get(j)){
                minVal = prices.get(j);
                position = j;
            }
        }
        sum += minVal;
        prices.remove(position);
        if(sum < k){
            toyNumber++;
        }
        else{
            break;
        }
    }
    return toyNumber;

    }
