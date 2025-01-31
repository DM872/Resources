---
layout: default #Do not change.
title: Gurobi #Article title.
date:   2023-03-09 14:02:54 +0200
author: marco #Author's nick.
nav_order: 5
nav_exclude: true
---


## Installation of Gurobi


- Download from <https://www.gurobi.com/downloads/>

- Register to get an academic
  [license](https://www.gurobi.com/downloads/end-user-license-agreement-academic/).
  It will last three months.

- Install Gurobi following the instructions at the
  [Quick Start Guide](https://www.gurobi.com/documentation/quickstart.html)
  relative to your system. You can install all software via the
  (Ana)conda Python distribution. However, note that if you have already
  Python installed you may end up having two distributions of it in
  your systems, which often creates confusion. Hence, the conda
  distribution is not recommended in this course.

- Install the Gurobi Python Interface (`gurobipy`) following these
  [instructions](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-)
  <!--
  [mac](https://www.gurobi.com/documentation/9.1/quickstart_mac/cs_grbpy_the_gurobi_python.html),
  [linux](https://www.gurobi.com/documentation/9.1/quickstart_linux/cs_grbpy_the_gurobi_python.html),
  [windows](https://www.gurobi.com/documentation/9.1/quickstart_windows/cs_grbpy_the_gurobi_python.html)
  (manual installation recommended)
  -->

- run `grbgetkey` using the argument provided at the license
  registration page (ex: grbgetkey
  ae36ac20-16e6-acd2-f242-4da6e765fa0a). The 'grbgetkey' program will
  prompt you to store the license file on your machine (to do this step
  you must be within the SDU Net via
  [VPN connect](https://any.sdu.dk/)).



## Recommended documentation material


Gurobi has an excellent
[documentation](https://www.gurobi.com/resources/?category-filter=documentation),
which it may appear overwhelming. Here is a list of recommended material:

-   you can get an introduction to modeling in Python with gurobi
    watching at least the first 34 minutes of this video: [Python I:
    Introduction to modeling with
    Python](http://www.gurobi.com/resources/seminars-and-videos/python-I-webinar)

-   two other
    [tutorials](https://www.gurobi.com/resources/seminars-and-videos/?category-filter=tutorials)
    on LP and MILP are available

-   an abundance of [application
    cases](https://www.gurobi.com/resources/seminars-and-videos/?category-filter=seminars-and-videos)

-   [examples](https://www.gurobi.com/documentation/9.1/examples/index.html)

-   [the Application Program Interface
    (API)](http://www.gurobi.com/documentation/current/refman/py_python_api_details.html).
