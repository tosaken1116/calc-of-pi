import random
import numpy
import multiprocessing

maxp = 100000000.0
max = 100000000

def calc(y: tuple) -> None:
    if random.uniform(0,0.1) ** 2 + random.uniform(0,0.1) ** 2 < 0.01:
        return 1
    return 0

def ensyuritu():
    return numpy.sum(multiprocessing.Pool().map(calc,zip(range(max), numpy.random.randint(0, 2 ** 32 -1, max))))

def call():
    callnumber = 2
    cn = 0
    countp = 0

    for cn in range(callnumber):
        countp += ensyuritu()
        print((cn + 1)*10,"億回",countp / (maxp * (cn + 1)) * 4)
        cn += 1

call()