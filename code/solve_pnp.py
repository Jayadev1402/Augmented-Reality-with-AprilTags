from est_homography import est_homography
import numpy as np

def PnP(Pc, Pw, K=np.eye(3)):

    # Homography Approach

    pw=Pw[:,:-1]
    H=est_homography(pw,Pc)
    p_prime = np.linalg.inv(K)@H
    s=p_prime[:,2].copy()
    p_prime[:,2] = np.cross(p_prime[:,0],p_prime[:,1])
    
    # Following slides: Pose from Projective Transformation
    [U,S,V_prime] = np.linalg.svd(p_prime)
    R=U@np.array([[1,0,0],[0,1,0],[0,0,np.linalg.det(U@V_prime)]])@V_prime
    t=(s/np.linalg.norm(p_prime[:,0]))
    R=np.linalg.inv(R)
    t=(-R@t).flatten()



    return R, t
