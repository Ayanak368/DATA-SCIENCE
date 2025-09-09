import numpy as np
num=np.arange(16,dtype="int").reshape(-1,4)
print("Original array:\n",num)
print("\n New array swapping first and last rows of the said array:")
num=num[[-1,1,2,0]]
print(num)