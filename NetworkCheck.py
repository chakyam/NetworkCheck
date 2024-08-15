import threading
import requests
import time
import winsound

class Checker():
    def __init__(self):
        self.count=0
        
    def network(self):
        try:
            requests.get('https://www.baidu.com', timeout=5)
            return True
        except requests.exceptions.RequestException:
            return False

    def beep(self):
        for _ in range(3):
            for _ in range(3):
                winsound.Beep(3000,200)
                time.sleep(0.2)
            time.sleep(0.8)

    def check(self):
        now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if self.network():
            self.count=0
            with open(r'checker.log','a') as log:
                log.write(f'{now} 网络正常\n')
            return True
        else:
            self.count+=1
            with open(r'checker.log','a') as log:
                log.write(f'{now} 网络断开\n')
            if self.count == 3:
                self.count-=1
                self.beep()
            return False

    def main(self):
        winsound.Beep(2000,200)
        if self.check():
            timer = threading.Timer(600, self.main)
            timer.start()
        else:
            timer = threading.Timer(60, self.main)
            timer.start()

c=Checker()
c.main()
