import numpy as np
import matplotlib.pyplot as plt
import noktasal as nk
import alansal as al
import bicimsel as bc
import konumsal as kn
import uzaysal as uz



I = plt.imread("data/biber.png")[::5,::5,:3]

XY = np.array([[0,100,100],[0,100,0],[1,1,1]])
UV = np.array([[200,100,100],[0,100,0],[1,1,1]])

J= uz.transform_matrix(XY,UV)
j=uz.affine(I, J)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(I)

plt.subplot(1,2,2)
plt.imshow(j)
