import numpy as np
k=int(input())
a=np.array([list(map(int,input().split())) for i in range(k)])
b=np.array([list(map(int,input().split()))for i in range(k)])
print(a@b)