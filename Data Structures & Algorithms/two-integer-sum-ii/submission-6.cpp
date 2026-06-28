class Solution {
   public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        if (numbers.empty()) {
            return {};
        }

        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int value = numbers[left] + numbers[right];

            if (value == target) {
                return {left + 1, right + 1};
            }
            if (value < target) {
                left++;
            }
            if (value > target) {
                right--;
            }
        }
    }
};
