import numpy as np
import matplotlib.pyplot as plt
import uzaysal as zs
import katmansal as kt
import toplamsal as tp


I=plt.imread("data/biber.png")[:,:,0]

plt.figure()
plt.subplot(1,3,1)
plt.imshow(I)

    
J = tp.radon(I)
plt.subplot(1,3,2)
plt.imshow(J,"gray")
    
    
