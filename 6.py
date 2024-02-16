import numpy as np
#ravel method
a1=np.arange(9).reshape(3,3)
print(a1)
'''a2=np.ravel(a1)
print(a2)
a2[4]=200
print(a2)
print(a1)'''
a3=a1.flatten()
print(a3)
a3[4]=200
print(a3)
print(a1)
