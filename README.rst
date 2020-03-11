.. image:: https://travis-ci.com/NLESC-JCER/ci_for_science.svg?branch=master
    :target: https://travis-ci.com/NLESC-JCER/ci_for_science
.. image:: https://github.com/NLESC-JCER/ci_for_science/workflows/build%20with%20conda/badge.svg
    :target: https://github.com/NLESC-JCER/ci_for_science/actions
.. image:: https://gitlab.com/nlesc-jcer/ci_for_science/badges/master/pipeline.svg
    :target: https://gitlab.com/nlesc-jcer/ci_for_science/badges/master/pipeline.svg

################################################################################
👩‍🚀 📡 🔬 Continuous Integration for Scientific Applications
################################################################################
This repository contains a brief example of Continuous integration for scientific applications,
using miniconda_ and Python3.

Overview
********
`Continuous Integration <https://en.wikipedia.org/wiki/Continuous_integration>`_ (**CI**) helps to automate the testing and delivery of scientific software tools. A **CI** is just a workflow that runs automatically 🤖 as a result of a certain action
taken in the source code (e.g. a push, pull-request, etc.).

This repository contains 3 different configuration files for *Github Actions*, *Travis* and *Gitlab CI*. These configuration files encode the actions to perform with the code on a given architecture, like installing the library from scratch in a Ubuntu machine.

###########################
🛠️ Setting up a CI workflow
###########################

|octocat| GitHub actions
************************
The *Github actions* configuration can be found at `Python actions file <.github/workflows/pythonapp.yml>`_. There is comprehensive documentation of what `Github actions`_ are and how to use them.

.. |octocat| raw:: html

   <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40pt">

|Travis| Travis CI
******************
The `Travis configuration file <.travis.yml>`_ contains the configuration to call a **CI** workflow using *Travis*. See `Travis tutorial`_.

.. |Travis| raw:: html

   <img src="https://travis-ci.com/images/logos/TravisCI-Mascot-pride-4.png" width="40pt">

|gitlab| GitLab CI
*********
The `GitLabCI configuration file <.gitlab-ci.yml>`_ contains the configuration to call a **CI** workflow using the *Gitlab CI*. A comprehensive documentation is available for the `GitLab CI`_ tool.

.. |gitlab| raw:: html

   <img src="https://about.gitlab.com/images/ci/gitlab-ci-cd-logo_2x.png" width="40pt">

Azure pipelines
***************
If you want to use `Azure pipelines, <https://azure.microsoft.com/en-us/services/devops/pipelines/>`_ have a look at `Tania Allard's great tutorial <https://github.com/trallard/ci-research>`_.

##################################
🚀 Running on your own infrascture
##################################
Sometimes you want to have more control over the hardware infrascture, compilers, etc. when performing
continuous integration. *GitHub Actions* and *GitLab CI/CD* allow you to set up your infrascture.
The following links contains a guide to help you run a **CI** workflow on your own infrascture:

- `GitLab CI/CD self-hosted runner <https://github.com/NLESC-JCER/gitlab_runner>`_
- `GitHub Actions self-hosted runnner <https://github.com/NLESC-JCER/linux_actions_runner>`_


###############################
🎮 Running the package examples
###############################
This package contains a toy example to estimate the value of π using the `Monte Carlo method`_.
To run the Monte Carlo calculator, you will need to have python install. We recommend you
create a `conda virtual environment <https://docs.conda.io/projects/conda/en/latest/index.html>`_ by following the instructions below,

1. Get a copy of `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
2. Create a new environment by running the following command:
    ``conda create --name ci_for_science python=3.7 -y -q``
3. Activate the environment:
    ``conda activate ci_for_science``

Now to install this package,

4. `Fork and clone this repo <https://help.github.com/en/github/getting-started-with-github/fork-a-repo>`_
5. install cython:
    ``pip install cython``
6. install the library from the root folder:
    ``pip install -e .``
7. run the command line interface like:
    ``compute_pi -n 1000``
The previous command will estimate π using 1000 random points.

Contributing
************

If you want to contribute to the development of ci_for_science,
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

License
*******

Copyright (c) 2019-2020, 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Credits
*******

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.

.. _miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _`Github actions`: https://help.github.com/en/actions/automating-your-workflow-with-github-actions
.. _`GitLab CI`: https://docs.gitlab.com/ee/ci/
.. _`Tania Allard great tutorial`: https://github.com/trallard/ci-research
.. _`Travis tutorial`: https://docs.travis-ci.com/user/tutorial/
.. _`Monte Carlo method`: https://en.wikipedia.org/wiki/Monte_Carlo_method
