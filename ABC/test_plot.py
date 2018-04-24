# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, 1, 0.01)
y = -x * np.log(x)
plt.plot(x,y)