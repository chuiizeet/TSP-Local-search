import numpy as np
import matplotlib.pyplot as plt

x = np.array([12,  5,  9,  7,  2])
y = np.array([10,  14,  11,  5,  12])

solution = np.array([4,1,2,0,3,4])

plt.plot(x,y, 'o', color='red')

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

for i in range(0,int(len(solution))):
    if(i < int(len(solution))-1):
        print(solution[i], solution[i+1])
        connectpoints(x,y,solution[i],solution[i+1])

plt.show()








# connectpoints(x,y,4,1)
# connectpoints(x,y,1,2)
# connectpoints(x,y,2,0)
# connectpoints(x,y,0,3)
# connectpoints(x,y,4,3)
#
#
# plt.show()
