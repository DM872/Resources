import numpy as np
#-----------------------------------------------------------------------------------------------------------------------
def load_instance(path, filename, n, Asymmetry_Flag, data_format_flag):
    d = np.zeros((n, n))
    if data_format_flag == 'CONCORD':
        if path != '':
            temp = np.loadtxt(path + '/' + filename + ".txt")
        else:
            temp = np.loadtxt(filename + ".txt")
        if not Asymmetry_Flag:
            for i in range(0, n):
                for j in range(0, n):
                    if i < j:
                        d[i, j] = np.round(np.sqrt(np.square(temp[i, 1] - temp[j, 1]) + np.square(temp[i, 2] - temp[j, 2])))
                        d[j, i] = d[i, j]
    if data_format_flag == 'SQUARE':
        if Asymmetry_Flag:
            temp = np.loadtxt(path + '/' + filename + ".txt")
            for i in range(0, n):
                for j in range(0, n):
                    if i != j:
                        d[i, j] = temp[i, j]
    if data_format_flag == 'VECTOR':
        temp = np.loadtxt(path + '/' + filename + ".txt")
        for i in range(0, len(temp)):
            j = i % n
            d[int((i - j)/n), j] = temp[i]
    return d
#-----------------------------------------------------------------------------------------------------------------------
