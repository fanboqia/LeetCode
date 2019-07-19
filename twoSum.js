function twoSum(numbers,target){
    var map = {};
    var toFindMap = {};
    for(var i = 0; i < numbers.length; i++){
        var sub = target - numbers[i];

        if(toFindMap[numbers[i]] !== undefined){
            return [map[sub],i];
        }

        map[numbers[i]] = i;
        toFindMap[sub] = sub;
    }
}
