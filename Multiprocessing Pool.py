from multiprococessing import popl


import time

def f(n):
    sum=0
    for n in range(1000):
              sum=n*n
    return sum

if __name__ == '__main__':
    t1=time.time()
    p= pool()
    results=p.map(f,range(1,10000))
    p.close()
    p.join()
    print("pool took :",time.time ()-t1)

    t2= time.time()
    results =[]
    for x in range(10000):
        results.append(f(n))


     print("serial processing took: ",time.time()-t2)
