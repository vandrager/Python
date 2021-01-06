from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

x = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# plt.plot(x)
# plt.show()
# plt.plot(x, color = 'r') # 컬러를 red(빨간색)으로 만들어라
# plt.show()
# plt.plot(x, ':', color = 'r') #점선으로 만들어라
# plt.show()

# 자세한 맷플롯립 함수모양 설정은 아래 링크 참고
# (https://kongdols-room.tistory.com/82)

y = [i for i in range(0, 9)]
print(y)
plt.plot(x, y)
plt.xlabel("x축")
plt.ylabel("y축")
plt.title("matplotlib sample")
plt.show()