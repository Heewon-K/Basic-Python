def add(x, y):
    return x+y 

def sigma(limit=10):
    s = 0 
    for i in range(1, limit+1):
        s +=i 
    return s 

class MyCalc:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
    def add(self):
        return self.x + self.y    
    def sub(self):
        return self.x - self.y    
    
if __name__ == "__main__":
    print( __name__ ) # 시스템이 제공하는 내부변수  __main__
    print( add(4,5) )
    print( sigma() )
    print( sigma(100))

    calc = MyCalc(7,8)
    print( calc.add() )
    print( calc.sub() )


