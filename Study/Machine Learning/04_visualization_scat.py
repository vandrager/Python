import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

plt.style.use("default")
df = pd.read_csv("auto-mpg.csv", header=None)
df.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]
print(type(df))
df.plot(kind = 'scatter',x = 'wei', y = 'mpg', c= 'coral', s = 10, figsize=(10, 5))
plt.title("scatter plot", size = 20)
plt.show()

syl_size = df.cyl/df.cyl.max() * 300
df.plot(kind = 'scatter',x = 'wei', y = 'mpg', c= 'coral', s = syl_size, alpha = 0.3, figsize=(10, 5))
# alpha값은 투명도 조절임
plt.title("scatter plot", size = 20)
plt.show()

syl_size = df.cyl/df.cyl.max() * 300
df.plot(kind = 'scatter',x = 'wei', y = 'mpg', marker = '+', cmap= 'viridis', c = syl_size, s = 50, alpha = 0.3, figsize=(10, 5))
plt.title("scatter plot(colorful)", size = 20)
plt.savefig("scatter.png")
plt.savefig("scatter_transparent.png", transparent= True)
plt.show()