function twoSum(numbers,target){
    var map = {}
    for(var i in numbers){
        var sub = target - numbers[i];

        if(typeof map[numbers[i]] == 'number'){
            return [Number(map[target - numbers[i]]),Number(i)];
        }

        map[numbers[i]] = i;
        map[sub] = sub;
    }
}
