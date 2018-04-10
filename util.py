# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Original Java implementation by Wild, S. and Reitzig, R.
# Python 3 port by Craig Younkins

import math

import double

EPSILON = 1E-14
MANTISSA_EPSILON = 16


def isBinary(arr):
    return all([i in (0, 1) for i in arr])


def kSubsets(v, k):
    assert v is not None and isBinary(v)

    result = []
    if k <= 0:
        # return only the zero-vector
        result.append([0] * len(v))
    elif sum(v) < k:
        # not enough ones --> return empty set
        pass
    else:
        # k > 0 and sum(v) >= k
        # Find first 1
        j = 0
        for j in range(len(v)):
            if v[j] == 1:
                break
        assert j < v.length and v[j] == 1

        # Recurse for picking this vs not picking this 1
        v[j] = 0
        v1 = v[:]

        # For picking this 1
        res1 = kSubsets(v1, k-1)
        for a in res1:
            a[j] = 1
            result.append(a)

        # For not picking this 1
        v1 = v[:]
        result.extend(kSubsets(v1, k))

    return result


def fuzzyFloor(x):
    if x < -1:
        raise ValueError("fuzzyFloor only works for x >= -1")
    if x < 0:
        return -1 if x < -EPSILON else 0

    xTimesOnePlusEps = double.longBitsToDouble(double.doubleToRawLongBits(x) + MANTISSA_EPSILON)
    return int(math.floor(xTimesOnePlusEps))


def fuzzyCeil(x):
    # TODO enable negative parameters
    if x < 0:
        raise ValueError("fuzzyCeil only works for x >= 0")
    xTimesOneMinusEps = double.longBitsToDouble(double.doubleToRawLongBits(x) - MANTISSA_EPSILON)
    return int(math.ceil(xTimesOneMinusEps))


def fuzzyEquals(x, y):
    return abs(x - y) < EPSILON
