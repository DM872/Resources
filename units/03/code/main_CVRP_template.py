#-----------------------------------------------------------------------------------------------------------------------
import numpy as np
from itertools import product
from gurobipy import *
from time import *
from CVRP_utilities import *
#-----------------------------------------------------------------------------------------------------------------------
def SCVRP_2CF(mode, folder, filename, n, V, Q, opt_obj, relax, add_cuts, warm_start, timelim):
    c, demand = load_instance(folder, filename, n)
    start_time = time()
    m = Model("Optimize")

    def RCI_fractional_node_callback(model, where):
        if where == GRB.Callback.MIPNODE:
            # add cuts at every bnb node
            if model.cbGet(GRB.callback.MIPNODE_NODCNT) % 1 == 0:
                if model.cbGet(GRB.Callback.MIPNODE_STATUS) == GRB.OPTIMAL:
                    x_values = model.cbGetNodeRel(model._x)
                    m_separation = Model("Optimize")
                    m_separation.setParam('OutputFlag', False)
                    m_separation.setObjective(obj_separation, GRB.MAXIMIZE)
                    m_separation.optimize()
                    if m_separation.objval >= 0.01:
                        S = {i for i in range(1, model._n + 1) if delta[i].x > 0.5}
                        LHS, RHS = create_RC_cut_symm(model, S)
                        model.cbCut(LHS, GRB.LESS_EQUAL, RHS)
    x = {}
    y = {}
    for i in range(1, n + 1):
        x[0, i] = m.addVar(vtype=GRB.CONTINUOUS, name='x_0_'+str(i))
        for j in range(i + 1, n + 1):
            x[i, j] = m.addVar(vtype=GRB.CONTINUOUS, ub=1, name='x_'+str(i)+'_'+str(j))
            y[i, j] = m.addVar(vtype=GRB.CONTINUOUS, name='y_'+str(i)+'_'+str(j))
            y[j, i] = m.addVar(vtype=GRB.CONTINUOUS, name='y_'+str(j)+'_'+str(i))

    for i in range(1, n + 1):
        m.addLConstr(quicksum(x[min(i, j), max(i, j)] for j in range(0, n + 1) if i != j), GRB.EQUAL, 2, name='degree_of_'+str(i))

    m.setObjective(quicksum(c[i, j] * x[i, j] for i in range(0, n + 1) for j in range(i + 1, n + 1)), GRB.MINIMIZE)

    # 2CF-CVRP formulation follows below ....

    # 2CF-CVRP formulation finished
    m._n = n
    m._demand = demand
    m._Q = Q
    m._x = x
    m.setParam('OutputFlag', False)
    m.optimize()
    print('Initial bound ', np.round(m.objval, 2))
    need_to_find_RCI_cuts = False
    cuts_count = 0
    if need_to_find_RCI_cuts:
        while need_to_find_RCI_cuts:
            m_separation = Model("Optimize")
            m_separation.setParam('OutputFlag', False)

            m_separation.optimize()
            if m_separation.objval >= 0.01:
                S = {i for i in range(1, n + 1) if delta[i].x > 0.5}
                LHS, RHS = create_RC_cut_symm(m, S)
                cuts_count += 1
                m.addLConstr(LHS, GRB.LESS_EQUAL, RHS)
                m.optimize()
                print('New bound: ', m.objval)
            else:
                need_to_find_RCI_cuts = False
        cvrp_lower_bound = m.objval
        print(filename, 'Q='+str(Q), round(cvrp_lower_bound, 2))
        print('2CF-CVRP ' + mode + ' LP time: ', round(time() - start_time, 1), ' sec. ', cuts_count, ' cuts generated')
        print('Instance ', filename, 'Q=', Q)
        if opt_obj != None:
            print('CVRP lower bound ', round(cvrp_lower_bound, 2), str(round(100 * cvrp_lower_bound / opt_obj, 2))+'%')
        else:
            print('CVRP lower bound ', cvrp_lower_bound)
    if not relax:
        m.setParam('OutputFlag', True)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                x[i, j].vtype = GRB.BINARY
        m.setParam('DisplayInterval', 100)
        m.setParam('TimeLimit', timelim)
        m.setParam('MIPGap', 0.0)
        m.setParam('MIPGapAbs', 0.99)
        m.optimize()
        #m.optimize(RCI_fractional_node_callback)
        print(filename, 'Q='+str(Q), round(m.objval, 2), str(round(m.MIPGap * 100, 2))+'%', str(round(m.Runtime, 1))+' sec.')
    print()
#-----------------------------------------------------------------------------------------------------------------------
def main_A_SCVRP():
    timelim = 3600
    relax = False
    warm_start = ''
    add_cuts = ''
    mode = 'm'
    SCVRP_2CF(mode, 'CVRP_instances', 'A-n33-k5', 32, 5, 100, 661, relax, add_cuts, warm_start, timelim)
    #SCVRP_2CF(mode, 'CVRP_instances', 'A-n55-k9', 54, 9, 100, 1073, relax, add_cuts, warm_start, timelim)
    #SCVRP_2CF(mode, 'CVRP_instances', 'A-n80-k10', 79, 10, 100, 1763, relax, add_cuts, warm_start, timelim)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main_A_SCVRP()
