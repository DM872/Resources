# Practice


## Task 1

Vehicle Routing with Stochastic Demand (VRPSD)

- Serve all customers.

- The demand of each customer $i$ is given by a
random variable $\xi_i$. The probability distribution
is assumed to be known. We
assume the variables are independent.

- Assume $\xi$ is Poisson distributed.

- Each vehicle has a capacity $Q$.

- We have to plan routes in advance. When executing the plan it may turn out
that the planned route violates the capacity constraint.  In that case, the
vehicle returns to the depot to empty/restock the vehicle. 

- We do not do preventive restock. Demands become known only when arriving at
  the customer.

- We enforce that the sum of expected demands on each route should be less
than vehicle capacity

- Objective: Minimize the expected cost of the solution.

Data:

$$
\begin{array}{rrr}
&X& Y &\lambda_i\\
0 &50 &50 &0\\
1 &1 &18 &12\\
2 &62 &80 &8\\
3 &25 &39 &4\\
4 &18 &22 &10\\
5 &43 &87 &11\\
6 &97 &100 &5\\
7 &32 &88 &5\\
8 &77 &22 &5
\end{array}
$$

Vehicle capacity 30.


(Solution in slides 05-StochVRP.pdf available in ItsLearning)

## Task 2

Vehicle Routing with Time Windows and Stochastic Travel Times 

As the CVRP but:

- For each arc $(i,j)$ there is an associated travel time $t_{ij}$ and travel
cost $c_{ij}$

- Here we consider minimizing the cost $c_{ij}$ of the used arc

- For each customer $i$ there is an associated service time $s_i$.

- For each node $i$ there is an associated time window $[a_i,b_i]$.

- Nodes must be visited within their time windows.

- The vehicle can wait if it arrives too early

- Assume travel time $\tau_{ij}$ is a stochastic variable normally distributed
  around the mean $t_{ij}$

- Assumptions:

  - For simplicity we assume that service time is zero for all customers [no
problem to ”lift” this assumption]

  - We assume that the stochastic variables $\tau_{ij}$ are independent [not very
realistic]

(Solution in slides 05-StochVRP.pdf available in ItsLearning)

## Task 3

[Precision Farming](https://www.linkedin.com/pulse/precision-farming-meinolf-sellmann-e6bwe)