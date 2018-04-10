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

import rank_selection
import util
from selection import SelectionBasedMethod


class SandwichSelect(SelectionBasedMethod):
    def __init__(self, alpha, beta):
        super().__init__(alpha, beta)

    def unitSize(self, apportionment_instance):
        n = len(apportionment_instance.votes)

        # Find largest population
        maxPop = max(apportionment_instance.votes)

        x_overbar = self.d(apportionment_instance.k - 1) / maxPop + 5 * util.EPSILON
        # x_overbar clearly feasible and suboptimal

        I_x_overbar = []
        Sigma_I_x_overbar = 0
        for i in range(n):
            if apportionment_instance.votes[i] > self.d(0) / x_overbar:
                I_x_overbar.append(i)
                Sigma_I_x_overbar += apportionment_instance.votes[i]

        a_overbar = (self.alpha * apportionment_instance.k + self.beta * len(I_x_overbar)) / Sigma_I_x_overbar
        a_underbar = max(0,
                         a_overbar - ((self.alpha + self.beta) *
                                      len(I_x_overbar))
                         / Sigma_I_x_overbar)

        A_hat_bound = int(math.ceil(
            2 * (1 + self.beta / self.alpha) * len(I_x_overbar)))

        # step 6
        A_hat = [0] * A_hat_bound
        # TODO how is this better than just using an ArrayList?

        A_hat_size = 0
        k_hat = apportionment_instance.k

        for i in I_x_overbar:
            v_i = apportionment_instance.votes[i]
            # If sequence is not contributing, deltaInvRaw might be invalid (< 0 etc),
            # so explicitly handle that case:
            if self.d(0) / v_i > a_overbar:
                continue

            # otherwise: add all elements between a_underbar and a_overbar
            realMinJ = self.deltaInvRaw(v_i * a_underbar)
            minJ = 0 if realMinJ <= 0 else util.fuzzyCeil(realMinJ)
            maxJ = util.fuzzyFloor(self.deltaInvRaw(v_i * a_overbar))
            for j in range(minJ, maxJ + 1):
                A_hat[A_hat_size] = self.d(j) / v_i
                A_hat_size += 1

            # Elements 0,1,...,minJ-1 missing from A_hat
            k_hat -= minJ

        # Selection algorithm is zero-based!
        return rank_selection.select(A_hat, k_hat - 1,  A_hat_size - 1)
