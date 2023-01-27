import numpy as np

def est_pixel_world(pixels, R_wc, t_wc, K):
    """
    Estimate the world coordinates of a point given a set of pixel coordinates.
    The points are assumed to lie on the x-y plane in the world.
    Input:
        pixels: N x 2 coordiantes of pixels
        R_wc: (3, 3) Rotation of camera in world
        t_wc: (3, ) translation from world to camera
        K: 3 x 3 camara intrinsics
    Returns:
        Pw: N x 3 points, the world coordinates of pixels
    """

    ##### STUDENT CODE START #####
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

    # return np.inv(H) @ np.inv(K)  @ p
    ##### STUDENT CODE END #####
    return new