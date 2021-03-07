
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun1(self,s):
        for i in range(10000000):
            a=10000**2
    def myFun2(self,s):
        for i in range(10000000):
            a=100000000**0.5
    '''答案方法1'''

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        s='dfkljal'
        self.testTime(self.myFun1,args=(s,))
        self.testTime(self.myFun2,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
