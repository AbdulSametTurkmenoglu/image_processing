import numpy as np
import matplotlib as pyplot

def euclid(I,a): 
    H,W,_=I.shape
    J=np.zeros((H,W,3))
    for v in range(H):
        for u in range(W):
            x,y,_=np.dot(np.linalg.inv(a),np.array([u,v,1]))
            if 0<=x<W and 0<=y<H:
               J[v,u,:]=I[int(y),int(x),:]
            else:
                J[v,u,:]=0
            
    return J      

def similarity(I,a): 
    H,W,_=I.shape
    J=np.zeros((H,W,3))
    for v in range(H):
        for u in range(W):
            x,y,_=np.dot(np.linalg.inv(a),np.array([u,v,1]))
            if 0<=x<W and 0<=y<H:
               J[v,u,:]=I[int(y),int(x),:]
            else:
                J[v,u,:]=0
            
    return J     

    
def affine(I,a):
    H,W,_=I.shape
    J=np.zeros((H,W,3))
    for v in range(H):
        for u in range(W):
            x,y,_=np.dot(np.linalg.inv(a),np.array([u,v,1]))
            if 0<=x<W and 0<=y<H:
               J[v,u,:]=I[int(y),int(x),:]
            else:
                J[v,u,:]=0
            
    return J     

def transform_matrix(xy,uv): 
    tranform =np.dot(uv,np.linalg.inv(xy)) 
    return tranform
    


    

    