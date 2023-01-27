from est_homography import est_homography
import numpy as np

def PnP(Pc, Pw, K=np.eye(3)):
    """
    Solve Perspective-N-Point problem with collineation assumption, given correspondence and intrinsic

    Input:
        Pc: 4x2 numpy array of pixel coordinate of the April tag corners in (x,y) format
        Pw: 4x3 numpy array of world coordinate of the April tag corners in (x,y,z) format
    Returns:
        R: 3x3 numpy array describing camera orientation in the world (R_wc)
        t: (3, ) numpy array describing camera translation in the world (t_wc)

    """

    ##### STUDENT CODE START #####
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


    ##### STUDENT CODE END #####

    return R, t