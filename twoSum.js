function twoSum(numbers,target){
    var map = {}
    for(var i in numbers){
        var sub = target - numbers[i];

        if(map[numbers[i]] == 'find'){
            return [Number(map[target - numbers[i]]),Number(i)];
        }

        map[numbers[i]] = i;
        map[sub] = 'find';
    }
}
