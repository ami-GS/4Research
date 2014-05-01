from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np
import libmushu as lm
import time

amps = lm.get_available_amps()
print amps
amp = lm.get_amp(amps[0])

channelNum = 17 #g.USBamp 17 max
SAMPLENUM = 128
amp.configure(fs=SAMPLENUM, channels=channelNum)
XMIN, XMAX = 0, 2
YMIN, YMAX = 0, 1024
INTERVAL = 1
TIME = np.linspace(XMIN, XMAX, SAMPLENUM*(XMAX-XMIN))

fig = plt.figure()
ax = []
plots = []
ydatas = []

for i in range(channelNum):
    tmpax = fig.add_subplot(channelNum,1,i)
    tmpax.set_xlim(XMIN,XMAX)
    tmpax.set_ylim(YMIN, YMAX)
    ax.append(tmpax)
    ydatas.append(np.zeros(0))
    plots.append(tmpax.plot(np.zeros(0), ydatas[i])[0])

def gen():
    while True:
        data = amp.get_data()[0]
        if ydatas[0].shape[0] + len(data[:, 0]) >= len(TIME):
            initData()
        yield data

def initData():
    for i in range(channelNum):
        ydatas[i] = np.zeros(0)

def updataData(data):
    for i in range(channelNum):
        ydatas[i] = np.append(ydatas[i], data[:, i])
        #print len(TIME[:ydatas[i].shape[0]]), len(ydatas[i]), ydatas[i].shape[0], "set"
        plots[i].set_data(TIME[:ydatas[i].shape[0]], ydatas[i])

    return plots

amp.start()
#time.sleep(0.5)
ani = animation.FuncAnimation(fig, updataData, gen, blit = False, interval=INTERVAL, repeat=False)
plt.show()
amp.stop()