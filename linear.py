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

import util


class LinearApportionmentMethod(object):
    def __init__(self, alpha, beta):
        self.alpha = float(alpha)
        self.beta = float(beta)

    def d(self, j):
        j = int(j)
        if j < 0:
            raise ValueError("Got j="+j)
            # The convention in the article was -infty for negative values,
            # but a single convention that can consistently be used in all cases seems
            # to be impossible, so check for negative values on call site.
            # Usually, this makes the difference between a party that has 0 seats
            # and one that has at least one seat, so often a case distinction is
            # needed anyway.

        return self.alpha * j + self.beta

    def deltaInvRaw(self, x):
        return (float(x) - self.beta) / self.alpha

    def deltaInv(self, x):
        return max(-1, self.deltaInvRaw(float(x)))

    def dRound(self, x):
        return util.fuzzyFloor(self.deltaInv(float(x)))

    def isStationary(self):
        return 0 <= self.beta / self.alpha and self.beta / self.alpha <= 1
