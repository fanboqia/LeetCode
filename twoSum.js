function twoSum(numbers,target){
    var numToIndex = {};
    var numAnother = {};
    for(var i = 0; i < numbers.length; i++){
        // another number to find
        var sub = target - numbers[i];

        //has the another number been registered
        if(numAnother[numbers[i]] !== undefined){
            return [numToIndex[sub],i];
        }

        //register current number with its index
        numToIndex[numbers[i]] = i;
        //register the another number
        numAnother[sub] = sub;
    }
    return [];
}
