class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int max_length = 1;
        std::unordered_set<int> num_set(nums.begin(), nums.end());

        for (int num : num_set) {
            if (num_set.find(num - 1) == num_set.end()) {
                int streak = 1;

                while (num_set.find(num + streak) != num_set.end()) {
                    streak++;
                }

                max_length = std::max(max_length, streak);
            }
        }

        return max_length;
    }
};
