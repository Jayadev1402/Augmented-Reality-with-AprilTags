import numpy as np

def est_pixel_world(pixels, R_wc, t_wc, K):

    R_wc=R_wc.T
    t_wc1 = -R_wc@t_wc

    H=np.zeros((3,3))
    H[:,:-1]=R_wc[:,:-1]
    H[:,-1]=t_wc1.flatten()

    p=np.ones((pixels.shape[0],3))
    p[:,:2]=pixels[:]

    new=np.linalg.inv(K@H)  @ p.T
    new=new.T
    # print(new)
    new=new/new[:,-1].reshape(-1,1)
    new[:,-1]=0


    return new
