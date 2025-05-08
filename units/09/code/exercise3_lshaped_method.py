#!/usr/bin/env python
# coding: utf-8

# # Problem
# Consider the following problem
# $$
# \begin{align*}
#   \min~&2x + \pi_1(y_{11} + 3y_{21}) + \pi_2(y_{12} + 3y_{22})+ \pi_3(y_{13} + 3y_{23})\\
#   \text{s.t.}~&2y_{1s}+y_{2s}+x = h_{1s} & s=1,\ldots,3\\
#        &-y_{1s}+y_{2s} +4x \geq h_{2s}& s=1,\ldots,3\\
#        &y_{1s},y_{2s}\geq 0, s=1,\ldots,3,x\geq 0
# \end{align*}
# $$
# 
# $(h_1,h_2)\in \Xi=\big\{(1,2),(1,3),(2,1)\big\}$ and $\pi_1=\pi_2=\pi_3=\frac{1}{3}$.

# # Exercise
# Solve the problem using the L-Shaped method and compare its solution to that obtained without decomposing the problem. Use the code below to get started.

# ## Useful code
# 

# In[ ]:


get_ipython().system('pip install gurobipy')
from gurobipy import Model, GRB, quicksum


# In[ ]:


class Scenarios:
  
    def __init__(self):
        self.n_scenarios = 3
        self.probability = [1/self.n_scenarios for s in range(self.n_scenarios)]
        self.h1 = [1,1,2]
        self.h2 = [2,3,1]


# This is how to use the `Scenarios` class.

# In[ ]:


scenarios = Scenarios()
print("Scenario 1 : h1=",scenarios.h1[0]," h2=",scenarios.h2[0]," probability=",scenarios.probability[0])


# ### Model
# We start by implementing a model for the problem (without decomposition).

# In[ ]:


class FullModel:
    def __init__(self, data: Scenarios):
        self.m = Model()
        self.data = data
        # Variables
        self.x = self.m.addVar(name="x")
        self.y1 = self.m.addVars(data.n_scenarios,name="y_1")
        self.y2 = self.m.addVars(data.n_scenarios,name="y_2")
        
        # Objective
        self.m.setObjective(2 * self.x 
                            + quicksum([data.probability[s] * (self.y1[s] + 3* self.y2[s]) 
                                        for s in range(data.n_scenarios)]))
        
        # Constraints
        self.m.addConstrs(2 * self.y1[s]+self.y2[s] == data.h1[s] - self.x for s in range(data.n_scenarios))
        self.m.addConstrs(-self.y1[s]+self.y2[s] >= data.h2[s] - 4* self.x for s in range(data.n_scenarios))

    def solve(self):
        self.m.Params.OutputFlag=0 
        self.m.optimize()
        
    def print_solution(self):
        print("Objective : ",self.m.objVal)
        print("x : ", self.x.x)
        print("y1 : ", self.m.getAttr('x',self.y1))
        print("y2 : ", self.m.getAttr('x',self.y2))


# ### Master Problem
# We will now implement the Master Problem. Obseve that the `MasterProblem` class has methods to add optimality and feasibility cuts which take as arguments the dual solution to the subproblems. 

# In[ ]:


class MasterProblem:
    
    def __init__(self,data:Scenarios):
        self.m = Model()
        self.data = data
        # Variables
        self.x = self.m.addVar(name="x")
        self.phi = self.m.addVar(name='phi')
        
        # Objective
        self.m.setObjective(2 * self.x + self.phi)
        
        
    def solve(self):
        self.m.Params.OutputFlag=0 
        self.m.optimize()
        
    def print_solution(self):
        print("Objective : ",self.m.objVal)
        print("x : ", self.x.x)
        print("phi : ", self.phi.x)
        
    def get_solution(self):
        return self.x.x, self.phi.x
    
    def get_objective(self):
        return self.m.objVal        
        
    def add_fc(self,s:int,dual1:float,dual2:float):
        self.m.addConstr(dual1 * (self.data.h1[s] - self.x) + dual2 * (self.data.h2[s] - 4*self.x) <= 0)
        
    def add_oc(self,dual1:list,dual2:list):
        self.m.addConstr(
            quicksum(
                self.data.probability[s] * (dual1[s] * (self.data.h1[s] - self.x) 
                                          + dual2[s] * (self.data.h2[s] - 4*self.x) ) for s in range(self.data.n_scenarios)) 
            <= self.phi)
    
  


