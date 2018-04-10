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


class Apportionment(object):
    def __init__(self, k, seats, tiedSeats, astar):
        assert k >= 0 and seats is not None and tiedSeats is not None and astar > 0

        self.k = k
        self.tiedSeats = tiedSeats
        self.astar = astar
        self.seats = seats

    def assignments(self):
        untied = util.kSubsets(self.tiedSeats[:], self.k - sum(self.seats))

        for u in untied:
            assert len(u) == len(self.seats) and util.isBinary(u)
            # "Bad tiebreaker! " + Arrays.toString(u)

            for i in range(len(u)):
                u[i] += self.seats[i]
            # assert sum(u) == k : "Computed assignment has bad number of seats!"

        return untied


class ApportionmentInstance(object):
    def __init__(self, votes, k):
        self.votes = votes

        # house size
        self.k = k
