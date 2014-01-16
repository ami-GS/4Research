__author__ = 'daiki'


import matplotlib.pyplot as plt

subject = [1,2,3,4]#example
data = [42.5, 30.7, 6.25, 53]#example

barWidth = 0.7
plt.bar(subject, data, width=barWidth, align="center")
plt.xticks(subject, ["#1","#2","#3","#4"])#example

plt.show()
