class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_candy = *max_element(candies.begin(),candies.end());
        vector<bool> result(candies.size());
        transform(candies.begin(),candies.end(),result.begin(),[max_candy,extraCandies](int i){
            return i + extraCandies >= max_candy;
        });
        return result;
    }
};
