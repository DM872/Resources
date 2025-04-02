# Obligatory Assignment 1

## Preface

- This assignment will be graded and will contribute to your final
  assessment in DM872. Overall there will be two assignments.

- This assignment must be carried out individually.

- To complete the assignment you have to submit in ItsLearning a `.tgz` or `.zip` archive
  named `asg1.tgz` or `asg1.zip` that decompress in the same structure as the
  `asg1` directory in this repository:

  ```{shell}
  asg1/
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

- **Deadline:** <s>Thursday, April 11, 2025, at 23:59</s> **Wednesday, April 16, 2025, at 23:59**

- Questions and answers about this assignment cannot be addressed to the
  teachers but must be posted as issues in the github page
  [Issues](https://github.com/DM872/Resources/issues). Start the title with
  `[asg1]`. In this way, the communication will be visible to the others class
  members as well.

- Changes to this document after publication on March 9 can be tracked using the
  History link on the top right side of this page.

- You are recommended to read the Guide on the use of Generative AI at SDU
  [https://mitsdu.dk/AIatSDU](https://mitsdu.dk/en/mit_studie/kandidat/matematik-oekonomi_kandidat/vejledning-og-support/aipaasdu).
  In this assignment, you can use chatbots to help you resolving coding issues
  but you are not allowed to use them to directly solve the tasks or to write
  the text of the report. As setting clear boundaries is not an easy task, if
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

## Problem Description

In this assignment, you are going to work on a version of the Traveling
Salesman Problem known as the Generalized Traveling Salesman Problem
(GTSP). The problem is characterized by

-   set of nodes $V = \\{1,\ldots,n\\}$

-   set of clusters $\mathcal{K} = \\{1,\ldots,m\\}$

-   clusters $C_k \subset V, k \in \mathcal{K}$, such that
    $V = \cup_{k\in \mathcal{K}} C_k$

-   distance matrix $D=\\{d_{ij} \| i, j \in V, i \neq j\\}$ where
    $d_{ij}$ represents the distance between nodes $i$ and $j$. It is
    assumed that matrix $D$ is symmetric.

The objective of the problem is to find a minimum distance tour visiting
one node in every cluster once. The problem is illustrated in the
following figure. Each cluster is visited exactly once.

<div style="text-align:center;">
<img src="tex/gtsp_image.png" alt="example" width="350">
</div>

GTSP finds application in warehouse management, route and production
planning, see (Laporte, Asef-Vaziri, and Sriskandarajah 1996) and (Pop
et al. 2024). The study by (Fischetti, Salazar González, and Toth 1997)
provided one of the most detailed analysis of the theoretical properties
of the problem to date.

## Your Tasks

Your overall task is to design and implement a solution algorithm for
the GTSP and report results of computational experiments of your
algorithm on 3 problem instances provided with this assignment.

More specifically, your task can be decomposed into subtasks as follows:

1.  Present a mathematical programming formulation of the
    problem and argue shortly for its correctness.

2.  Design and implement a solution algorithm to solve the chosen
    formulation.

3.  Argue whether your solution algorithm favors finding a better
    solution or it focuses more on improving the lower bound to the
    optimal solution.

Requirements for the proposed algorithm:

-   Your algorithm must address the problem of identifying violated,
    valid inequalities as discussed in (Fischetti, Salazar González, and
    Toth 1997).

-   Separation of violated valid inequalities must be implemented based upon the
    fractional values of decision variables, either at the root node of
    the problem or within a callback. In other words, you implement
    either a cut-and-branch or branch-and-cut algorithm and justify your
    choice.

The computational results should demonstrate the effectiveness of your
algorithm demonstrated on the three problem instances provided:

| instance name |  clusters|  nodes|
|---------------|----------|-------|
| instance 1    |         20|    100|
| instance 2    |         45|    225|
| instance 3    |         89|    442|

Every instance is provided in the format of two files. One file lists the
clusters, one cluster defined in every line. Another file contains the
coordinates of the locations involved in the GTSP. Once the Euclidian distance
between two locations is calculated, the result is rounded using `numpy.round()`
function to keep all the distances integer-valued and to streamline the
comparison of the results. Your results must contain the objective value of the
best solution, the lower bound and the corresponding optimality gaps obtained at
the time limit for every problem instance. Ideally, you could let your
experiments run until proved optimality. However, a time limit to the
computation time of 1,000 seconds could also be enough.

## References

::: 
Fischetti, Matteo, Juan José Salazar González, and Paolo Toth. 1997. "A
Branch-and-Cut Algorithm for the Symmetric Generalized Traveling
Salesman Problem." *Operations Research* 45 (3): 378--94.
:::

::: 
Laporte, Gilbert, Ardavan Asef-Vaziri, and Chelliah Sriskandarajah.
1996. "Some Applications of the Generalized Travelling Salesman
Problem." *Journal of the Operational Research Society* 47 (12):
1461--67.
:::

::: 
Pop, Petrică C, Ovidiu Cosma, Cosmin Sabo, and Corina Pop Sitar. 2024.
"A Comprehensive Survey on the Generalized Traveling Salesman Problem."
*European Journal of Operational Research* 314 (3): 819--35.
:::
