#-----------------------------------------------------------------------------------------------------------------------
from TSP_utilities import *
from gurobipy import *
#-----------------------------------------------------------------------------------------------------------------------
def find_subtours(x_values):
    G = nx.Graph()
    for (i, j) in x_values.keys():
        if x_values[i, j] > 0.5:
            G.add_edge(i, j)
    returned_subtours = []
    for tour in nx.connected_components(G):
        returned_subtours.append(tour)
    return returned_subtours
#-----------------------------------------------------------------------------------------------------------------------
def ATSP_DFJ(folder, filename, Asymmetry_Flag, data_format_flag, n, relax, time_lim):
    d = load_instance(folder, filename, n, Asymmetry_Flag, data_format_flag)
    #-------------------------------------------------------------------------------------------------------------------
    def DFJ_incumbent_callback(model, where):
        if where == GRB.Callback.MIPSOL:
            x_values = model.cbGetSolution(model._x)
            subtours = find_subtours(x_values)
            if len(subtours) > 0:
                for S in subtours:
                    if len(S) < model._n:
                        if len(S) <= model._n / 2:
                            model.cbLazy(quicksum(model._x[i, j] for i in S for j in S if i != j) <= len(S) - 1)
                        else:
                            S_bar = set(range(0, model._n)).difference(S)
                            model.cbLazy(quicksum(model._x[i, j] for i in S_bar for j in S_bar if i != j) <= len(S_bar) - 1)
    #-------------------------------------------------------------------------------------------------------------------
    def DFJ_fractional_node_callback(model, where):
        if where == GRB.Callback.MIPNODE:
            # add violated cuts at every BnB node
            if model.cbGet(GRB.callback.MIPNODE_NODCNT) % 1 == 0:
                if model.cbGet(GRB.Callback.MIPNODE_STATUS) == GRB.OPTIMAL:
                    x_values = model.cbGetNodeRel(model._x)
                    model.cbCut(0, GRB.LESS_EQUAL, 0)
    #-------------------------------------------------------------------------------------------------------------------
    def complete_callback(model, where):
        #DFJ_fractional_node_callback(model, where)
        DFJ_incumbent_callback(model, where)
    #-------------------------------------------------------------------------------------------------------------------
    m = Model("Optimize")
    x = {}
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                x[i, j] = m.addVar(vtype=GRB.CONTINUOUS, name='x_' + str(i) + '_' + str(j))
    for i in range(0, n):
        m.addLConstr(quicksum(x[i, j] for j in range(0, n) if i != j), GRB.EQUAL, 1)
        m.addLConstr(quicksum(x[j, i] for j in range(0, n) if i != j), GRB.EQUAL, 1)

    obj = quicksum(d[i, j] * x[i, j] for i in range(0, n) for j in range(0, n) if i != j)
    #m.setParam('OutputFlag', False)
    m.setObjective(obj, GRB.MINIMIZE)
    add_root_node_DFJ_cuts = True
    if add_root_node_DFJ_cuts:
        m.optimize()
        x_values = {(i, j): x[i, j].x for (i, j) in x.keys()}
        #print(x_values[(0, 1)])
        # .... separate and add violated DFJ inequalities

    if not relax:
        # set up the MILP problem
        for (i, j) in x.keys():
            x[i, j].vtype = GRB.BINARY
        # provide the simplest 1 -> 2 -> 3 .... n -> 1 to the solver as a starting solution
        for k in range(1, n):
            x[k - 1, k].start = 1.0
        m.Params.LazyConstraints = 1
        m._x = x
        m._n = n
        m._epsilon_1 = pow(10, -4)
        m._epsilon_2 = pow(10, -3)
        # we search for truly optimal solutions, for which we can prove that the optimality gaps is 0
        m.setParam('MIPGap', 0)       
        # given that all c_ij costs are integer-valued, then a lower bound = a + epsilon where a is integer and epsilon < 1 implies that an 
        # optimal solution might have the objective of at least a + 1. hence, the absolute optimality gap equal to 0.99 allows to find a 
        # provably optimal solution 
        m.setParam('MIPGapAbs', 0.99) 
        m.setParam('Timelimit', time_lim)
        # no callback
        #m.optimize()
        # with callback
        m.optimize(complete_callback)
#-----------------------------------------------------------------------------------------------------------------------
def main_ATSP():
    relax = False
    Asymmetry_Flag = True
    time_lim = 3600
    #ATSP_DFJ('realfiles', 'dc112', Asymmetry_Flag, 'VECTOR', 112, relax, time_lim)
    ATSP_DFJ('realfiles', 'dc126', Asymmetry_Flag, 'VECTOR', 126, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc134', Asymmetry_Flag, 'VECTOR', 134, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc176', Asymmetry_Flag, 'VECTOR', 176, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc188', Asymmetry_Flag, 'VECTOR', 188, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc563', Asymmetry_Flag, 'VECTOR', 563, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc849', Asymmetry_Flag, 'VECTOR', 849, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc895', Asymmetry_Flag, 'VECTOR', 895, relax, time_lim)
    #ATSP_DFJ('realfiles', 'dc932', Asymmetry_Flag, 'VECTOR', 932, relax, time_lim)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main_ATSP()
