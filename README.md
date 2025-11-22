# Sudoku

This repo is ____, bcs ____

## Learning Objectives:

> Familiarity with Forward-Checking in constrained problems.

> Familiarity with Constraint-Propagation.
> Design a GUI with pygame or a similar library.
> Generate a puzzle without generating a solved version to check if the puzzle is uniquly solvable.
> Publish work as a PyPi package.
> Implement in C/C++

## Generator:
I'll be coding this after the Solver is solved.

## Solver:
Currently I'm going to be coding a simple backpropagation solver and will include the more efficient techniques later on as the project is more developed.


This solver has a few different techniques coded into it:

### Backpropagation:
Most common way to solve this sort of problem. Having a Depth-First-Search (DFS) approach and going back when reaching an invalid state is a common way to solve issues like these. This method has a runtime bound of O(-), assuming no special optimizations but simply well written code.

### Forward-Checking:
This is a technique I learned in my CS 440 - Artificial Intelligence class. By utilizing forward-checking with backpropagation, we can "prune" off branches that we know aren't going to lead to a correct/solved state. 

### Constraint-Propagation:
Similar to Forward-Checking, this goes on to all the other states past the forward-checking cells, and propagates the constraints to different layers in the tree we're iterating through. (I'll provide a much better explanation later.)


## Roadmap:

1) Grid validation utilities
2) Backtracking solver
3) Solver with forward checking
4) Solver with constraint propagation
5) Puzzle generator with uniqueness enforcement
6) Difficulty rating algorithm
7) Pygame GUI
8) Publish as installable Python package


<!-- 
## Install:

Python:

C:

C++:

## Usage:

Examples: -->