# Project Euler 100

## About

Problem-solving lies at the very heart of computer science. Finding efficient algorithms is what ultimately enables us to solve ever more complex problems. This project, then, focuses on the steps to develop efficient algorithms from zero for the first 100 hundred problems os <a href='https://projecteuler.net/archives'>Project Euler</a>. Starting with a simple, albeit not always efficient, solution, I analyze which parts of the algorithm hinder its performance and possible ways to work around them. Then, proposing a new way to solve the problem that builds on what previous solutions taught, I create a new algorithm and compare it to the performance of prior solutions.

## Why Project Euler

Ultimately, I choose to solve Project Euler's problems because, different from those hosted on sites such as HackerRank or LeetCode, they are more mathematical in nature. Furthermore, having considered pursuing a math major for most of my high school life, I find that Project Euler's problems provide an excellent opportunity to learn more about that field and enter a joyous journey into areas like number theory, which ultimately makes solving them and trying to create better algorithms much more enjoyable.

## Setting up

This project is, except for some utilities, entirely written using Jupyter Notebooks. Among the many ways to host Jupyter Notebooks, the most popular are using Google Colab and creating a local server.

### Creating a Local Server

The easiest way to set up Jupyter notebooks is using Anaconda. To download and install Jupyter Notebooks, run:

```
conda install -c conda-forge notebook
```

This project also uses **matplotlib** to create graphs, so if it is not already installed, run:

```
conda install -c conda-forge matplotlib 
```

Finally, on the folder with all the notebooks and in the conda environment with matplotlib, run:

```
jupyter notebook
```