import numpy as np

a = np.random.randint(32,size=(8,4))
print(a)
np.ravel(a)

x1=[[1,2,3],[4,5,6],[7,8,9]]
np.ravel(x1)

m = np.arange(8)
m.reshape(2,4)