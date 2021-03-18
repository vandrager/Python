import time, random
import numpy as np
import sys
# print(sys.argv[0])
# print(time.time())

# list_a = ["a", "b", "c", "d"]

# print(list_a[0:2])

# import os

# print(os.listdir())

con = ["bio", "enemy", "ill"]
conj = ", ".join(con)
print(", ".join(con))

for i in range(3):
    print(conj)

for i in range(100):
    print(str(time.time())[:-7])

x, y, z, w = np.random.randint(10, 200, size = 4)
print(f"x = {x}, y = {y}, z = {z}, w = {w}")

k = np.random.randint(10, size = 4)
print(k)
