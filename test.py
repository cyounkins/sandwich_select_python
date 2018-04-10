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

from apportionment import ApportionmentInstance
from sandwich import SandwichSelect


def test():
    # Test vectors from Mark Beumer thesis "Apportionment in Theory and Practice"
    apportionment_instance = ApportionmentInstance(
        [9061.0, 7179.0, 5259.0, 3319.0, 1182.0],
        26
    )

    ss = SandwichSelect(2, 1)  # Webster / Major Fractions / St. Lagüe / Willcox
    assert ss.apportion(apportionment_instance).assignments() == [[9, 8, 5, 3, 1]]

    ss = SandwichSelect(1, 1)  # Jefferson / Greatest Divisors
    assert ss.apportion(apportionment_instance).assignments() == [[10, 7, 5, 3, 1]]

    ss = SandwichSelect(1, 0)  # Adams / Smallest Divisors
    assert ss.apportion(apportionment_instance).assignments() == [[9, 7, 5, 3, 2]]


if __name__ == "__main__":
    test()
