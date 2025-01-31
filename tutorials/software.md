---
layout: default #Do not change.
title: "MILP Software" #Article title.
date:   2023-03-09 14:02:54 +0200
author: marco #Author's nick.
---


# Solving MILP Problems in Python

## Introduction

This hands on tutorial aims at introducing students to mathematical
modeling languages. These languages make it possible to write in an easy
and compact way problems in Linear Programming (LP), Integer Programming
(IP) and Mixed Integer Linear Programming (MILP) and to instantiate them
in MILP solvers.

Well known mathematical programming languages are:
[AMPL](http://www.ampl.com/), [GAMS](http://www.gams.com/),
[ZIMPL](http://zimpl.zib.de/) and
[GNU MathProg](http://www.gnu.org/software/glpk/). The last two are open
source.

These languages are declarative type of languages, as opposed to
procedural type. That is, they can be used to define the problem without
saying how it should be solved. Moreover, they allow to separate the
model from the data. In fact, that is essentially all what they do, they
*instantiate* the model on the given data. The output that is used by
the solver can also be used for debugging purposes, that is, to check
that the explicit model is as expected. There are two formats in which
an instantiated MILP can be exported to a file: `.mps` format, which is
an almost universal format among solver systems, but that is not easy to
read and `.lp` format, which is more readable (introduced by CPLEX).

You find a list of commercial or free solvers in this
[page](https://imada.sdu.dk/u/march/Blog/optimization/software/2023/02/12/optsoft.html). Commercial
solvers remain maybe 6-7 time faster than the main free/open-source
solvers.

The NEOS server ([www.neos-server.org](https://neos-server.org/neos/)) provides an
infrastructure to upload an instantiated model and solve it remotedly.

In this course, we use Python. In Python we will import a module, that
makes available a library to pass models to the solver. It is not a
mathematical programming language but the library is very light and
similar to a modelling language.

You can work on your own laptop, in which case it is enough to install
the software there. Alternatively, you can use the
[IMADA Virtual Computer Lab](https://imada.sdu.dk/u/jlandersen/imada/it/complab.html#imada-comp-lab). In
this latter case you will have to install the software in your IMADA
home directory.

We will consider the following alternatives:

- [gurobipy](https://support.gurobi.com)
  Gurobi Python interface to their solver (commercial)
- [Python-MIP](https://github.com/coin-or/python-mip) interface for CBC (free) and Gurobi (commercial)
- [PySCIPOpt](https://github.com/scipopt/PySCIPOpt) interface for SCIP (free)




## Preparation

You can use Google CoLabs and execute the code online. However, it is recommended to set up a local working environment
with the following steps:

- If your operating system is Windows then install the Windows Subsystem
  for Linux (WSL) and work from the shell.

- Ensure you have at least Python 3.10 installed otherwise install it
  <http://python.org/download/>.
   
- Choose and prepare your favourite Python Integrated Development Environment (IDE): For example:
  - [VS Code](https://code.visualstudio.com/docs/python/python-tutorial) (recommended), Spyder3, Emacs, Eclipse, etc. 
  - [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906)
    <!-- If you are on Windows you may consider [PyScripter IDE](http://www.gurobi.com/documentation/current/quickstart_windows/installing_a_python_ide.html).-->

- Choose one of the following:

  - Install `gurobipy` (easiest alternative). Follow these
    [guidelines](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-). The
    recommended installation is via `pip`.  This should install also
    gurobi. To make it work you need also a license from the gurobi web
    page. You could use the tools from
    [here](https://support.gurobi.com/hc/en-us/articles/360059842732)
    and register at the [gurobi page](https://www.gurobi.com) to get
    the license. See also this local page of [guidelines](../gurobi/)
    for a full installation and documentation of gurobi.

  - Alternatively, install Python-MIP with `pip install mip` this should install also
    the solver CBC. If you want to work with gurobi follow these local
    [guidelines](../gurobi.html) for the installation.

  - Alternatively, install SCIP following these
    [instructions](https://github.com/scipopt/PySCIPOpt/blob/master/INSTALL.md) (you need
    to be on Linux, MacOs or WSL). Choose the installation via Precompiled
    Packages.  Then, install `PySCIPOpt` with `pip install pyscipopt`
    preceeded by these
    [instructions](https://www.scipopt.org/index.php#download) under the
    section Requirements. Consult the
    [documentation](https://scipopt.github.io/PySCIPOpt/docs/html/).

We assume that you have previous knowledge of Python programming (a
couple of links to review Python programming are available from the
course Web Page).

In the remaining part of this document you will be guided through some
elements of the course revisited with the use of software. Although the
exercises are about implementing the models at the computer, remember
that the best practice is to first write the mathematical models on
paper! Do that for the subtasks that asks you to derive a mathematical
model.


## Hands on

Continue this tutorial with the hands on parts:

- gurobipy:
  [Part 1](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_gurobi_1.ipynb)
  and
  [Part 2](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_gurobi_2.ipynb)
  of this tutorial.

- python-mip:  [Part 1](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_mip_1.ipynb)
  and
  [Part 2](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_mip_2.ipynb)
  of this tutorial.

- pyscipopt: [Part 1](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_scip_1.ipynb) and [Part 2](https://github.com/DM871/dm871.github.io/blob/main/notebooks/lab_scip_2.ipynb)
