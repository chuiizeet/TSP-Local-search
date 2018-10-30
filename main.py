import numpy as np


x_prices = np.array([
[ 0,  8,  3,  7,  10],
[ 8,  0,  5,  9,  4],
[ 3,  5,  0,  6,  7],
[ 7,  9,  6,  0,  9],
[ 10,  4,  7,  9,  0]])


hamiltoniano = np.array([
[5,2,3,1,4,5],
[0,0,0,0,0]
])

hamiltoniano_list = []

for i in range(0,6):
    hamiltoniano_list.append(hamiltoniano[0][i])




def price(tsp):
    # print(type(tsp))
    # print(len(tsp))
    # print(tsp[0],tsp[1])
    # print(tsp[1],tsp[2])
    # print(tsp[2],tsp[3])
    # print(tsp[3],tsp[4])
    # print(tsp[4],tsp[0])
    print("-----------")

    for i in range (0,len(tsp)):
        j = i + 1
        if j > int(len(tsp)-1):
            j = j - 1
            break;
        else:
            x = int(tsp[i])
            y = int(tsp[j])

            print(x_prices[x-1][y-1])























#MARK: Init functions
price(hamiltoniano_list)
