// https://leetcode.com/problems/move-zeroes/description/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                count++;
            } else if(count){
                int val = nums[i];
                nums[i] = 0;
                nums[i - count] = val;
            }
        }
    }
};
