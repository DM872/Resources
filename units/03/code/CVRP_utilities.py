import numpy as np
#-----------------------------------------------------------------------------------------------------------------------
def load_instance(folder, filename, n):
    temp = np.loadtxt(folder + '/' + filename + '.txt')
    d = np.zeros((n + 1, n + 1))
    temp2 = np.loadtxt(folder + '/' + filename + '+demand.txt')
    demand = np.zeros(n + 1)
    for i in range(0, n + 1):
        demand[i] = temp2[i, 1]
        for j in range(0, n + 1):
            if i < j:
                d[i, j] = np.round(np.sqrt(np.square(temp[i, 1] - temp[j, 1]) + np.square(temp[i, 2] - temp[j, 2])))
                #d[i, j] = np.sqrt(np.square(temp[i, 1] - temp[j, 1]) + np.square(temp[i, 2] - temp[j, 2]))
                d[j, i] = d[i, j]
    return d, demand
#-----------------------------------------------------------------------------------------------------------------------
