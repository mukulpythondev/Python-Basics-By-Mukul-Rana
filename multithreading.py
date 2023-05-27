import threading
import time
def sleeping(seconds):
    print(f"the function is sleeping for {seconds}")
    time.sleep(seconds)
time1=time.perf_counter()#ye current time bteyga
#Normal code 
sleeping(1)
sleeping(2)
sleeping(4)
time2= time.perf_counter()
net_time=time2-time1#ye bta dega kitna time laga 3 function ko run karne m 
print(net_time)
#code using threading 
time3= time.perf_counter()
t1=threading.Thread(target=sleeping, args=[1])
t2=threading.Thread(target=sleeping, args=[2])
t3=threading.Thread(target=sleeping, args=[4])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
#calculation of time
time4=time.perf_counter()
net_threading_time=time4-time3
print(net_threading_time)