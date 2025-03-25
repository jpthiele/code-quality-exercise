
# Code quality tool exercise
## What do I find here? 
This is a small repository with a purposely buggy Python file. 
The aim is to show usage of various small tools 
for finding and fixing these bugs.

This repo accompanies a workshop on usage of these tools and the slides can be found [here](https://doi.org/10.5281/zenodo.15081373).

## What files are there?
The file `conjugate_gradient.py` implements the 
[conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method).
A copy of it can be found in `conjugate_gradient.py.bak` if you want to easily revert all changes.

The file `.pre-commit-config.yaml` is an example
of a configuration file for the tool `pre-commit` 
discussed in the appendix 
and can be used in the final (optional) exercise. 

## Methods & Tools

The code quality methods discussed in the workshop are
- [Linting](https://en.wikipedia.org/wiki/Lint_(software)), as a static code analysis using [ruff](https://docs.astral.sh/ruff/)
- Formatting using `ruff` again
- Spellchecking using [codespell](https://github.com/codespell-project/codespell)
- (optional) Automating the previous checks with each git commit by using [pre-commit](https://pre-commit.com/) 


