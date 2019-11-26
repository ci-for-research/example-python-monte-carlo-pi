################################################################################
Continuous Integration for Scientific Applications
################################################################################
👩‍🚀 This repository contains a brief example of Continuous integration for scientific applications,
using miniconda_ and Python3.

Overview
********
`Continuous Integration`_ (**CI**)  **CI** helps to automate the testing and delivery of scientific software tools. A **CI** is just a workflow that runs automatically as a result of a certain action
taken in the source code (e.g. a push, pull-request, etc.).

_`Continuous Integration`: https://en.wikipedia.org/wiki/Continuous_integration

In this repository there are stored 3 different configuration files for *Github Actions*, *Travis* and *Gitlab CI.*. These configuration files encodes the actions to perform with the code on a given
architecture, like installing the library from scratch in a Ubuntu machine.

GitHub actions
**************
The *Github actions* configuration can be found at `Python actions file <.github/workflows/pythonapp.yml>`_. There is comprehensive documentation of what are `Github actions`_ and how to use them.

Travis CI
*********
The `Travis configuration file <.travis.yml>`_ contains the configuration to call a **CI** workflow using the *Travis*. See `Travis tutorial`_.

Gitlab CI
*********
The `GitlabCI configuration file <.gitlab-ci.yml>`_ contains the configuration to call a **CI** workflow using the *Gitlab CI*. A comprehensive documentation is available for the `GitLab CI`_ tool.

Azure pipelines
***************
If you want to uze the `Azure pipelines`_ Have a look at `Tania Allard great tutorial`_.

_`Azure pipelines`: https://azure.microsoft.com/en-us/services/devops/pipelines/

Contributing
************

If you want to contribute to the development of ci_for_science,
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

License
*******

Copyright (c) 2019, 

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
