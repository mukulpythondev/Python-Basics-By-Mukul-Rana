# In this module we learn how to run multiple function at same time 
import time 
import asyncio
from  concurrent.futures import ThreadPoolExecutor
async  def func1():
    time.sleep(1)
    print("Func1")
async def func2():
    time.sleep(1)
    print("Func2")
async def func3():
    time.sleep(4)
    print("Func3")
#async def main():
 #   await func1()
  #  await func2()
   # await func3()
#asyncio.run(main())
async def main():
    k=asyncio.gather(# isse ye upar wale se fast chalte h 
        func1(),
        func2(),        
        func3())
    print(k)
asyncio.run(main())
# now learn  thread pool executor 

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()
