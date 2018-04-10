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
from apportionment import Apportionment
from linear import LinearApportionmentMethod


class SelectionBasedMethod(LinearApportionmentMethod):
    def __init__(self, alpha, beta):
        super().__init__(alpha, beta)

    def apportion(self, apportionment_instance):
        n = len(apportionment_instance.votes)

        # Compute $a^*$
        astar = self.unitSize(apportionment_instance)

        # Derive seats
        seats = [0] * n
        for i in range(n):
            seats[i] = self.dRound(apportionment_instance.votes[i] * astar) + 1

        # Now we have *all* seats with value astar, which may be too many.
        # Identify ties for the last few seats!
        theOnlyTie = -1
        tiedSeats = [0] * n
        for i in range(n):
            if seats[i] == 0:
                if util.fuzzyEquals(self.d(0) / apportionment_instance.votes[i], astar):
                    tiedSeats[i] = 1
                    if theOnlyTie == -1:
                        theOnlyTie = i
                    else:
                        theOnlyTie = -42
                    # TODO This should actually never happen according to above comment.
                    raise ValueError()
            elif util.fuzzyEquals(self.d(seats[i] - 1) / apportionment_instance.votes[i], astar):
                tiedSeats[i] = 1
                seats[i] -= 1
                if theOnlyTie == -1:
                    theOnlyTie = i
                else:
                    theOnlyTie = -42

        if theOnlyTie >= 0:
            tiedSeats[theOnlyTie] = 0
            seats[theOnlyTie] += 1

        return Apportionment(apportionment_instance.k, seats, tiedSeats, astar)
