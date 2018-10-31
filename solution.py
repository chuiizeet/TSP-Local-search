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



def localSearch(tspInit):


    print(price(tspInit)[0], "->", price(tspInit)[1])
    print("-----------------------")

    items = np.array(tspInit)
    indices = np.arange(items.shape[0])

    for i in range(1,int(len(items))-1):
        for j in range(1,int(len(items))-1):
            items[j],items[i] = items[i],items[j]
            if i != j:
                print(price(items)[0], "->", price(items)[1])
            if price(items)[1] < price(tspInit)[1]:
                return localSearch(items)



def price(tsp):
    #MARK: fo
    fo = 0;
    for i in range (0,len(tsp)):
        j = i + 1
        if j > int(len(tsp)-1):
            j = j - 1
            break;
        else:
            x = int(tsp[i])
            y = int(tsp[j])

            fo += x_prices[x-1][y-1]

    values = [tsp,fo]

    return values

#MARK: Init functions
localSearch(hamiltoniano_list)
#price(hamiltoniano_list)
