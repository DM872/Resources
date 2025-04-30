# Obligatory Assignment 2 

## Preface

- This is the second of the two assignments that will be graded and will
  determine your final assessment in DM872.

- This assignment must be carried out in groups of two persons. Groups of
  different sizes must be agreed with the teachers.

- To complete the assignment you have to submit in ItsLearning a `.tgz` or `.zip` archive
  named `asg2.tgz` or `asg2.zip` that decompress in the same structure as the
  `asg2` directory in this repository:

  ```{shell}
  asg2/
  ├── README.md
  ├── data
  ├── src
  └── tex
      └── main.pdf
  ```
  - `data` contains the problem instances

  - `tex` contains your report in pdf format as concise as possible (by no way more than 10
    pages) with the answers to the tasks. The report should be written
    in Latex using this [template](tex/template.tex).

  - `src` must contain the Python code for the calculations you carried out.

- **Deadline:** Saturday, May 31, 2025, at 23:59

- Questions and answers about this assignment cannot be addressed to the
  teachers but must be posted as issues in the github page
  [Issues](https://github.com/DM872/Resources/issues). Start the title with
  `[asg2]`. In this way, the communication will be visible to the other class
  members as well.

- Changes to this document after publication on May 1 can be tracked using the
  History link on the top right side of this page.

- You are recommended to read the Guide on the use of Generative AI at SDU
  [https://mitsdu.dk/AIatSDU](https://mitsdu.dk/en/mit_studie/kandidat/matematik-oekonomi_kandidat/vejledning-og-support/aipaasdu).
  In this assignment, you can use chatbots to help you resolving coding issues
  but you are not allowed to use them to directly solve the tasks or to write
  the text of the report. Setting clear boundaries is not an easy task, so if
  you use chatbots you must share the chat and provide the link in the report.
  The chat can be left anonymous and always ensure you are not sharing sensitive
  or personal information. If the chatbot does not support chat sharing, then
  you can manually share the content by 1. copying the text from the chat; 2.
  pasting it into a note/document (e.g., Google Docs, Notes, Word); 3.
  generating a shareable link via that platform (if supported). Alternatively,
  you can paste the chat in an appendix of the report beyond the page limit. The
  content of the communication will not be used to determine whether you have
  been cheating but rather as an indication of how much help you needed to solve
  the assignment.

- Looking through some of your submissions for asg1 and reported usage of chatGPt, we
  would like to recommend you to restrict the use of ChatGPT to technical
  questions on programming and on language only, and to read relevant papers in the 
  reference list on your own, allowing you to come up with your own problem formulations, cut /
  column generation routines, etc., without relying on ChatGPT.

## Problem Description

In this assignment, you will consider a delivery problem instance with
side constraints. Specifically, a truck company deals with delivery of
replenishments to stores on a particular day to 200 retailers. All the
orders can not fit to a single truck due to weight limitations. Hence,
multiple vehicles have to be involved in the delivery process. The goal
is to determine:

- an appropriate number of vehicles of the identical capacity of $Q=12600$ kg

- the routes these vehicles should take to organize the delivery respecting the
  time intervals provided and travelling the least possible total distance

In addition, note that:

- customer demands are represented in kg and should not split, i.e., every customer should be visited by one truck only

- the distances between locations are Euclidian and can be calculated using the
  coordinates provided

- the speed of trucks is $1000$ distance units / h

- all the retail stores have specific time intervals, when they are available to
    receive the order. **Note that some retailers have multiple time intervals**,
    which means that delivery must take place during one of the presented
    time intervals

- you can assume that a delivery truck may wait at the location in case it arrives
  early, if that is needed

- you can also assume that all the locations are in the same time zone, i.e., no
  time adjustments are needed when determining the arrival times

- the problem instance contains the service times, i.e., the times required to
    unpack the order, expressed in minutes. You can assume that the arrival,
    i.e., the start of service, must start within the time interval, but not
    necessary end within the same inteval.

All the details can be found in the instance files in `data`. A separate
file exists that provide you with location coordinates, order weights,
service times and time window intervals. 

## Your Task

As delivery decision support assistants, your job is to:

1. determine an appropriate exact solution methodology for this problem, i.e.,
    present a problem formulation that models the truck routes within capacity
    and specifically accounts for multiple alternative time window intervals and
    service times, together with possible cut and / or column generation
    strategy

2. develop the code implementing the chosen methodology

3. report the best solution you manage to obtain (number of vehicles and total travelled distance), together with a possible
    optimality gap if the problem is not solved to optimality, and a visualization of this solution.

Note that solving the problem to optimality is not a requirement.
Therefore, it is acceptable to employ a solution methodology that is
theoretically exact, but use it to obtain a suboptimal solution as long
as an optimality gap can be derived using your methodology.

To assist you in your decision making you are referred to your class
notes and the following additional references. Given that one part of
the problem is the Capacitated Vehicle Routing Problem, you are referred
back to class notes for references. The additional part of this problem
deals with delivery time requirements. First, (Ascheuer, Fischetti, and
Grötschel 2001) presents several approaches to model time window
constraints, including the label-setting based approach (MTZ) and the
approach resembling the one-commodity network flow idea. The
strengthened MTZ approach for modeling time window constraints presented
on page 486 of (Ascheuer, Fischetti, and Grötschel 2001) contained
errors, and was corrected in (Yuan et al. 2020). References to other
solution approaches, including the ones involving set partitioning
formulations and column-generation methods, can be found in (Feillet
2010; Irnich and Desaulniers 2005; Gualandi and Malucelli 2012),
(Baldacci, Mingozzi, and Roberti 2012), as well as other papers
available online.

**Acknowledgement**. This assignment employs a problem instance, appeared earlier
in a public [Operations Research
challenge](https://www.linkedin.com/posts/borjamenendezmoreno_operationsresearch-activity-7277227758991142913-Hamd),
with the consent from the author.


## References

::: 
Ascheuer, Norbert, Matteo Fischetti, and Martin Grötschel. 2001.
"Solving the Asymmetric Travelling Salesman Problem with Time Windows by
Branch-and-Cut." *Math. Program.* 90 (3): 475--506.
<https://doi.org/10.1007/PL00011432>.
:::

::: 
Baldacci, Roberto, Aristide Mingozzi, and Roberto Roberti. 2012. "Recent
Exact Algorithms for Solving the Vehicle Routing Problem Under Capacity
and Time Window Constraints." *Eur. J. Oper. Res.* 218 (1): 1--6.
<https://doi.org/10.1016/J.EJOR.2011.07.037>.
:::

::: 
Feillet, Dominique. 2010. "A Tutorial on Column Generation and
Branch-and-Price for Vehicle Routing Problems." *4OR* 8 (4): 407--24.
<https://doi.org/10.1007/S10288-010-0130-Z>.
:::

:::
Gualandi, Stefano, and Federico Malucelli. 2012. "Resource Constrained
Shortest Paths with a Super Additive Objective Function." In *Principles
and Practice of Constraint Programming - 18th International Conference,
CP 2012, Québec City, QC, Canada, October 8-12, 2012. Proceedings*,
edited by Michela Milano, 7514:299--315. Lecture Notes in Computer
Science. Springer.
<https://doi.org/10.1007/978-3-642-33558-7_24>.
:::

::: 
Irnich, Stefan, and Guy Desaulniers. 2005. "Shortest Path Problems with
Resource Constraints." In *Column Generation*, edited by Guy
Desaulniers, Jacques Desrosiers, and Marius M. Solomon, 33--65. Boston,
MA: Springer US. <https://doi.org/10.1007/0-387-25486-2_2>.
:::

:::
Yuan, Yuan, Diego Cattaruzza, Maxime Ogier, and Frédéric Semet. 2020. "A
Note on the Lifted Miller-Tucker-Zemlin Subtour Elimination Constraints
for Routing Problems with Time Windows." *Oper. Res. Lett.* 48 (2):
167--69. <https://doi.org/10.1016/J.ORL.2020.01.008>.
:::
