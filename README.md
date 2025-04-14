# Skill Boost: IDE Configuration and Debugging

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/datamindedacademy/skill-boost-ide-configuration)

This repository contains: 
- a devcontainer configuration with some of the tools that are discussed in the skill boost session on IDE configuration and debugging ([slides](https://docs.google.com/presentation/d/1HOhkK2mtWqBviVpXMvX7beettaUngfqOqUJaUd4rdoQ/edit?slide=id.p#slide=id.p))
- Exercises to become familiar with these tools 

The exercises are designed with "self-service" in mind: each folder contains a `README.md` that explains the what and why of the exercise, so people that did not attend the skill boost session can also benefit from the material.

Any and all feedback (suggestions, fixes, additional exercises, ...) is welcome!

Topics:
1. [Python Version Management](./1-python-versions/README.md)
2. [Virtual Environments](./2-virtual-environments/README.md)
3. [Debugging](./3-debugging/README.md)
4. [Linters and Formatters](./4-linters/README.md)
5. [Pre-commit Hooks](./5-pre-commit-hooks/README.md)
6. [Notebooks](./6-notebooks/README.md)

\
Note: The extensions in the `.devcontainer.json` file are VSCode-specific. Nevertheless, JetBrains IDEs (IntelliJ, PyCharm) also support the devcontainer specification, so it should be possible to solve the exercises in those IDEs as well. Users of JetBrains IDEs are welcome to add any plugins they deem necessary to the `customizations` section of the `devcontainer.json` configuration. 