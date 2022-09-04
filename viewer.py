# read the file at /home/jeff/Documents/Code/EvoSkeleton-master/examples/jeff_kpts_normalized_clipped/jeff_test_2_3d_8_good.npy
# and display it in a 3D plot

import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

f = np.load('/home/jeff/Documents/Code/EvoSkeleton-master/examples/jeff_kpts_normalized_clipped/jeff_test_2_3d_8_good.npy')
ax = plt.subplot(gs[0], projection='3d')
for i in f:
    ax.scatter(x, y, z)