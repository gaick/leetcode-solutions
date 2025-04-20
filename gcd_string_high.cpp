class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int len1 = str1.length();
        int len2 = str2.length();
        int len = gdc(len1,len2);
        if(len1%len!=0||len2%len!=0) return "";
        string c = str1.substr(0,len);
        for(int i = 0;i<len1;i = i+len){
            if(str1.substr(i,len)!=c) return "";
        }
        for(int j = 0;j<len2;j = j+len){
            if(str2.substr(j,len)!=c) return "";
        }
        return c;
    }
public:       
     int gdc(int a,int  b){
        return b == 0? a:gdc(b,a%b);
        }
};
