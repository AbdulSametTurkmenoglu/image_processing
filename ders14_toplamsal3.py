import numpy as np
import matplotlib.pyplot as plt
import uzaysal as zs
import katmansal as kt
import toplamsal as tp


I=plt.imread("data/biber.png")[:,:,0]
# J = tp.hough_line(I)
# plt.figure()
# plt.subplot(1,3,1)
# plt.imshow(I)
# plt.subplot(1,3,2)
# plt.imshow(J,"gray")
    
for i in range(100):
    y= np.random.randint(0,I.shape[0])
    x= np.random.randint(0,I.shape[0])
    I[y,x] = 1
J = tp.hough_line(I)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(I)


plt.subplot(1,3,2)
plt.imshow(J,"gray")