# 有几个线程就用几个信号量，最先开始的信号量初始化为1，其他初始化为0，然后根据条件判断实现同步

import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.Zero = threading.Semaphore(1)
        self.Even = threading.Semaphore(0)
        self.Odd = threading.Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.Zero.acquire()
            printNumber(0)
            if i & 1 == 0:
                self.Odd.release()
            else:
                self.Even.release()
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i & 1 == 1:
                self.Even.acquire()
                printNumber(i + 1)
                self.Zero.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i & 1 == 0:
                self.Odd.acquire()
                printNumber(i + 1)
                self.Zero.release()
