import gurobipy as gp
from data import BinPackingExample, Lister, FFD
import itertools


def bpp(s, B):
    n = len(s)
    U = len(FFD(s, B))
    
    # Your Gurobi model for the compact formulation
    model = gp.Model("bpp")
    x, y = {}, {}
    for i in range(n):
        for j in range(U):
            x[i, j] = model.addVar(vtype=gp.GRB.BINARY, name="x(%s,%s)" % (i, j))
    for j in range(U):
        y[j] = model.addVar(vtype=gp.GRB.BINARY, name="y(%s)" % j)

    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(U)) == 1, "Assign(%s)" % i)
    for j in range(U):
        model.addConstr(gp.quicksum(s[i]*x[i, j] for i in range(n)) <= B*y[j], "Capac(%s)" % j)
    for j in range(U):
        for i in range(n):
            model.addConstr(x[i, j] <= y[j], "Strong(%s,%s)" % (i, j))
    model.setObjective(gp.quicksum(y[j] for j in range(U)), gp.GRB.MINIMIZE)
    model._x = x # , y
    return model


def solveBinPacking(s, B):
    n = len(s)
    U = len(FFD(s, B))
    model = bpp(s, B)
    model.optimize()
    bins = [[] for i in range(U)]
    # Get the contents of the bins from your model 
    for i in range(n):
        for j in range(U):
            if model._x[i,j].X>.5:
                bins[j].append(s[i])

    
    for i in range(bins.count([])):
        bins.remove([])
    for b in bins:
        b.sort()
    bins.sort()
    return bins


if __name__ == '__main__':
    s, B = BinPackingExample()
    # s, B = Lister()
    bins = solveBinPacking(s, B)
    print(len(bins))
    for b in bins:
        print((b, sum(b)))
