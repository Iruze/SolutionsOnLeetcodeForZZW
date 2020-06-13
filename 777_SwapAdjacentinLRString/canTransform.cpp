/*
思路分析： 题目的意思是说 ‘R’只能向右移动，并且只能移向’X’，‘L’只能向左移动，并且只能移向’X’。

第一：如果将start、end中的‘X’全部去掉得到的newStart 和 newEnd相等才有可能转换成功。
第二：如果start中'R'的左边'X'的个数超过在end中对应位置的'R'的左边'X'的个数，则不能转换成功，因为start中的'R'只能向右移动，右边的'X'只能增加不能减少
第三：如果end中'L'的左边'X'的个数超过在start中对应位置的'L'的左边'X'的个数，则不能转换成功，因为start中的'L'只能向左移动，左边的'X'只能减少不能增加

参考： 
作者：hestyle 
来源：CSDN 
原文：https://blog.csdn.net/qq_41855420/article/details/90044548 
版权声明：本文为博主原创文章，转载请附上博文链接
*/

class Solution {
public:
    bool canTransform(string start, string end) {
        int i = 0, j = 0;
        while(start[i] || end[j]) {
            while(start[i] == 'X')
                ++i;

            while(end[j] == 'X')
                ++j;

            if(start[i] != end[j])
                return false;

            if(start[i] == 'L' && i < j)
                return false;

            if(start[i] == 'R' && i > j)
                return false;
                
            if(start[i]) ++i;
            if(end[j]) ++j;
        }

        return true;
    }
};
