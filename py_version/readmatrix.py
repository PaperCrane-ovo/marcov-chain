import os
import sys
import numpy as np

class ReadMatrix:
    def __init__(self, filename,dimension=1)->None:
        '''
        filename: 矩阵文件名
        matrix: numpy矩阵,二维或更高
        dimension: 矩阵维度,对应n-1阶马尔可夫链
        '''
        self.filename = filename
        self.matrix = None
        self.dimension = dimension
    def read(self)->np.ndarray:
        if not os.path.exists(self.filename):
            print ("File does not exist")
            sys.exit()
        self.matrix = np.loadtxt(self.filename, dtype = np.float64)
        return self.matrix