import numpy as np
def P3P(Pc, Pw, K=np.eye(3)):



    p1=Pw[0,:]
    p2=Pw[1,:]
    p3=Pw[2,:]

    a=np.linalg.norm(p2-p3)
    b=np.linalg.norm(p1-p3)
    c=np.linalg.norm(p1-p2)

    j1=np.zeros((3,))
    j2=np.zeros((3,))
    j3=np.zeros((3,))

    j1[:2]=(Pc[0,:2] - K[:2,-1])
    j2[:2]=(Pc[1,:2] - K[:2,-1])
    j3[:2]=(Pc[2,:2] - K[:2,-1])


    j1[2]=K[0,0]/2 + K[1,1]/2
    j2[2]=K[0,0]/2 + K[1,1]/2
    j3[2]=K[0,0]/2 + K[1,1]/2


    j1=j1/np.linalg.norm(j1)
    j2=j2/np.linalg.norm(j2)
    j3=j3/np.linalg.norm(j3)

    j1=j1.flatten()
    j2=j2.flatten()
    j3=j3.flatten()

    ca=np.dot(j2,j3)
    cb=np.dot(j1,j3)
    cg=np.dot(j1,j2)


    A4 = np.power((a*a-c*c)/(b*b) - 1, 2) - (4*c*c*ca*ca)/(b*b)
    A3 = 4*(((a*a-c*c)/(b*b))*(1-(a*a-c*c)/(b*b))*cb - (1-(a*a+c*c)/(b*b))*ca*cg + (2*c*c*ca*ca*cb)/(b*b) )
    A2 = 2*(np.power((a*a-c*c)/(b*b),2)- 1+(2*np.power((a*a-c*c)/(b*b),2))*cb*cb + 2*(b*b-c*c)/(b*b)*ca*ca - 4*((a*a+c*c)/(b*b))*ca*cb*cg + (2*(b*b-a*a)/(b*b)*cg*cg ))
    A1 = 4*(((a*a-c*c)/(b*b))*(1+(a*a-c*c)/(b*b))*(-1*cb) - (1-(a*a+c*c)/(b*b))*ca*cg + (2*a*a*cg*cg*cb)/(b*b) )
    A0 = np.power(((a*a-c*c)/(b*b)+1),2) - (4*a*a*cg*cg)/(b*b)
    # print(A4,A3,A2,A1,A0)

    root=np.roots([A4,A3,A2,A1,A0 ])

    temp=root.astype(str)
    real_val=[]
    for i in range(len(temp)):
        if '0j' in temp[i]:
          if float(temp[i][1:-4])>0:
            real_val.append(float(temp[i][1:-4]))
    root=np.array(real_val)

    

    if len(root)==1:
      u = np.zeros(1)
    elif len(root)==2:
      u = np.zeros(2)

    for i in range(len(root)):
        u[i] = ((-1+(a*a-c*c)/(b*b))*np.power(root[i],2) - 2 * (a*a-c*c)/(b*b) * cb * root[i]+ 1 + (a*a-c*c)/(b*b)) / (2 * (cg - ca * root[i]))
    # print(u)
    s1=np.sqrt((c*c)/(1+u*u-2*u*cg))
    s2=u*s1
    s3=root*s1
    # print(s1,s2,s3)
    s=[s1,s2,s3]
    # print(s)
    if len(root)==2:
      x=s[0][0]*j1
      y=s[1][0]*j2
      z=s[2][0]*j3

      x1=s[0][0]*j1
      y1=s[0][1]*j2
      z1=s[0][1]*j3
      Pc=np.array([x,y,z])
      Pc1=np.array([x1,y1,z1])
      print('Pc : ',Pc)
      print('Pc1 : ',Pc1)
      R, t = Procrustes(Pc, Pw[0:-1,:])
      R1, t1 = Procrustes(Pc1, Pw[0:-1,:])
 
      if np.linalg.norm(R@Pw[-1,:]+t-Pc[-1,:])>np.linalg.norm(R1@Pw[-1,:]+t1-Pc[-1,:]):
        return R,t
      else:
        return R1,t1
      
    elif len(root)==1:
      x=s[0][0]*j1
      y=s[1][0]*j2
      z=s[2][0]*j3

    
      Pc=np.array([x,y,z])

      R, t = Procrustes(Pc, Pw[0:-1,:])


  
    return R, t
def Procrustes(X, Y):


    X_mean=np.sum(X,axis=0)/X.shape[0]
    Y_mean=np.sum(Y,axis=0)/Y.shape[0]

    X_new = np.transpose(X-X_mean)
    Y_new = np.transpose(Y-Y_mean)

    U, l, V = np.linalg.svd(X_new @ Y_new.T)

    S=np.zeros((3,3))
    S[0,0]=1
    S[1,1]=1
    S[2,2]= np.linalg.det(V.T @ U.T)

    R=U@S@V
    R=R.T
 
    t = Y_mean - R @ X_mean

    return R, t

