from cgi import test
from glob import glob
import random
from re import X
from traceback import print_tb
import numpy
import pycuda.driver as cuda
import pycuda.gpuarray as gpuarray
import multiprocessing
import pycuda.autoinit
from scipy import stats
import scipy
import os
import time

maxp = 100000000.0
max = 100000000

def test(x):
    t = calc()
    return t

def calc(y: tuple) -> None:
    rand_array1 = random.uniform(0,0.1)
    rand_array2 = random.uniform(0,0.1)
    if rand_array1 * rand_array1 + rand_array2 * rand_array2 < 0.01:
        return 1
    return 0

def ensyuritu():
    return numpy.sum(multiprocessing.Pool().map(calc,zip(range(max), numpy.random.randint(0, 2 ** 32 -1, max))))

def call():
    callnumber = 100
    cn = 0
    countp = 0

    for cn in range(callnumber):
        countp += ensyuritu()
        print((cn + 1)*10,"億回",countp / (maxp * (cn + 1)) * 4)
        cn += 1

call()