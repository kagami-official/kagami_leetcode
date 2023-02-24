import java.util.HashMap;
import org.junit.Test;

/*
 * @Author: Alice
 * @Date: 2023-02-24 19:13:20
 * @LastEditors: Alice
 * @LastEditTime: 2023-02-24 20:22:33
 * @Description: 
 */
class problem_1{
    public static void main(String[] args) {
        test01();
    }
    @Test
    public static void test01(){
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        Solution s = new Solution();
        System.out.println(s.twoSum(nums,target));
       
    }
};

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        // for(int i=0; i<nums.length; i++) {
        //     map.put(nums[i], i);
        // }
        int[] ans = new int[] {};
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (map.containsKey(complement)){
                ans = new int[] {map.get(complement), i};
                if (ans[0]>ans[1]){
                    ans = new int[] {i,map.get(complement)};
                }
                return ans;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
}