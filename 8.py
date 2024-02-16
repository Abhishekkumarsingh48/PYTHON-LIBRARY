import numpy as np
a=np.arange(6,12).reshape(2,3)
print(a)
b=np.arange(6).reshape(2,3)
print(b)
c=np.hstack([b,a])
print(c)
d=np.vstack([b,a])
print(d)

