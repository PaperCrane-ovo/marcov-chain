import os
import sys
import numpy as np

class ReadMatrix:
    def __init__(self, filename):
        self.filename = filename
        self.matrix = None
    def read(self)->np.ndarray:
        if not os.path.exists(self.filename):
            print ("File does not exist")
            sys.exit()
        self.matrix = np.loadtxt(self.filename, dtype = np.float64)
        return self.matrix