# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Original Java implementation by Wild, S. and Reitzig, R.
# Python 3 port by Craig Younkins

import random


# Rank selection algorithms as seen in
# <a href="http://algs4.cs.princeton.edu/23quicksort/QuickPedantic.java.html">QuickPedantic</a>
# by <a href="http://algs4.cs.princeton.edu/code/">Sedgewick/Wayne</a>,
# but modified to run on primitive double[]
# @author Sebastian Wild (s_wild@cs.uni-kl.de)
def median(a):
    return a[0] if a.length == 1 else select(a, a.length / 2 - 1)


# Rearranges the elements in a so that a[k] is the kth smallest element, and a[0]
# through a[k-1] are less than or equal to a[k], and a[k+1] through a[n-1] are greater
# than or equal to a[k].
# def select(a, k):
#     if k < 0 or k >= len(a):
#         raise ValueError("Selected element out of bounds")
#
#     random.shuffle(a)
#     lo = 0
#     hi = a.length - 1
#     while hi > lo:
#         i = partition(a, lo, hi)
#         if i > k:
#             hi = i - 1
#         elif i < k:
#             lo = i + 1
#         else:
#             return a[i]
#
#     return a[lo]

# Like {@link #select(double[], int)}, but ignoring positions A[hi+1], A[hi+2], ...
# @param a
# @param hi
# @param k
# @return
def select(a, k, hi=None):
    # NOTE - second and third arguments have been switched in python version
    if hi is not None and hi >= len(a):
        raise ValueError("hi > len(a)")
    if k < 0 or (hi is not None and k >= hi):
        raise ValueError("Selected element out of bounds")

    if hi is None:
        hi = len(a) - 1
        # shuffle everything
        a = random.sample(a, k=len(a))
    else:
        a = random.sample(a[:hi], k=hi) + a[hi:]

    lo = 0

    while hi > lo:
        i = partition(a, lo, hi)
        if i > k:
            hi = i - 1
        elif i < k:
            lo = i + 1
        else:
            return a[i]

    return a[lo]


# partition the subarray a[lo .. hi] by returning an index j
# so that a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
def partition(a, lo, hi):
    assert lo <= hi
    i = lo
    j = hi + 1
    v = a[lo]
    while True:
        # find item on lo to swap
        i += 1
        while a[i] < v:
            if i == hi:
                break
            i += 1

        # find item on hi to swap
        j -= 1
        while v < a[j]:
            # redundant since a[lo] acts as sentinel
            if j == lo:
                break
            j -= 1

        # check if pointers cross
        if i >= j:
            break

        exch(a, i, j)

    # put v = a[j] into position
    exch(a, lo, j)

    # with a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
    return j


# exchange a[i] and a[j]
def exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap
