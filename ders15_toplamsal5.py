import numpy as np
import matplotlib.pyplot as plt
import uzaysal as zs
import katmansal as kt
import toplamsal as tp


I=plt.imread("data/circle.png")[:,:,0]

plt.figure()
plt.subplot(1,3,1)
plt.imshow(I,"gray")
J = tp.hough_circle2(I)

plt.subplot(1,3,2)
plt.imshow(np.sum(J,axis=2),"gray")
    
    
