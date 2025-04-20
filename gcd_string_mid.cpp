class Solution {
public:
    string gcdOfStrings(string str1, string str2) {

        if(str1 + str2 != str2 + str1)  return "";
        return str1.substr(0,gdc(str1.length(),str2.length()));
    }
public:       
     int gdc(int a,int  b){
        return b == 0? a:gdc(b,a%b);
        }
};
