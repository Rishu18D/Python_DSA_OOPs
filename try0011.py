from time import sleep, ctime
def loop():
    print'start loop 0 at:',ctime()
    sleep(4)
    print'loop 0 done at:',ctime()
    def loop():
        print(