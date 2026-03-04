from gurobipy import *
from itertools import product
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
def create_RC_cut(model, S):
    target_no_vehicles = np.ceil(sum(model._demand[i] for i in S) / model._Q)
    S_size = len(S)
    Constr_LHS = quicksum(model._x[i, j] for (i, j) in product(S, S) if i != j)
    Constr_RHS = S_size - target_no_vehicles
    return Constr_LHS, Constr_RHS
#-----------------------------------------------------------------------------------------------------------------------
def create_RC_cut_symm(model, S):
    target_no_vehicles = np.ceil(sum(model._demand[i] for i in S) / model._Q)
    S_size = len(S)
    Constr_LHS = quicksum(model._x[i, j] for (i, j) in product(S, S) if i < j)
    Constr_RHS = S_size - target_no_vehicles
    return Constr_LHS, Constr_RHS
#-----------------------------------------------------------------------------------------------------------------------
