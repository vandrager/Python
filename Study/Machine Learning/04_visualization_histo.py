import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")
from matplotlib import font_manager, rc
font_path = r'C:\Windows\Fonts\Malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use("classic")
df = pd.read_csv("auto-mpg.csv")
df.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]

df['mpg'].plot(kind = 'hist', bins=10, color= 'coral', figsize=(10, 5))
plt.xlabel("mpg", size =10)
plt.title("histogram", size = 20)
plt.show()