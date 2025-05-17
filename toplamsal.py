import numpy as np
import matplotlib.pyplot as plt

def dondurme(I,A):
    H,W=I.shape
    a = A*np.pi/180
    J = np.zeros(I.shape)
    x0 , y0 = W/2 , H/2  
    for v in range(H):
        for u in range(W):
            x = int((u-x0)*np.cos(a)+(v-y0)*np.sin(a)+x0)
            y = int(-(u-x0)*np.sin(a)+(v-y0)*np.cos(a)+y0)
            if 0<=x<W and 0<=y<H:
               J[v,u] = I[y,x] 
    return J

def radon(I): #sadece doğruları yakalar
    H,W=I.shape
    x0 , y0 = W/2 , H/2  
    t = np.zeros((I.shape[0],180))
    for A in range(180):
        a = A*np.pi/180
        J = np.zeros(I.shape)
        for v in range(H):
            for u in range(W):
                x = int((u-x0)*np.cos(a)+(v-y0)*np.sin(a)+x0)
                y = int(-(u-x0)*np.sin(a)+(v-y0)*np.cos(a)+y0)
                if 0<=x<W and 0<=y<H:
                   J[v,u] = I[y,x]
        t[:,A] = np.sum(J,axis=1)
     
    return t


def hough_line(I):
    H,W=I.shape
    x0 , y0 = W/2 , H/2  
    J = np.zeros(I.shape)
    R = np.sqrt(H*2+W*2)
    t = np.zeros((int(R),180))
    r0 =R/2
    for y in range(H):
        for x in range(W):
            if I[y,x]==1:
                for A in range(180):
                    a = A*np.pi/180-np.pi/2
                    r= int((x-x0)*np.cos(a)+(y-y0)*np.sin(a)+r0)
                    if 0<=r<R:
                       t[r,A]+=1
    return t


def hough_circle(I):
    H,W=I.shape
    t = np.zeros((H,W,30))
    for y in range(H):
        for x in range(W):
            for r in range(8,30):
                for A in range(-180,180,10):
                    a = A*np.pi/180
                    x1 = int(x+r*np.cos(a))
                    y1 = int(y+r*np.sin(a))
                    if 0<=x1<W and 0<=y1<H:
                        t[y,x,r] = I[y1,x1]
                        
    return t


def hough_circle2(I):
    H,W=I.shape
    t = np.zeros((H,W,30))
    for y in range(H):
        for x in range(W):
            if I[y,x]==1:
                for r in range(10,30):
                    for A in range(-180,180,10):
                        a = A*np.pi/180
                        x1 = int(x+r*np.cos(a))
                        y1 = int(y+r*np.sin(a))
                        if 0<=x1<W and 0<=y1<H:
                            t[y1,x1,r]+=1
                            
        return t


               
            
    
    
    
    
    
    
    
    
    
    