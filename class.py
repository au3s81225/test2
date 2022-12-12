import time
"""
class 家庭():
    def __init__(self, 名字, 在幹嘛): #會先把__init__執行一遍
        self.名字 = 名字
        self.在幹嘛 = 在幹嘛 #物件本身(self),屬性(.名字/.在幹嘛),外部參數(名字/在幹嘛)
    
    def 現在(self, now = time.ctime()): #  now = 為預設值
        print("[" + now + "]" + "時" + self.名字 + "在" + self.在幹嘛)

a = 家庭("張智凱", "熬夜打code") #建立一個物件
a.現在()
"""                
"""
class Bank_acount:
    @property  # 讓以下的code只能讀取無法變更
    def password(self):
        return '密碼:123'
a = Bank_acount()
print(a.password) #後面還有沒看完
"""
        

