# Stat 159 - Project 3
## An analysis of demographics information, 1994

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/berkeley-stat159-f17/project-3-p2-ou-yu-li/master?filepath=demographics-p1.ipynb) [![Build Status](https://travis-ci.org/berkeley-stat159-f17/project-3-p2-ou-yu-li.svg?branch=master)](https://travis-ci.org/berkeley-stat159-f17/project-3-p2-ou-yu-li)

**Team**: project-3-p2-ou-yu-li

**Members**: Aaron Ou, Julien Yu, Brian Lin

**Articles on**: https://berkeley-stat159-f17.github.io/project-3-p2-ou-yu-li/

## Purpose of the repository

The dataset we work on is named adult.csv (1994, UC Irvine Machine Learning Repository), which consists of the demographic information (i.e. age, work class, education, race, sex, etc.) about adults with an occupation.

We would like to analyze the relationship between different explanatory variables. For example, does one’s gender affect how many years of education they obtain? What about one’s race? These questions are essential, not only to understand the American society of 20 years ago, but also to understand that of today.

## Instructions for reproduction

Clone the repo folder from github and rename it to p3:

`git clone https://github.com/berkeley-stat159-f17/project-3-p2-ou-yu-li.git p3`

Make sure you have **Anaconda** installed in your local machine.
Ref: https://www.anaconda.com/download/#linux

To set up the proper environment with prerequisites (Python, a few python packages, Sphinx etc). Run the following: 
```
cd p3 # go to the p3 folder
make env # create an environment named `demographics`
source activate demographics # activate the environment named `demographics`
make all # run all ipython notebooks

```

Run unit tests: 

`python folder/testing.py`

## Folder and files

- **data**: store the raw data csv file
- **fig**: store the figures created from notebook
- **functions**: store the python functions that will be reused across notebooks
- **results** : store the cleaned data files created from notebook

## Licensing conditions
MIT License

Copyright (c) 2017 Reproducible and Collaborative Statistical Data Science

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.