# ### Subproblems
# We proceed by implementing the Feasibility and Optimality subproblems. Observe that both subproblems have methods to retrieve the optimal dual solution which will then be necessary to generate cuts.

# In[ ]:


class FSP:
    
    def __init__(self,data:Scenarios, s:int, X:float):
        self.m = Model()
        self.data = data
        
        # Variables
        self.y1 = self.m.addVar(name="y_1")
        self.y2 = self.m.addVar(name="y_2")
        self.v1 = self.m.addVar(name="v_1")
        self.v2 = self.m.addVar(name="v_2")
        self.v3 = self.m.addVar(name="v_3")
        
        # Objective
        self.m.setObjective(self.v1 + self.v2 + self.v3)
        
        # Constraints
        self.c1 = self.m.addConstr(2 * self.y1+self.y2 + self.v1 - self.v2 == data.h1[s] - X)
        self.c2 = self.m.addConstr(-self.y1+self.y2 +self.v3>= data.h2[s] - 4* X)

    def solve(self):
        self.m.Params.OutputFlag=0 
        self.m.optimize()
        
    def get_objective(self):
        return self.m.objVal
    
    def get_dual(self):
        return self.c1.Pi, self.c2.Pi
        
    def print_solution(self):
        print("Objective : ",self.m.objVal)
        print("y1 : ", self.y1.x)
        print("y2 : ", self.y2.x)
        print("Pi1 : ", self.c1.Pi)
        print("Pi2 : ", self.c2.Pi)


# In[ ]:


class OSP:
    
    def __init__(self,data:Scenarios, s: int,X:float):
        self.m = Model()
        self.data = data
        # Variables
        self.y1 = self.m.addVar(name="y_1")
        self.y2 = self.m.addVar(name="y_2")
        
        # Objective
        self.m.setObjective(self.y1 + 3* self.y2)
        
        # Constraints
        self.c1 = self.m.addConstr(2 * self.y1 + self.y2 == data.h1[s] - X)
        self.c2 = self.m.addConstr(-self.y1 + self.y2 >= data.h2[s] - 4* X)

    def solve(self):
        self.m.Params.OutputFlag=0 
        self.m.optimize()
    
    def get_objective(self):
        return self.m.objVal
    
    def get_dual(self):
        return self.c1.Pi, self.c2.Pi
        
    def print_solution(self):
        print("Objective : ",self.m.objVal)
        print("y1 : ", self.y1.x)
        print("y2 : ", self.y2.x)
        print("Pi1 : ", self.c1.Pi)
        print("Pi2 : ", self.c2.Pi)


# # Solution

# Here we implement the L-Shaped algorithm.

# In[ ]:


data = Scenarios()
mp = MasterProblem(data)
converged = False
iteration = 0
ub = float('inf')
lb = -float('inf')
while (not converged) and (iteration < 5):
    iteration = iteration + 1
    print("Iteration #",iteration)
    
    # Solve MP

    # Get the solution X,Phi to MP
    
    # Update the lower bound
    
    # Check feasibility
    for s in range(data.n_scenarios):
        
        # Create FSP
        
        # Solve FSP

        # Get FSP objective
        
        # Do feasibility test
        
        # If feasibility test fails add a feasibility cut

        # If feasibility test succeeds do nothing

    # If no feasibility cuts have been added:
      # Check optimality 
      for s in range(data.n_scenarios):
            
            # Create OSP
            
            # Solve OSP
            
            # Get OSP objective
            
        
        # Compute recourse function
        
        # Update upper bound

        # Do optimality test

        # If optimality test succeeds: problem solved!

        # Else, add an optimality cut      
    print("Lower bound ",lb," upper bound ",ub)

