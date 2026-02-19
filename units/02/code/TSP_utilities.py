import numpy as np
#-----------------------------------------------------------------------------------------------------------------------
def load_instance(path, filename, n, Asymmetry_Flag, data_format_flag):
    #path = os.path.dirname(__file__)
    #path = os.path.dirname(os.path.dirname(__file__))

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
    if data_format_flag == 'TSPLIB':
        if not Asymmetry_Flag:
            problem = tsplib95.load_problem(path + '/' + filename + ".tsp")
        else:
            problem = tsplib95.load_problem(path + '/' + filename + ".atsp")
        for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    d[i, j] = problem.wfunc(i, j)
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
    symmetry_check = 1
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                if d[i, j] != d[j, i]:
                    symmetry_check = 0
                    break
    print()
    print('#####################################################')
    if symmetry_check == 1:
        print('Symmetric instance loaded ' + filename)
    else:
        print('Asymmetric instance loaded ' + filename)
        asymmtery_measure = 0
        epsilon = 0
        D_sum = 0
        for i in range(0, n):
            for j in range(0, n):
                if i < j:
                    D_sum += d[i, j] + d[j, i]
                    if d[i, j] != d[j, i]:
                        asymmtery_measure += 1
                        epsilon += abs(d[i, j] - d[j, i])
        print('Asymmetry measure Type 1:', round(100 * 2 * asymmtery_measure / (n * (n - 1)), 2), '%')
        print('Asymmetry measure Type 2:', round(100 * epsilon / D_sum, 2), '%')
        #for i in range(0, n):
        #    count = 0
        #    for j in range(0, n):
        #        if i != j and d[i, j] != d[j, i]:
        #            count += 1
        #    if count > 0:
        #        print('# of asymmetric arcs from node ', i, ' is ', count)
    return d
#-----------------------------------------------------------------------------------------------------------------------
