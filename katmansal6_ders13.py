import numpy as np
import matplotlib.pyplot as plt
import noktasal as nk
import alansal as al
import bicimsel as bc
import konumsal as kn
import uzaysal as uz
import katmansal as ka


I1 = plt.imread("data/domates.jpg")
plt.imsave("data/domates01.png",I1)


I2 = plt.imread("data/elma.jpg")
plt.imsave("data/elma01.png",I2)

I1 = plt.imread("data/domates01.png")[::1,::1,:3]
I2 = plt.imread("data/elma01.png")[::1,::1,:3]


plt.figure()
plt.subplot(1,3,1)
plt.imshow(I2)

plt.subplot(1,3,2)
plt.imshow(I1)

J = ka.yogunluk2(I2,I1) 
plt.subplot(1,3,3)
plt.imshow(J)