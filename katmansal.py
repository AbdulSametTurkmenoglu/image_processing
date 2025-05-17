import numpy as np
import matplotlib as pyplot

def yogunluk(p,g):
    J=p-g    
    return np.clip(J,0,1)   ,

def yogunluk2(p,g):
    J=2*p-g    
    return np.clip(J,0,1)       

def yogunluk3(p,g):
    J=np.abs(p-g)    
    return np.clip(J,0,1)     

def yogunluk5(p,g):
    J=p*g    
    return np.clip(J,0,1)     

def yogunluk6(p,g):
    J=np.sqrt(p*g)    
    return np.clip(J,0,1)     
    
def büyükletme(I1,I2): 
    H,W,_=I1.shape
    J=np.zeros((H,W,3))
    for y in range(H):
        for x in range(W):
            for c in range(3):
                if I1[y,x,c]>I2[y,x,c]:
                   J[y,x,c]=I1[y,x,c]
                else:
                   J[y,x,c]=I2[y,x,c]
    return J   

def küçükletme(I1,I2):
   H,W,_=I1.shape
   J=np.zeros((H,W,3))
   for y in range(H):
       for x in range(W):
           for c in range(3):
               if I1[y,x,c]<I2[y,x,c]:
                  J[y,x,c]=I1[y,x,c]
               else:
                  J[y,x,c]=I2[y,x,c]
   return J          


def rastgele_birlestirme(I1,I2,r=0.5):
    H,W,_=I1.shape
    J=np.zeros((H,W,3))
    for y in range(H):
        for x in range(W):
            if np.random.random()<r:
                J[y,x,:]=I1[y,x,:]
            else:
                J[y,x,:]=I2[y,x,:]
    return J        

def add(I1,I2,a=1):
    J = I1*a+I2*(1-a)
    return J


def gecmeli(I1,I2,kH=1,kW=1):
    H,W,_=I1.shape
    dy = H/kH 
    dx = W/kW
    J=np.zeros((H,W,3))
    for y in range(H):
        for x in range(W):
            if (int(y/dy)+int(x/dx))%2==0:
                J[y,x,:]=I1[y,x,:]
            else:
                J[y,x,:]=I2[y,x,:]
    return J        
     
           
def gecisli(I1,I2):
    H,W,_=I1.shape
    J=np.zeros((H,W,3))
    for y in range(H):
        for x in range(W):
            f = x/(W-1)
            J[y,x,:]=I1[y,x,:]*f+(1-f)*I2[y,x,:]
                
    return J           
                
            