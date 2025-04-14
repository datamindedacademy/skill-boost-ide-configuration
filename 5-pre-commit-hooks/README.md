# Pre-commit hooks

From the [pre-commit documentation](https://pre-commit.com/):

> Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

It's a good practice (especially when working in a team) to add linters, formatters and other types of validation to your *continuous integration* (CI) pipeline. However, waiting for feedback from CI can be a bit slow and cumbersome, especially when working on small changes. Pre-commit hooks allow you to run these checks before you even commit your code, so you can catch issues early.

⚠️ Note that you cannot enforce usage of pre-commit hooks by your peers (they are opt-in, and can be bypassed by running `git commit --no-verify`), which is why they should not be considered a replacement for CI. ⚠️

## Goal of the exercise

The goal of the exercise is to set up and experiment with pre-commit hooks.

In `config.py` you will find that someone has been a bit careless with their passwords. This could have been easily avoided by adding a pre-commit hook!

So: 
1. Install pre-commit: `uv tool install pre-commit` or `pipx install pre-commit`
2. Find an appropriate pre-commit hook to check for passwords in the `config.py` file (hint, there's one from an organization whose name rhymes with "help").
3. Add the pre-commit hook to a `.pre-commit-config.yaml` file in the root of the repository, and install the pre-commit hooks: `pre-commit install`
4. Run the pre-commit hook on the config.py file: `pre-commit run`