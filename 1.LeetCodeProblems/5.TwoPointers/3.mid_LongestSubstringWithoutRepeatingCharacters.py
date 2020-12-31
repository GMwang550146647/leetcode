"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb" , the answer is "abc" , which the length is 3.

Given "bbbbb" , the answer is "b" , with the length of 1.

Given "pwwkew" , the answer is "wke" , with the length of 3. Note that the answer must be a substring , "pwke" is a subsequence and not a substring.
"""
import time
class Solution():
    def __init__(self):
        self.num=19235713

    '''我的方法:居然比答案快'''
    def myFun(self,str):

        max_length = 0
        p_s = 0
        p_e = 1
        while p_e < len(str):
            if str[p_e] not in str[p_s:p_e]:
                p_e += 1
            else:
                tempt_length = p_e - p_s
                if tempt_length > max_length:
                    max_length = tempt_length
                p_s = str.index(str[p_e], p_s) + 1
                p_e = p_e + 1
        if p_e - p_s > max_length and len(str) != 0:  #len(str)!=0的情况是防止为空列表
            max_length = p_e - p_s
        return max_length

    '''答案方法1'''

    def lengthOfLongestSubstring(self, s) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        str='pwwkewoipdjlkafjldvbcmnbakhdkahfhakcmbvmw'
        self.testTime(self.myFun,args=(str,))
        self.testTime(self.lengthOfLongestSubstring,args=(str,))

if __name__=='__main__':
    SL=Solution()
    SL.main()