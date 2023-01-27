import numpy as np

def est_Pw(s):
    Pw=np.array([[-s/2, -s/2, 0],
                 [ s/2, -s/2, 0],
                 [ s/2,  s/2, 0],
                 [-s/2,  s/2, 0]])


    return Pw
