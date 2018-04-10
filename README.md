A Python 3 port of the SandwichSelect algorithm originally written by Sebastian Wild and Raphael Reitzig and described in their 2015 paper "A Practical and Worst-Case Efficient Algorithm for Divisor Methods of Apportionment".

Few changes were made from the original implementation. The most significant is that the second and third parameters for rank_selection.select() were swapped to better accommodate the optional third parameter.

Java implementation: https://github.com/reitzig/2015_apportionment
Also included is a copy of `double.py` by Martin Jansche  (http://symptotic.com/mj/double/double.py).
Test vectors by Mark Beumer in "Apportionment in Theory and Practice"

This repo is not yet a proper Python package. To run the tests, simply clone and run `python test.py`
