# Notebooks

There's a time and place for everything, even for notebooks. For a Dataminded™-approved summary of the pros and cons of notebooks, check out [this Medium article](https://medium.com/datamindedbe/from-notebook-hell-to-container-heaven-20cbe05100a1). 

In summary, notebooks are great for:
- 💨 Quick iterations and tight feedback loop
- 📈 Data Exploration + Early Visualisation
- 🤖 Building Machine Learning models

And not so great when it comes to:
- 🤐 Secrets management
- 🧱 Modularisation
- 🧪 Testing
- 🔁 Reproducibility
- 📜 Versioning and Collaboration

## Goal of the exercise

In this exercise, there is a notebook that contains some code to plot the monthly stargazers of the `data-product-portal` repository over time.

The goal of this exercise is to make sure that the notebook can be checked in into version control, so that others can reproduce the plot, *without* committing the plot itself.

Remember: notebooks can contain both code and output, and output can contain sensitive information. Committing the code, and making sure that it can be run by others, is the goal of this exercise.

To complete the exercise, you need to:
- Figure out the dependencies of the notebook, and make sure that others can run it as well.
- Ensure that only the code gets committed to Git, not the plot. Hint: there is a pre-commit hook that can help you with that. 