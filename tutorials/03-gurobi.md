
## Installation of Gurobi

- Download from <https://www.gurobi.com/downloads/>


- Install Gurobi following the instructions at the
  [Quick Start Guide](https://www.gurobi.com/documentation/quickstart.html)
  relative to your system. You can install all software via the
  (Ana)conda Python distribution. However, note that if you have already
  Python installed you may end up having several distributions of it in
  your systems, which often creates confusion. Hence, the conda
  distribution is not recommended in this course. Use `pyenv` to have a better control
  over Python versions.

- Install the Gurobi Python Interface (`gurobipy`) following these
  [instructions](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python-)
  The recommended installation is via `pip`.  This should install also the
  gurobi solver library.
  
  <!--
   To make it work you need also a license from the gurobi
    web page. You could use the tools from
    [here](https://support.gurobi.com/hc/en-us/articles/360059842732) and
    register at the [gurobi page](https://www.gurobi.com) to get the license.
    See also this local page of [guidelines](../gurobi/) for a full installation
    and documentation of gurobi.
    -->
  <!--
  [mac](https://www.gurobi.com/documentation/9.1/quickstart_mac/cs_grbpy_the_gurobi_python.html),
  [linux](https://www.gurobi.com/documentation/9.1/quickstart_linux/cs_grbpy_the_gurobi_python.html),
  [windows](https://www.gurobi.com/documentation/9.1/quickstart_windows/cs_grbpy_the_gurobi_python.html)
  (manual installation recommended)
  -->

- Register to get a temporary academic
  [license](https://www.gurobi.com/downloads/end-user-license-agreement-academic/).
 
- run `grbgetkey` using the argument provided at the license
  registration page (eg: grbgetkey
  ae36ac20-16e6-acd2-f242-4da6e765fa0a). The `grbgetkey` program will
  prompt you to store the license file on your machine (to do this step
  you must be within the SDU Net via
  [VPN connect](https://any.sdu.dk/)).


## Recommended documentation material


- Solving MILP Problems in Python with Gurobi: [Modelling 1](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-1.pdf); [Modelling 2](https://www.gurobi.com/pdfs/user-events/2017-frankfurt/Modeling-2.pdf);
[Algorithms 1](https://assets.gurobi.com/pdfs/user-events/2017-frankfurt/Algorithms-I.pdf);
[Algorithms 2](https://assets.gurobi.com/pdfs/user-events/2017-frankfurt/Algorithms-II.pdf)

- Gurobi has an excellent [documentation](https://docs.gurobi.com/current/).

- The gurobi github [modeling-examples](https://github.com/Gurobi/modeling-examples) repository.

<!--
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

-->

