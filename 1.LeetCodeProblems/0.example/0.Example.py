
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,s):
        pass
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
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
