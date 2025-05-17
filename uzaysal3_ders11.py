import numpy as np
import matplotlib.pyplot as plt
import noktasal as nk
import alansal as al
import bicimsel as bc
import konumsal as kn
import uzaysal as uz



I = plt.imread("data/biber.png")[::5,::5,:3]

a = np.array([[1.2*0.866,-0.5,0],[0.5,1.2*0.866,0],[0,0,1]])

J= uz.affine(I,a)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(I)

plt.subplot(1,2,2)
plt.imshow(J)
