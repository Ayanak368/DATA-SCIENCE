import numpy as np
x=np.arange(16).reshape(4,4)
print("Array:\n",x)
header="C1 C2 C3 C4"
np.savetxt("array.txt",x,fmt="%d",header=header)
print("\n After loading,content of the text file:")
print(np.loadtxt("array.txt"))