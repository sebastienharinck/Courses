# What Makes a Good Feature? - Machine Learning Recipes #3
# https://www.youtube.com/watch?v=N9fDIAflCMY&list=PLT6elRN3Aer7ncFlaCz8Zz-4B5cnsrOMt&index=4

import numpy as np
import matplotlib.pyplot as plt 

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()