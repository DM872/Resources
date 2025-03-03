#-----------------------------------------------------------------------------------------------------------------------
from CVRP_utilities import *
from gurobipy import *
#-----------------------------------------------------------------------------------------------------------------------
def ACVRP_compact_formulation(folder, filename, Q, n, relax, time_lim):
    d, demand = load_instance(folder, filename, n)
    #-------------------------------------------------------------------------------------------------------------------
    def RCI_fractional_node_callback(model, where):
        if where == GRB.Callback.MIPNODE:
            # add cuts at every bnb node
            if model.cbGet(GRB.callback.MIPNODE_NODCNT) % 3 == 0:
                if model.cbGet(GRB.Callback.MIPNODE_STATUS) == GRB.OPTIMAL:
                    x_values = model.cbGetNodeRel(model._x)
                    model.cbCut(0, GRB.LESS_EQUAL, 0)
    #-------------------------------------------------------------------------------------------------------------------
    m = Model("Optimize")
    x = {}
    u = {}
    C_0 = set(range(0, n + 1))
    C = set(range(1, n + 1))
    for i in C:
        u[i] = m.addVar(vtype=GRB.CONTINUOUS, name='u_' + str(i))
    for i in C_0:
        for j in C_0:
            if i != j:
                x[i, j] = m.addVar(vtype=GRB.CONTINUOUS, name='x_' + str(i) + '_' + str(j))
    for i in C:
        m.addConstr(quicksum(x[i, j] for j in C_0 if j != i), GRB.EQUAL, 1)
        m.addConstr(quicksum(x[j, i] for j in C_0 if j != i), GRB.EQUAL, 1)

    obj = quicksum(d[i, j] * x[i, j] for i in C_0 for j in C_0 if i != j)
    m.setObjective(obj, GRB.MINIMIZE)

    # D-L constraints
    for i in C:
        adjcoeff = max(demand[j] for j in C if j != i)
        m.addConstr(u[i], GRB.LESS_EQUAL, Q - (Q - adjcoeff - demand[i]) * x[0, i] - quicksum(demand[j] * x[i, j] for j in C if j != i), name='UB_' + str(i))
        m.addConstr(u[i], GRB.GREATER_EQUAL, demand[i] + quicksum(demand[j] * x[j, i] for j in C if j != i), name='LB_' + str(i))
    for i in C:
        for j in C:
            if i != j:
                m.addConstr(u[i] - u[j] + Q * x[i, j] + (Q - demand[i] - demand[j]) * x[j, i], GRB.LESS_EQUAL, Q - demand[j], name='Laporte_' + str(j) + '_' + str(i))
    # G-G m constraints instead

    #m.setParam('OutputFlag', False)
    add_root_node_DFJ_cuts = True
    if add_root_node_DFJ_cuts:
        m.optimize()
        x_values = {(i, j): x[i, j].x for (i, j) in x.keys()}
        #print(x_values[(0, 1)])
        # ....
        add_root_node_DFJ_cuts = False
    if not relax:
        # set up the MILP problem
        for i in C:
            for j in C:
                if i != j:
                    x[i, j].vtype = GRB.BINARY
        m.Params.LazyConstraints = 1
        m._x = x
        m._n = n
        m._Q = Q
        m._demand = demand
        m._epsilon_1 = pow(10, -4)
        m._epsilon_2 = pow(10, -3)
        m.setParam('MIPGap', 0) # means that an optimal solution is being searched for
        m.setParam('MIPGapAbs', 0.99) # means that the absolute gap might be up to 1 withoug violating optimality conditions
        m.setParam('Timelimit', time_lim)
        # no callback
        m.optimize()
        # with callback
        #m.optimize(RCI_fractional_node_callback)
#-----------------------------------------------------------------------------------------------------------------------
def main_ACVRP():
    relax = False
    time_lim = 3600
    ACVRP_compact_formulation('instances', 'A-n33-k5', 100, 32, relax, time_lim)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main_ACVRP()
