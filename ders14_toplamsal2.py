import numpy as np
import matplotlib.pyplot as plt
import uzaysal as zs
import katmansal as kt
import toplamsal as tp


I=plt.imread("data/biber.png")[:,:,0]
J = tp.radon(I)
T=np.zeros((I.shape[0],180))
plt.figure()
plt.subplot(1,3,1)
plt.imshow(I)


for a in range(180):
    J = tp.donusum(I,a)
    T[:,a] = np.sum(J,axis=1)
    plt.subplot(1,3,2)
    plt.gca()
    plt.imshow(J,"gray")
    
    plt.subplot(1,3,3)
    plt.gca()
    plt.imshow(T,"gray")
    plt.pause(0.1)
