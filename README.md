# Movies README

Project for Intro to Programming / Full Stack Nanodegree on Udacity.com.

Creates a movie trailer webpage `fresh_tomatoes.html`.

Written for [python 2.7](https://www.python.org/)

## Installation

Install [python 2.7](https://www.python.org/).
Clone the GitHub repository.

	$ git clone https://github.com/Tamburkey/Movies.git

## Contents

This directory contains 3 python files:
[entertainment_center.py](entertainment_center.py),
[fresh_tomatoes.py](fresh_tomatoes.py),
[media.py](media.py)

## Description

`media.py` contains the class `Movie` constructor and methods.

`fresh_tomatoes.py` contains the html structure and python functions
which create the `fresh_tomatoes.html` file.

`entertainment_center.py` is a python script which imports class `Movie`
from `media.py`, creates instances of class `Movie` in an array `movies`,
and runs the `.open_movies_page` function from `fresh_tomatoes.py`on the
`movies` array, which creates `fresh_tomatoes.html` in the Movies directory.

## Use

After cloning the [master repository](https://github.com/Tamburkey/Movies.git)
and running `entertainment_center.py` using python 2.7, open the file 
`fresh_tomatoes.html` in a browser to view the movie trailer website.
