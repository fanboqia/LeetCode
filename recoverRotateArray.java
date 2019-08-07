public class Solution {
    /**
     * @param nums: An integer array
     * @return: nothing
     */
    public void recoverRotatedSortedArray(List<Integer> nums) {
        // write your code here
        if(nums == null){
            return;
        }
        //find the place of unordered
        int index = -1;
        int num_size = nums.size();
        List<Integer> part1 = new ArrayList<Integer>();
        List<Integer> part2 = new ArrayList<Integer>();
        for(int i = 0; i < num_size - 1; i++){
            Integer num1 = nums.get(i);
            Integer num2 = nums.get(i+1);
            if(num1 > num2){
                index = i;
            }
        }
        //already sorted
        if(index == -1){
            return;
        }
        for(int i = 0; i <= index; i++){
            part1.add(nums.get(i));
        }
         for(int i = index+1; i < num_size; i++){
            part2.add(nums.get(i));
        }
        int part1Size = part1.size();
        int part2Size = part2.size();
        for(int i = 0; i < part2Size; i++){
            nums.set(i,part2.get(i));
        }
        for(int i = 0; i < part1Size; i++){
            nums.set(part2Size+i,part1.get(i));
        }
    }
}
