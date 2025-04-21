class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_candy = 0;
        for(int i : candies){
            max_candy = max(i,max_candy);
        }
        vector<bool> result(candies.size());
        for(int i = 0;i < candies.size(); i++){
            result[i] = (candies[i] + extraCandies >= max_candy);
        }
        return result;
    }
};
